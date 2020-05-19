x = int(input('Number 1:'))
y = int(input('Number 2:'))
start = 0
if x < y:
    start = y
else:
    start = x

for i in range(start, x * y + 1):
    if i % x == 0 and i % y == 0:
        print(i)
        exit()
