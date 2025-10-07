import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import kagglehub

path = kagglehub.dataset_download("uciml/pima-indians-diabetes-database") #dataset de diabetes do pima mostrado na aula
csv_path = f"{path}/diabetes.csv"

data = pd.read_csv(csv_path)

X = data.drop("Outcome", axis=1).values
y = data["Outcome"].values

#normaliza
scaler = StandardScaler()
X = scaler.fit_transform(X)

X = np.hstack([np.ones((X.shape[0], 1)), X]) #fazer a cluna do bias

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


def gradiente(X, y, w, lambda1=0.0, lambda2=0.0):
    m = len(y)
    h = X.dot(w)
    grad = (2/m) * X.T.dot(h - y)
    grad += lambda1 * np.sign(w) + 2 * lambda2 * w
    return grad

def gradiente_descendente(X, y, w_init, lambda1=0.0, lambda2=0.0, lr=0.01, epochs=1000):
    w = w_init.copy()
    for _ in range(epochs):
        grad = gradiente(X, y, w, lambda1, lambda2)
        w -= lr * grad
    return w

def treinar(X, y, lambda1=0.0, lambda2=0.0, lr=0.01, epochs=1000):
    n_features = X.shape[1]
    w_init = np.zeros(n_features)
    w = gradiente_descendente(X, y, w_init, lambda1, lambda2, lr, epochs)
    return w



def predit(X, w):
    y_hat = X.dot(w)
    return (y_hat >= 0.5).astype(int)

def acuracia(y_true, y_pred):
    return np.mean(y_true == y_pred)

#fiz tudo numa função só, e ai só mudar o lamba dependendo do que quer fozer

w_lr = treinar(X_train, y_train, lambda1=0.0, lambda2=0.0)

w_l2 = treinar(X_train, y_train, lambda1=0.0, lambda2=0.5)

w_en = treinar(X_train, y_train, lambda1=0.3, lambda2=0.3)
#valores de lambda colocados aleatoriamente

y_pred_lr = predit(X_test, w_lr)
y_pred_l2 = predit(X_test, w_l2)
y_pred_en = predit(X_test, w_en)

print("------------ACURÁCIAS------------")
print(f"Regressão linear:            {acuracia(y_test, y_pred_lr)*100:.2f}%")
print(f"L2:                          {acuracia(y_test, y_pred_l2)*100:.2f}%")
print(f"Elastic Net:                 {acuracia(y_test, y_pred_en)*100:.2f}%")
