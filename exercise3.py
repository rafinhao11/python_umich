hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Hours:")
r = float(rate)
if h <= 40:
    h = h * r
else:
    h = 40 * r + (h - 40) * r * 1.5
print(h)
