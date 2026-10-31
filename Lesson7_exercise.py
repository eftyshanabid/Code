def counting_scores(scores):
        frequency = {}
        for score in scores:
            if score in frequency:
                frequency[score] += 1
            else:
                frequency[score] = 1
        return frequency

def unique_scores(scores):
     u_score = set(scores)
     return u_score

def most_frequent_score(scores):
     frequency = counting_scores(scores)
     most_frequent_score = max(frequency.values())
     return most_frequent_score

def scoreless_match(scores):
     frequency = counting_scores(scores)
     for     

def main():

    scores = [2, 0, 3, 2, 0, 1, 2, 3, 1, 0, 4, 2]

    print(counting_scores(scores))
    print(unique_scores(scores))
    print(most_frequent_score(scores))

main()