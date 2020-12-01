import collections


def rainaverage(l):
    sum={}
    count={}
    ans=[]
    for i in range(len(l)):
        try:
            sum[l[i][0]]+=l[i][1]
            count[l[i][0]]+=1
        except:
            sum[l[i][0]]=l[i][1]
            count[l[i][0]]=1
    sum=collections.OrderedDict(sorted(sum.items()))
    count=collections.OrderedDict(sorted(count.items()))
    for k,v in sum.items():

        sum[k]=sum[k]/count[k]
        ans.append((k,sum[k]))

    return ans


def flatten(a):
    i=0
    while i<len(a):

        if(type(a[i]) == type([])):

            a[i]=flatten(a[i])
            length=len(a[i])
            for j in range(len(a[i])):
                a.insert(i,a[i][j])
                i+=1
            del(a[i])
            i-=length
        elif(type(a[i])==type(()) or type(a[i])==type(set([]))):

            a[i]=list(a[i])

            a[i]=tuple(flatten(a[i]))



        i+=1

    return a
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "rainaverage":
  arg = parse(farg)
  print(rainaverage(arg))

if fname == "flatten":
  arg = parse(farg)
  print(flatten(arg))
