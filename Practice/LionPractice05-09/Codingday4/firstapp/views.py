from django.shortcuts import render
import random

def home(request):
    Lion8 = ['명환','민지','채원','재훈','지은','진우','희찬','지윤','바다','인아','민정','예빈','은아','지원','주희']
    TeamMatch = []

    while(Lion8 != []):
        temp = []
        cnt = 0 
        while(True):
            pie = len(Lion8)
            if cnt == 3:
                break
            a = random.randint(0,pie-1)
            if Lion8[a] not in temp:
                temp.append(Lion8[a])
                Lion8.pop(a)
                cnt+=1
        TeamMatch.append(temp)
    Team1 = ('-'.join(TeamMatch[0]))
    Team2 = ('-'.join(TeamMatch[1]))
    Team3 = ('-'.join(TeamMatch[2]))
    Team4 = ('-'.join(TeamMatch[3]))
    Team5 = ('-'.join(TeamMatch[4]))
    return render(request, 'home.html' , {"Team1":Team1,"Team2":Team2,"Team3":Team3,"Team4":Team4,"Team5":Team5})