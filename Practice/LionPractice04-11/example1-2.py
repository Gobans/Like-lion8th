a,b,c = map(int,input('첫번째 [시,분,초]를 입력해주세요').split())
d,e,f = map(int,input('첫번째 [시,분,초]를 입력해주세요').split())
a = abs(a-d)*3600
b = abs(b-e)*60
c = abs(c-f)
print('두 시각의 차이는',a+b+c,'초 입니다')