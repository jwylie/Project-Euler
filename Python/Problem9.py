
def main():
    sum = 1000
    for a in range(sum):
        for b in range(a, sum):
            c = sum - a - b
            if a**2 + b**2 == c**2 and a*b*c != 0:
                print(a * b * c)
if __name__ == '__main__':
    main()