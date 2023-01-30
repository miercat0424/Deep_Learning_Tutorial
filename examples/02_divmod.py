d = lambda x,y  : divmod(x,y)

d(2,4)
d(3,10)
d(10,3)

ar = [i for i in range(10)]

print(ar[d(10,3)])
print("*"*100)
print(ar)