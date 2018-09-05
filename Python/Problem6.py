def main():
    sumOfSquares = 0
    SquareOfSum = 0
    for i in range(1, 101):
        sumOfSquares += i**2
        SquareOfSum += i

    SquareOfSum = SquareOfSum**2
    print(SquareOfSum - sumOfSquares)
if __name__ == '__main__':
    main()
