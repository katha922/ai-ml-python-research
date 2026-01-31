import numpy as np

print(np.random.rand(5))
print(np.random.rand(3,5))

#without seed
x=np.random.rand(3)
y=np.random.rand(3)
print(x)
print(y)
#with seed
a=np.random.seed(1)
b=np.random.rand(3)
print(a)
print(b)

c=np.random.seed(1)
d=np.random.rand(3)
print(c)
print(d)
#uniform distribution(equal change)
print("equal change")
print(np.random.uniform(0, 100, size=10))
#normal distribution
print(np.random.normal(loc=0, scale=1, size=1000)) #mean=0,std=1,bell curve data
#synthetic data creation
print("synthetic data")
X = np.random.normal(50, 10, (100, 3)) #100 sample,3 features, 50 mean, 10 std
print(X)

#Target variable
Y = X[:, 0] * 2 + 5
print(Y)
#noise add
noise = np.random.normal(0, 2, size=100)
y_noisy = Y + noise
print(y_noisy)
