def isPalindrome(n):
    strN = str(n)
    return strN == strN[::-1]

def main():
    for i in range(1000, 100):
        for j in range(1000, 100):
            if isPalindrome(i * j):
                print(i * j)
if __name__ == '__main__':
    main()
