def palindrome_number():
    n = 101
    temp = n
    y =0
    while (n):
        x = n % 10
        y = y * 10 + x
        n = n // 10
    if y == temp:
        print("palindrome")
    else:
        print("sorry this not a palindrome")

palindrome_number()