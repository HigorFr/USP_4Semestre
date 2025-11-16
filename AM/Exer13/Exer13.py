
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv1D, LSTM, Dense, Dropout, concatenate
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping



#DISCLAIMER: Usei ChatGPT para auxiliar em grande parte do código.


#Leitura e preparação dos dados

data = pd.read_csv("Exer13/ibovnew.csv")

#Se houver datas, ordena cronologicamente
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values('Date')

#Normaliza as features numéricas principais
features = ['Open', 'Close', 'Min', 'Max', 'Mean']
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(data[features])


#Criação da variável-alvo com 3 classes (Caixa de previsão)

# Exemplo simples: se o fechamento de amanhã for:
# maior que o de hoje + limiar → sobe
# menor que o de hoje - limiar → desce
# caso contrário → estável

limiar = 0.005  # 0.5% de variação

returns = data['Close'].pct_change().shift(-1)
y = np.select(
    [returns > limiar, returns < -limiar],
    [2, 0],  # 2 = sobe, 0 = desce
    default=1  # 1 = estável
)

#Remove última linha (sem target futuro)
X_scaled = X_scaled[:-1]
y = y[:-1]

# Codifica a variável-alvo (3 classes)
y_cat = to_categorical(y, num_classes=3)


#Criação de janelas temporais (sequências)

def create_sequences(X, y, seq_len=10):
    Xs, ys = [], []
    for i in range(len(X) - seq_len):
        Xs.append(X[i:i+seq_len])
        ys.append(y[i+seq_len])
    return np.array(Xs), np.array(ys)

seq_len = 10 #Escolhi 10 dias arbritariamente

X_seq, y_seq = create_sequences(X_scaled, y_cat, seq_len=seq_len)

X_train, X_test, y_train, y_test = train_test_split(X_seq, y_seq, test_size=0.2, shuffle=False)


# Modelo tem Recorrência Local + Global


inp = Input(shape=(seq_len, len(features)))

#Recorrência local (CNN capta padrões curtos)
x_local = Conv1D(filters=64, kernel_size=3, activation='relu', padding='causal')(inp)
x_local = Dropout(0.3)(x_local)

#Recorrência global (LSTM capta padrões longos)
x_global = LSTM(64, return_sequences=False)(inp)

#Combina as duas representações
x = concatenate([x_global, x_local[:, -1, :]])
x = Dense(64, activation='relu')(x)
x = Dropout(0.3)(x)
out = Dense(3, activation='softmax')(x)

model = Model(inputs=inp, outputs=out)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()


#Treinamento
es = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

history = model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=100,
    batch_size=32,
    callbacks=[es],
    verbose=1
)


#Avaliação
loss, acc = model.evaluate(X_test, y_test, verbose=0)
print(f"Acurácia no teste: {acc*100:.2f}%")


#Exemplo de previsão
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)


print("Primeiras previsões:", y_pred_classes[:10])


#Resultado inicial deu [2 2 2 2 2 2 2 2 2 2], ou seja, ele acha que tudo vai subir
#isso se deve ao fato de o modelo estar simples, não há sepração de regime então o viés de crescimento é forte