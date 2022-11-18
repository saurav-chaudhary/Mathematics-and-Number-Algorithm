# This Algorith help us to find Prime Number in a give n range

def sieve_of_eratostenes():
    n = 12
    prime_no = [True for i in range(n+1)]

    x = 2
    while(x*x<=n):
        if prime_no[x] == True:
            for i in range(x*x,n+1,x):
                prime_no[i] = False


        x+=1
    for p in range(2,n+1):
        if prime_no[p]:
            print(p)

sieve_of_eratostenes()