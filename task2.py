import numpy

income = numpy.arange(100, 400, 10).reshape(3, 10)
print("Original income:")
print(income)

net_income = income * 0.7
print("Net income:")
print(net_income)

new_income = income * 0.7
new_income[:, 4:7] = income[:, 4:7] * 0.6
print("Updated net income:")
print(new_income)

print("Second quarter:")
print(new_income[:, 3:6])
