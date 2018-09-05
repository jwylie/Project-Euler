def isPrime(n):
    for i in range(2, n):
       if n % i == 0:
         return False
    return True

def main():
    p = 2
    i = 0
    while True:
        if isPrime(p):
            i += 1
            if i == 10001:
                print(p)
                break
        p += 1
if __name__ == '__main__':
    main()