d = [2, 1, 3, 9, 0, 2, 1, 0, 6]

mx = max(d[0], d[1])
secondmax = min(d[0], d[1])
n = len(d)
for i in range(2, n):
    if d[i] > mx:
        secondmax = mx
        mx = d[i]
    elif d[i] > secondmax and mx != d[i]:
        secondmax = d[i]

print("Second highest number is:", str(secondmax))
