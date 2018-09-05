def main():
    divider = 20
    i = 20
    while True:
        if i % divider == 0:
            divider -= 1
            if divider == 0:
                break
        else:
            divider = 20
            i += 1
    print(i)
if __name__ == '__main__':
    main()
