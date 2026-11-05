def main():
    scores = [2, 0, 4, 1, 3]

    highest_score = -1
    best_match = 0

    for index, score in enumerate(scores, start=1):

        if score > highest_score:
            highest_score = score
            best_match = index

    print(best_match)


if __name__ == "__main__":
    main()