import math
import copy
def progression(arr):
    a=True
    for i in range(len(arr)-2):
        if(arr[i+1]-arr[i]!=arr[i+2]-arr[i+1]):
            return False
    return True
primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
last=199
def isprime(n):
    if(n>last):
        flag=0
        for i in range(199,math.ceil(math.sqrt(n))+1,2):
            if(n%i==0):
                flag+=1
                return False
        if(flag==0):
            return True
    elif(n in primes):
        return True

def primesquare(arr):
    if((math.sqrt(arr[0])).is_integer()):
        for i in range(1,len(arr)):
            if(i%2!=0):
                if(not isprime(arr[i])):
                    return False
            elif(i%2==0):
                if(not (math.sqrt(arr[i])).is_integer()):
                    return False
        return True

    else:
        for i in range(0,len(arr)):
            if(i%2==0):
                if(not isprime(arr[i])):
                    return False
            elif(i%2!=0):
                if(not (math.sqrt(arr[i])).is_integer()):
                    return False
        return True
        
        
def matrixflip(m,d):
    arr=copy.deepcopy(m)
    if(d=="h"):
        for i in range(len(arr)):
            arr[i].reverse()
        return (arr)
    elif(d=="v"):
        for i in range(int(len(m)/2)):
            temp=arr[0]
            arr[0]=arr[len(m)-1-i]
            arr[len(m)-1-i]=temp
        return (arr)
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "progression":
  arg = parse(farg)
  print(progression(arg))

if fname == "primesquare":
  arg = parse(farg)
  print(primesquare(arg))

if fname == "matrixflip":
  (arg1,arg2) = parse(farg)
  savearg1 = []
  for row in arg1:
    savearg1.append(row[:])
  ans = matrixflip(arg1,arg2)
  if savearg1 == arg1:
    print(ans)
  else:
    print("Side effect")

