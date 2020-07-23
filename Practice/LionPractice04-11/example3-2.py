N = int(input())
star = '*'
for i in range(N):
    print(star.rjust(N))
    star+= '*'
