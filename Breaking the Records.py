n=int(input())
score=list(map(int,input().split()))
best=score[0]
worst=score[0]
best_count=0
worst_count=0
for i in range(1,n):
    if(score[i]>best):
        best=score[i]
        best_count+=1
    elif(score[i]<worst):
        worst=score[i]
        worst_count+=1
print(best_count,worst_count)
