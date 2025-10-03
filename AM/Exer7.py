#Feito com ajuda do Github Copilot


import numpy as np
from sklearn.model_selection import train_test_split



from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from ucimlrepo import fetch_ucirepo


class LogisticRegressionGD:
    def __init__(self, lr=0.1, n_iter=1000):
        self.lr = lr
        self.n_iter = n_iter
    
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def fit(self, X, y):
        X = np.c_[np.ones(X.shape[0]), X]  # adiciona bias
        self.theta = np.zeros(X.shape[1])
        
        for _ in range(self.n_iter):
            z = X @ self.theta
            h = self.sigmoid(z)
            gradient = X.T @ (h - y) / y.size
            self.theta -= self.lr * gradient
    
    def predict_proba(self, X):
        X = np.c_[np.ones(X.shape[0]), X]
        return self.sigmoid(X @ self.theta)
    
    def predict(self, X):
        return (self.predict_proba(X) >= 0.5).astype(int)






class OneVsAll:
    def __init__(self, lr=0.1, n_iter=1000):
        self.lr = lr
        self.n_iter = n_iter
        self.classifiers = {}
    
    def fit(self, X, y):
        self.classes = np.unique(y)
        for c in self.classes:
            y_binary = (y == c).astype(int)
            clf = LogisticRegressionGD(lr=self.lr, n_iter=self.n_iter)
            clf.fit(X, y_binary)
            self.classifiers[c] = clf
    
    def predict(self, X):
        probs = np.array([clf.predict_proba(X) for clf in self.classifiers.values()])
        return self.classes[np.argmax(probs, axis=0)]


class OneVsOne:
    def __init__(self, lr=0.1, n_iter=1000):
        self.lr = lr
        self.n_iter = n_iter
        self.classifiers = []
        self.pairs = []
    
    def fit(self, X, y):
        self.classes = np.unique(y)
        for i in range(len(self.classes)):
            for j in range(i+1, len(self.classes)):
                c1, c2 = self.classes[i], self.classes[j]
                mask = (y == c1) | (y == c2)
                X_pair, y_pair = X[mask], y[mask]
                y_binary = (y_pair == c1).astype(int)
                clf = LogisticRegressionGD(lr=self.lr, n_iter=self.n_iter)
                clf.fit(X_pair, y_binary)
                self.classifiers.append(clf)
                self.pairs.append((c1, c2))
    
    def predict(self, X):
        votes = np.zeros((X.shape[0], len(self.classes)))
        for clf, (c1, c2) in zip(self.classifiers, self.pairs):
            pred = clf.predict(X)
            for i, p in enumerate(pred):
                if p == 1:
                    votes[i, np.where(self.classes == c1)[0]] += 1
                else:
                    votes[i, np.where(self.classes == c2)[0]] += 1
        return self.classes[np.argmax(votes, axis=1)]



iris = fetch_ucirepo(id=53)
X = iris.data.features.values
y = iris.data.targets.values.ravel()

#normalização
scaler = StandardScaler()
X = scaler.fit_transform(X)

#split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#One-vs-All
ova = OneVsAll(lr=0.1, n_iter=2000)
ova.fit(X_train, y_train)
y_pred_ova = ova.predict(X_test)
print("Acurácia One-vs-All:", accuracy_score(y_test, y_pred_ova))

#One-vs-One
ovo = OneVsOne(lr=0.1, n_iter=2000)
ovo.fit(X_train, y_train)
y_pred_ovo = ovo.predict(X_test)
print("Acurácia One-vs-One:", accuracy_score(y_test, y_pred_ovo))
