def main():
    scores = [2, 0, 3, 2, 0, 1, 2, 3]

    frequency = {}

    for score in scores:

        if score in frequency:
            frequency[score] += 1

        else:
            frequency[score] = 1

    print(frequency)


if __name__ == "__main__":
    main()