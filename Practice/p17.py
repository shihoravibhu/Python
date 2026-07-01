T = (10, 20, 30, 40, 50)
k = 2

# tp = []

# for i in range(k+1,len(T)):    
#     tp.append(T[i])
    
# for i in range(k+1):
#     tp.append(T[i])

# print(tuple(tp))

# or

T = T[k+1:] + T[ : k+1]
print(T)