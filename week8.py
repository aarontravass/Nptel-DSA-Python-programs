from sys import stdin,stdout

def pal(s1,s2, l1, l2):
    len=0
    arr=[[0 for i in range(l1+3)] for j in range(l2+3)]
    row=col=0
    for i in range(l1+1):
        for j in range(l2+1):
            if(i==0 or j==0):
                arr[i][j]=0
            elif(s1[i-1]==s2[j-1]):
                arr[i][j]=arr[i-1][j-1]+1
                if(len<arr[i][j]):
                    len=arr[i][j]
                    col=j
                    row=i
            else:
                arr[i][j]=0
    ans=[]
    while(arr[row][col]!=0):
        ans.append(s1[row-1])
        row-=1
        col-=1

    return ans[::-1]

L=int(stdin.readline())
S=stdin.readline()
S1=list(S)
if(S1[-1]=="\n"):
    S1.pop()
S2=S1[::-1]
S=pal(S1,S2,len(S1),len(S2))
stdout.write(str(len(S))+"\n"+"".join(S))