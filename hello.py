'''
Created on 2022/10/14

@author: t20cs015
'''
import random

a=random.randrange(3)
b=random.randrange(3)



if a==0 and b==0:
    print('Aの⼿︓グー v.s. Bの⼿︓グー → 引き分け')
elif a==0 and b==1:
    print('Aの⼿︓グー v.s. Bの⼿︓チョキ → Aの勝ち')
elif a==0 and b==2:
    print('Aの⼿︓グー v.s. Bの⼿︓パー → Bの勝ち')
elif a==1 and b==0:
    print('Aの⼿︓チョキ v.s. Bの⼿︓グー → Bの勝ち')
elif a==1 and b==1:
    print('Aの⼿︓チョキ v.s. Bの⼿︓チョキ → 引き分け')
elif a==1 and b==2:
    print('Aの⼿︓チョキ v.s. Bの⼿︓パー → Aの勝ち')
elif a==2 and b==0:
    print('Aの⼿︓パー v.s. Bの⼿︓グー → Aの勝ち')
elif a==2 and b==1:
    print('Aの⼿︓パー v.s. Bの⼿︓チョキ → Bの勝ち')
elif a==2 and b==2:
    print('Aの⼿︓パー v.s. Bの⼿︓パー → 引き分け')