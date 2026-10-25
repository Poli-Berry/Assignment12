import numpy

income = numpy.arange(100, 400, 10).reshape(3, 10)
print("Original income:")
print(income)

net_income = income * STANDARD_TAX_RATE
print("Net income:")
print(net_income)

new_income = net_income.copy()
new_income[:, 4:7] = income[:, 4:7] * REDUCED_TAX_RATE
print("Updated net income:")
print(new_income)

print("Second quarter:")
print(new_income[:, 3:6])
