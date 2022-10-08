s=[[4,8,2], [4,5,7], [6,1,6]] 
l=[i for i in range(1,10)]
ss=[s[i][j] for i in range(len(s)) for j in range(len(s))]
for i in set(ss):
    l.remove(i)
n=3
summ=n*(n**2+1)/2
cols = [(summ-sum(i)) for i in zip(*s)] 
rows = [(summ-sum(i)) for i in s]
diagonal = (summ-sum([s[i][j] for i in range(len(s)) for j in range(len(s)) if i==j]))
diagonal1 = (summ-sum([s[i][len(s)-1-i] for i in range(len(s))]))
t=sum(rows)+sum(cols)+diagonal


l=[i for i in range(1,10)]
ss=[s[i][j] for i in range(len(s)) for j in range(len(s))]
ll=[]
lll=[]
for i in (ss):
    if i not in ll:
        l.remove(i)
    else:
        lll.append(i)
    ll.append(i)
print(sum(lll)-sum(l))
