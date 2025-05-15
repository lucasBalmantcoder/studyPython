import math

value_x = list(map(float, input().split()))
value_y = list(map(float, input().split()))

distance = math.sqrt((value_x[0] - value_y[0])**2 + (value_x[1] - value_y[1])**2)

print(f'{distance:.4f}')

