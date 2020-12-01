import math


def isprime(n):
    flag = 0
    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if (n % i == 0):
            flag += 1
            return False
    if (flag == 0):
        return True


def primepartition(n):
    if (n > 0):
        if (n % 2 == 0):
            return (True)
        else:
            return (isprime(n - 2))
    else:
        return (False)


def nestingdepth(s):
    arr=[]
    m=-1
    count=0
    if(len(s)==0):
        return 0
    else:
        for i in range(len(s)):
            if(s[i]=="("):
                arr.append(s[i])
                count+=1
            if(len(arr)>0):
                if(s[i]==")" and arr[-1]=="("):
                    arr.pop()
                    count-=1
            m=max(m,count)
        if(s.count(")")>s.count("(")):
            return -1
        else:
            if(len(arr)>0):
                return -1
            else:
                return m


def rotatelist(arr,k):
    n=len(arr)
    new_ar = []

    for i in range(len(arr)):
        new_ar.append(arr[(i + k) % n])
    return new_ar
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "primepartition":
  arg = parse(farg)
  print(primepartition(arg))

if fname == "nestingdepth":
  arg = parse(farg)
  print(nestingdepth(arg))

if fname == "rotatelist":
  (arg1,arg2) = parse(farg)
  print(rotatelist(arg1,arg2))