# d1 = {}
# k = input()
# v = input()
# d1[k] = v
# k = input()
# v = input()
# d1[k] = v
# print(d1)

# dct1 = {}
# for _ in range(2):
#     k, v = input().split()
#     dct1[k] = v
# print(dct1)

hash = {}
for _ in range(3):
    key, value = input().split()
    hash[int(key)] = value
#hash=dict.fromkeys(key, value)
print(hash)
