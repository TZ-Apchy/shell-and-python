f = lambda i:1 if i <= 1 else f(i-1) * i
print(f(5))
print( type(f))