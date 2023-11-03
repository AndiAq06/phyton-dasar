# RANGES

# for n in range(5):
#     print(n)  # 5 tidak masuk

# print('-----')
# for n in range(3, 10):
#     print(n)

# print('-----')
# for n in range(0, 20, 4):
#     print(n)


burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']

for n in range(len(burgers)):
    print(n, burgers[n])

print('---------')
# range(start, end, step)
for n in range(len(burgers) - 1, -1, -1):
    print(n, burgers[n])
