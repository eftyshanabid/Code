def main():

    scores = [2, 0, 3, 1, 0, 4, 2, 1, 0, 3]

    def calculate_total(scores):
        total_score = 0
        for score in scores:
            total_score = total_score + score
        return total_score

    # def count_scoreless_match(scores):
    #     count = 0
    #     for score in (scores):
    #         if score == 0:
    #             count = count + 1
    #     return count

    # def find_highest_score(scores):
    #     highest_score = scores[0]
    #     for score in scores:
    #         if score > highest_score:
    #             highest_score = score
    #     return highest_score

    # def cacalculate_average(scores):
    #     total_score = calculate_total(scores)
    #     total_matches = len(scores)
    #     avg_score = total_score/total_matches
    #     return avg_score

    # print(f"Total score is: {calculate_total(scores)}")
    # print(f"Total scoreless matches: {count_scoreless_match(scores)}")
    # print(f"Highest score in a single match is : {find_highest_score(scores)}")
    # print(f"Average score is {cacalculate_average(scores)}")


main()



