f = [lambda x=1:x*2,lambda x:x**2]
print(f[1](f[0](3)))
