
def main():
    max = 2000000
    numbers = set(range(3, max + 1, 2))

    for number in range(3, int(max ** 0.5) + 1):
        if number not in numbers:
            continue

        num = number
        while num < max:
            num += number
            if num in numbers:
                numbers.remove(num)

    print(2 + sum(numbers))
if __name__ == '__main__':
    main()