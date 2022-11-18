# This algorithm help us to gcd or can say hcf bewteen two number

def hcf(a,b):
    if b == 0:
        return a
    return hcf(b,a%b)

gcd = hcf(81,15)
print(gcd)