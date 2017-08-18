def main():
    answer = 0
    current = 2
    previous = 1
    while current < 4000000:
            if current % 2 == 0:
                    answer = answer + current
            temp = current
            current = current + previous
            previous = temp
    print(answer)
if __name__ == '__main__':
    main()
