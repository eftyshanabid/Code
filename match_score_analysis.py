def main():
    scores = [2, 0, 3, 1, 0, 4, 2, 1, 0, 3]
    total_goals = 0
    matches = []
    highest_num_of_goals = scores[0]
    count = 0  
    total_matches = 0 

    for score in scores:
        total_goals = total_goals + score
        if score == 0:
            count = count + 1
        if highest_num_of_goals < score:
            highest_num_of_goals = score

    total_matches = len(scores)
    avg_score = total_goals/total_matches

    print(f"total {total_goals} scored accross all the matches")      
    print(f"Team failed to score in total {count} matches")
    print(f"Highest {highest_num_of_goals} goals scored in a single match")
    print(f"Average {avg_score} goals scored")

    for index,score in enumerate(scores,start=1):
        if score >= 3 :
            matches.append(index)

    print(f"Matches where team scored atleast three goals : {matches}")

main()
        
