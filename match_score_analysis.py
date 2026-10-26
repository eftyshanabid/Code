def main():
    scores = [2, 0, 3, 1, 0, 4, 2, 1, 0, 3]
    total_goals = 0

    for score in scores:
        total_goals = total_goals + score

    print(f"total {total_goals} scored accross all the matches")

    for score in scores:
        if score == 0:
            count = count + 1

    print(f"Team failed to score in total {count} matches")

    

