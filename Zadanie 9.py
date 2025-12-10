values = [75, 50, 100, 62.5]
min = 50
max = 100
normalize = [(value - min) / (max - min) for value in values]
checks = ["OK" if 0 <= n <= 1 else "OUT" for n in normalize]
print(checks)
print("wartość oryginalna | wartość znormalizowana")
for original, norm in zip (values, normalize):
    print(f"{original:<18} | {norm:<20}")