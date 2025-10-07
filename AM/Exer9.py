# 1) Deduzir a expressão para hessiana do modelo de regressão logística multinominal. 

# 2) Implementar o algoritmo gradiente e newton para regressão logística multinominal

# 3) Utilizar o conjunto de dados iris 


'''
1) Dedução

Modelo:
  z_{ik} = x_i^T w_k
  p_{ik} = P(y=k | x_i) = exp(z_{ik}) / Σ_{j=1}^K exp(z_{ij})

Função objetivo (negativa da log-verossimilhança, média por amostra):
  L(W) = - (1/m) Σ_{i=1}^m Σ_{k=1}^K y_{ik} log p_{ik}

Derivação do gradiente (passo a passo):
1) Derivada parcial de log p_{ik} em relação às ativações z_{ij}:
     ∂ log p_{ik} / ∂ z_{ij} = δ_{kj} - p_{ij}
   (δ é delta de Kronecker: 1 se k=j, senão 0)

2) Pela cadeia, derivada de log p_{ik} em relação a w_r:
     ∂ log p_{ik} / ∂ w_r = Σ_j (∂ log p_{ik} / ∂ z_{ij}) (∂ z_{ij} / ∂ w_r)
   como ∂ z_{ij} / ∂ w_r = x_i * δ_{jr}, obtemos
     ∂ log p_{ik} / ∂ w_r = (δ_{kr} - p_{ir}) x_i

3) Agora derivamos L em relação a w_r:
     ∂L/∂w_r = - (1/m) Σ_i Σ_k y_{ik} (δ_{kr} - p_{ir}) x_i
            = (1/m) Σ_i (p_{ir} - y_{ir}) x_i

4) Forma matricial (vetorizada):
     P = softmax(X @ W)  (m×K), Y (m×K)
     ∇_W L = X^T (P - Y) / m   (d×K)

Segunda derivada (Hessiana) — bloco por bloco:
1) Gradient component para a classe r: g_r = (1/m) Σ_i (p_{ir} - y_{ir}) x_i
2) Derivar g_r em relação a w_s:
     ∂ p_{ir} / ∂ z_{is} = p_{ir} (δ_{rs} - p_{is})
     ∂ p_{ir} / ∂ w_s = p_{ir} (δ_{rs} - p_{is}) x_i
   Logo o bloco (d×d) H_{rs} é
     H_{rs} = ∂^2 L / ∂ w_s ∂ w_r^T = (1/m) Σ_i p_{ir} (δ_{rs} - p_{is}) x_i x_i^T

3) Forma compacta usando Kronecker:
     Defina S_i = diag(p_i) - p_i p_i^T   (K×K)
     Então a Hessiana total (dK × dK) vale
       H = (1/m) Σ_{i=1}^m ( S_i ⊗ (x_i x_i^T) )
   (cada bloco H_{rs} corresponde ao bloco (r,s) dessa soma)

Regularização L2 (opcional):
  Se J_reg = L + (λ/2) Σ_k ||w_k||^2 então
    ∇_W J_reg = ∇_W L + λ W
    H_reg = H + λ I_{dK}

Newton-Raphson (vetorizado):
  - Empilhe W em w_vec ∈ R^{dK}
  - Calcule g_vec = vec(∇_W L) e H (dK×dK)
  - Resolva H Δ = g_vec e atualize w_vec ← w_vec - Δ
  (na prática evita-se inversão explícita; resolve-se o sistema linear)

Observações práticas:
  - Construir H explicitamente tem custo e memória altos (dimensão dK × dK).
  - Para d ou K grandes use L-BFGS ou métodos que usam produto H·v (CG).
=============================================================================
'''


#2 e 3) as funções implemntadas e já utilizando o iris


import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from ucimlrepo import fetch_ucirepo




# Dataset
iris = fetch_ucirepo(id=53)
X = iris.data.features.values
y = iris.data.targets.values.flatten()

# One-hot encoding
K = len(np.unique(y))
Y = np.eye(K)[y]

# Normalizar
scaler = StandardScaler()
X = scaler.fit_transform(X)
m, n = X.shape

# Adiciona termo de bias
X = np.hstack([np.ones((m,1)), X])

X_train, X_test, Y_train, Y_test, y_train, y_test = train_test_split(X, Y, y, test_size=0.2, random_state=42)

def softmax(Z):
    Z -= np.max(Z, axis=1, keepdims=True)
    return np.exp(Z) / np.sum(np.exp(Z), axis=1, keepdims=True)

def cost(X, Y, W):
    m = X.shape[0]
    P = softmax(X @ W)
    return -np.sum(Y * np.log(P + 1e-9)) / m

def grad(X, Y, W):
    m = X.shape[0]
    P = softmax(X @ W)
    return X.T @ (P - Y) / m

def hessian(X, Y, W):
    m, n = X.shape
    P = softmax(X @ W)
    H = np.zeros((n * K, n * K))
    for i in range(m):
        p = P[i].reshape(-1,1)
        R = np.diagflat(p) - p @ p.T
        xi = X[i].reshape(-1,1)
        H += np.kron(R, xi @ xi.T)
    return H / m

def gradient_descent(X, Y, W, lr=0.1, epochs=300):
    for _ in range(epochs):
        W -= lr * grad(X, Y, W)
    return W

def newton_method(X, Y, W, epochs=10):
    for _ in range(epochs):
        g = grad(X, Y, W)
        H = hessian(X, Y, W)
        W -= np.linalg.solve(H, g.flatten()).reshape(W.shape)
    return W

# Inicialização
W = np.zeros((X.shape[1], K))

# Gradiente
W_gd = gradient_descent(X_train, Y_train, W.copy(), lr=0.1, epochs=500)

# Newton
W_newton = newton_method(X_train, Y_train, W.copy(), epochs=8)

def predict(X, W):
    return np.argmax(softmax(X @ W), axis=1)

from sklearn.metrics import accuracy_score

print("Gradiente:", accuracy_score(y_test, predict(X_test, W_gd)))
print("Newton:", accuracy_score(y_test, predict(X_test, W_newton)))



