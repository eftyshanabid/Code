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

    for score in scores:
        highest_num_of_goals = scores[0]
        if highest_num_of_goals > score :
            highest_num_of_goals = score

    print(f"Highest {highest_num_of_goals} goals scored in a single match")

    for score in scores:
        count = count + 1

    print(f"Total {count} matches played")

    
