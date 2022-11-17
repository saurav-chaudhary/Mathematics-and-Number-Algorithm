def trailing_zeros():
    res = 0
    n = 100
    # for i in range(5,n,5):
    #     print(i)
    #
    #     res = res +  n//i
    #     n = n//i
    #     print("res",res)
    # print(res)
    i = 5

    while (n):

        res = res + n // i
        n = n//i
        i *= 5
    print(res)
trailing_zeros()