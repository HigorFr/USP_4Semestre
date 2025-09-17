import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from ucimlrepo import fetch_ucirepo 


from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

#dataset
heart_disease = fetch_ucirepo(id=45)

#separar o que eu quero descobrir
X = heart_disease.data.features.values
y = heart_disease.data.targets.values

#Normalizar
scaler = StandardScaler()
X = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_cost(X, y, w, lambda1, lambda2):
    m = len(y)
    h = sigmoid(X.dot(w))
    cost = (-1/m) * (y.dot(np.log(h)) + (1 - y).dot(np.log(1 - h))) + lambda1 * np.sum(np.abs(w)) + lambda2 * np.sum(w**2)
    return cost

def compute_gradient(X, y, w, lambda1, lambda2):
    m = len(y)
    h = sigmoid(X.dot(w))
    gradient = (1/m) * X.T.dot(h - y) + lambda1 * np.sign(w) + 2 * lambda2 * w
    return gradient

def gradient_descent(X, y, w_init, lambda1, lambda2, learning_rate=0.01, epochs=1000):
    w = w_init
    cost_history = []
    for epoch in range(epochs):
        gradient = compute_gradient(X, y, w, lambda1, lambda2)
        w -= learning_rate * gradient
        cost = compute_cost(X, y, w, lambda1, lambda2)
        cost_history.append(cost)
        if epoch % 100 == 0:
            print(f'Época {epoch}: Custo = {cost}')
    return w, cost_history

# Inicializar pesos
w_init = np.zeros(X_train.shape[1])

# Definir parâmetros de regularização
lambda1 = 0.1  # Regularização L1
lambda2 = 0.1  # Regularização L2

# Treinar o modelo
w_opt, cost_history = gradient_descent(X_train, y_train, w_init, lambda1, lambda2, learning_rate=0.01, epochs=1000)


def predict(X, w):
    return (sigmoid(X.dot(w)) >= 0.5).astype(int)

# Fazer previsões
y_pred = predict(X_test, w_opt)

# Calcular acurácia
accuracy = np.mean(y_pred == y_test)
print(f'Acurácia no conjunto de teste: {accuracy * 100:.2f}%')

import matplotlib.pyplot as plt

plt.plot(cost_history)
plt.xlabel('Épocas')
plt.ylabel('Custo')
plt.title('Histórico de Custo durante o Treinamento')
plt.show()

