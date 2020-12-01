lib = []

while True:

    s = input()

    lib.append(s)

    if s == "EndOfInput":

        break

sibcopy=lib[:]

booklist=[]

borrowerlist=[]

checkoutlist=[]

booi=sibcopy.index("Books")

bori=sibcopy.index("Borrowers")

chki=sibcopy.index("Checkouts")

eoii=sibcopy.index("EndOfInput")

for x in range(booi+1,bori):

    booklist.append(sibcopy[x])

for x in range(bori+1,chki):

    borrowerlist.append(sibcopy[x])

for x in range(chki+1,eoii):

    checkoutlist.append(sibcopy[x])

bookd={}

borrwerd={}

checkd1={}

for x in booklist:

    l=x.split("~")

    bookd[l[0]]=l[1]

for x in borrowerlist:

    l=x.split("~")

    borrwerd[l[0]]=l[1]

for x in checkoutlist:

    l=x.split("~")

    checkd1[l[1]]=[l[0],l[2]]

checkoutlistl=[]

for x in checkoutlist:

    l=x.split("~")

    l.reverse()

    checkoutlistl.append(l)

checkoutlistl.sort()

finallist=[]

for x in checkoutlistl:

    lis=[]

    lis.append(x[0])

    lis.append(borrwerd[x[2]])

    lis.append(x[1])

    lis.append(bookd[x[1]])

    finallist.append(lis)

finallist.sort()

for x in finallist:

    print(x[0]+"~"+x[1]+"~"+x[2]+"~"+x[3])