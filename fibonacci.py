nterms = int(input("enter howmany terms: "))
n1, n2 = 0 , 1
count = 0
if nterms <= 0:
    print("enter positive number")
elif nterms==1:
    print("fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("the fibonacci sequence is:  ")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
