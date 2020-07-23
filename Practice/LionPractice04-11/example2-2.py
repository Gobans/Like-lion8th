from string import ascii_uppercase
alpha_list = list(ascii_uppercase)
Li = input()
answer = 0
for idx,i in enumerate(alpha_list):
    if Li.count(i) != 0 :
        temp = Li.count(i)
        if (idx+1)%3 == 0:
            x= 3
        else:
            x= (idx+1)%3
        num = int(idx/3) + 1
        answer += temp*x*num
print(answer)