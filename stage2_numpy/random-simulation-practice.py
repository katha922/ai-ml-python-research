import numpy as np

np.random.seed(0)

X = np.random.normal(10, 3, (50, 2))
noise = np.random.normal(0, 1, 50)

y = X[:, 0] * 1.5 + noise

print("Feature shape:", X.shape)
print("Target mean:", np.mean(y))
print("Target std:", np.std(y))
