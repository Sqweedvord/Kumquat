from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(17, 2)
result2 = fake_divide(99, 0)
result3 = true_divide(56, 8)
result4 = true_divide(25, 0)

print(result1)
print(result2)
print(result3)
print(result4)