def isPalindrome(n):
    strN = str(n)
    return strN == strN[::-1]

def main():
    max = 0
    for i in range(100, 1000):
        for j in range(100, i+1):
            n = i * j
            if isPalindrome(n) and n > max:
                max = n
    print(max)
if __name__ == '__main__':
    main()
