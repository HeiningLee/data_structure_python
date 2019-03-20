"""
    create the list
    [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
"""
index = range(11)
result = []
for i in index[:10]:
    result.append(index[i] * index[i+1])
print(result)


