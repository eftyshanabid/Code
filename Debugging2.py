def analyze_performance(scores):

    stats = {
        "total_goals": 0,
        "high_scoring_matches": 0,
        "goalless_matches": 0,
        "best_match": 0
    }

    for index, score in enumerate(scores, start=1):

        stats["total_goals"] += score

        if score >= 3:
            stats["high_scoring_matches"] += 1

        elif score == 0:
            stats["goalless_matches"] += 1

        if score > stats["best_match"]:
            stats["best_match"] = index

    return stats


def main():

    scores = [2, 0, 4, 1, 3, 0, 5, 2, 1, 4]

    result = analyze_performance(scores)

    print(result)


if __name__ == "__main__":
    main()