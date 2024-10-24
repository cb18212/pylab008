list0 = [1, 2, 3]
list1 = [4, 5]

t = (list0, list1)
print(t)
list1.append(6)
print(t)
d = {t: 'this tuple contains two lists'}