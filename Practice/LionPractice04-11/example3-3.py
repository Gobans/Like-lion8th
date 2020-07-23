num = []
while(True):
    num.append(int(input()))
    if num[-1] == 0:
        num.sort(reverse=True)
        print('두번째로 큰 값은:',num[1])
        break