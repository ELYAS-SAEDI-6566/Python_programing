from solution import get_func
ls = get_func(['square', 'circle', 'rectangle', 'triangle'])

print(ls[0](1))      # 1
print(ls[1](2))      # 12.566370614359172
print(ls[2](2, 4))   # 8
print(ls[3](4, 5))   # 10.0 5663706143588