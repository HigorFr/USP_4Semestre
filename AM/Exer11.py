#Exercicio
#Implementar o perceptron multicamadas para o conjunto de dados iris. Comparar o desempenho usando algoritmo gradiente, gradiente conjugado e método de newton.

#a organização da classe teve ajuda do Copilot do github

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder

#funções pra ajudar

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)


class MLP:
    def __init__(self, n_inputs, n_hidden, n_outputs):
        # pesos iniciais
        self.W1 = np.random.randn(n_inputs, n_hidden) * 0.1
        self.b1 = np.zeros((1, n_hidden))
        self.W2 = np.random.randn(n_hidden, n_outputs) * 0.1
        self.b2 = np.zeros((1, n_outputs))

    def forward(self, X):
        self.Z1 = np.dot(X, self.W1) + self.b1
        self.A1 = sigmoid(self.Z1)
        self.Z2 = np.dot(self.A1, self.W2) + self.b2
        self.A2 = sigmoid(self.Z2)
        return self.A2

    def compute_loss(self, y_true, y_pred):
        #utilizando o eqm
        return np.mean((y_true - y_pred) ** 2)


    def backward(self, X, y, y_pred):
        m = X.shape[0]

        dZ2 = (y_pred - y) * sigmoid_deriv(y_pred)
        dW2 = np.dot(self.A1.T, dZ2) / m
        db2 = np.sum(dZ2, axis=0, keepdims=True) / m

        dZ1 = np.dot(dZ2, self.W2.T) * sigmoid_deriv(self.A1)
        dW1 = np.dot(X.T, dZ1) / m
        db1 = np.sum(dZ1, axis=0, keepdims=True) / m

        grads = (dW1, db1, dW2, db2)
        return grads




    #Os tipos de treinamento

    def treinar_gradiente(self, X, y, lr=0.1, epochs=1000):
        for i in range(epochs):
            y_pred = self.forward(X)
            grads = self.backward(X, y, y_pred)
            dW1, db1, dW2, db2 = grads

            self.W1 -= lr * dW1
            self.b1 -= lr * db1
            self.W2 -= lr * dW2
            self.b2 -= lr * db2

            if i % 200 == 0:
                loss = self.compute_loss(y, y_pred)
                print(f"[Gradiente] Época {i} | Loss = {loss:.4f}")

    def treinar_conjugado(self, X, y, epochs=1000):
        lr = 0.1
        prev_grad = None
        direction_W1, direction_W2 = None, None

        for i in range(epochs):
            y_pred = self.forward(X)
            grads = self.backward(X, y, y_pred)
            dW1, db1, dW2, db2 = grads

            # inicializa direção
            if prev_grad is None:
                direction_W1, direction_W2 = -dW1, -dW2
            else:
                beta = np.sum(dW1 * (dW1 - prev_grad[0])) / (np.sum(prev_grad[0] ** 2) + 1e-8)
                direction_W1 = -dW1 + beta * direction_W1
                direction_W2 = -dW2 + beta * direction_W2

            prev_grad = (dW1, dW2)

            # atualização
            self.W1 += lr * direction_W1
            self.W2 += lr * direction_W2
            self.b1 -= lr * db1
            self.b2 -= lr * db2

            if i % 200 == 0:
                loss = self.compute_loss(y, y_pred)
                print(f"[Conjugado] Época {i} | Loss = {loss:.4f}")

    def treinar_newton(self, X, y, epochs=100):
        lr = 1.0
        for i in range(epochs):
            y_pred = self.forward(X)
            grads = self.backward(X, y, y_pred)
            dW1, db1, dW2, db2 = grads

            # aproximação do Hessiano diagonal (simplificada)
            H_W1 = np.abs(dW1) + 1e-4
            H_W2 = np.abs(dW2) + 1e-4

            # passo de Newton
            self.W1 -= lr * dW1 / H_W1
            self.W2 -= lr * dW2 / H_W2
            self.b1 -= lr * db1
            self.b2 -= lr * db2

            if i % 50 == 0:
                loss = self.compute_loss(y, y_pred)
                print(f"[Newton] Época {i} | Loss = {loss:.4f}")

    def predict(self, X):
        probs = self.forward(X)
        return np.argmax(probs, axis=1)



#dadods pegos pela propria bliblioteca do site
iris = load_iris()
X = iris.data
y = iris.target.reshape(-1, 1)

#Normaliza
scaler = StandardScaler()
X = scaler.fit_transform(X)

#One-hot encode
encoder = OneHotEncoder(sparse_output=False)
y_onehot = encoder.fit_transform(y)

#treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y_onehot, test_size=0.3, random_state=42)





#ajusta entradas e saídas
n_inputs = X_train.shape[1]
n_hidden = 8
n_outputs = y_onehot.shape[1]


#testando gradiente descedente
mlp_grad = MLP(n_inputs, n_hidden, n_outputs)
mlp_grad.treinar_gradiente(X_train, y_train, lr=0.1, epochs=1000)
y_pred_grad = mlp_grad.predict(X_test)
acc_grad = np.mean(np.argmax(y_test, axis=1) == y_pred_grad)
print(f"\nAcurácia (Gradiente Descendente): {acc_grad:.3f}")

#testanto gradiente conjugado
mlp_conj = MLP(n_inputs, n_hidden, n_outputs)
mlp_conj.treinar_conjugado(X_train, y_train, epochs=1000)
y_pred_conj = mlp_conj.predict(X_test)
acc_conj = np.mean(np.argmax(y_test, axis=1) == y_pred_conj)
print(f"Acurácia (Gradiente Conjugado): {acc_conj:.3f}")

#testanto newton
mlp_newton = MLP(n_inputs, n_hidden, n_outputs)
mlp_newton.treinar_newton(X_train, y_train, epochs=200) #200 porquê o computador não estava aguentando muito
y_pred_newton = mlp_newton.predict(X_test)
acc_newton = np.mean(np.argmax(y_test, axis=1) == y_pred_newton)
print(f"Acurácia (Método de Newton): {acc_newton:.3f}")
