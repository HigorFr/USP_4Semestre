#Feito com ajuda do Github Copilot

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class Perceptron:
    def __init__(self, n_inputs, taxa_aprendizado=0.01, n_epocas=1000):
        self.taxa = taxa_aprendizado
        self.n_epocas = n_epocas
        # pesos iniciais (inclui bias como w0)
        self.pesos = np.random.uniform(-0.5, 0.5, n_inputs + 1)

    def ativacao(self, x):
        return np.where(x >= 0, 1, 0)  # função degrau

    def prever(self, X):
        X_bias = np.c_[np.ones((X.shape[0], 1)), X]  # adiciona bias
        return self.ativacao(np.dot(X_bias, self.pesos))

    def treinar(self, X, y):
        X_bias = np.c_[np.ones((X.shape[0], 1)), X]  # adiciona bias
        for _ in range(self.n_epocas):
            for xi, target in zip(X_bias, y):
                saida = self.ativacao(np.dot(xi, self.pesos))
                erro = target - saida
                # Regra delta
                self.pesos += self.taxa * erro * xi

# === Teste com Iris ===
iris = load_iris()
X = iris.data[:, :2]  # usar só 2 features (sepal length e sepal width)
y = (iris.target == 0).astype(int)  # binário: 1 = setosa, 0 = não-setosa

# Normalização
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinar perceptron
p = Perceptron(n_inputs=2, taxa_aprendizado=0.1, n_epocas=50)
p.treinar(X_train, y_train)

# Avaliar
y_pred = p.prever(X_test)
acuracia = np.mean(y_pred == y_test)

print("Pesos finais:", p.pesos)
print("Acurácia no teste:", acuracia)

