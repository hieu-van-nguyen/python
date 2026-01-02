def pow(x, y):
    res, power = 1.0, y
    if power < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            res *= x
        x, power = x * x, power >> 1
    return res

print(pow(2, 0)) # 1
print(pow(2, 2)) # 4
print(pow(2, -2)) # .25 