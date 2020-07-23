a = list(map(int,input().split()))
max_num = max(a)
min_num = min(a)
for idx,i in enumerate(a):
    if i == max_num:
        max_num_idx = idx
    elif i == min_num:
        min_num_idx = idx

print('최댓값:',max_num,',위치는:',max_num_idx,"입니다")
print('최솟값:',min_num,',위치는:',min_num_idx,"입니다")