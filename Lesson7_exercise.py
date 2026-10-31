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
     m_frequent_score = max(frequency.values())
     return m_frequent_score

def scoreless_match(scores):
     frequency = counting_scores(scores)
     for score,count in frequency.items():
          if(score) == 0:
               return count

def handle_ties(scores):
     frequency = counting_scores(scores)
     most_frequent_score = max(frequency.values())
     highest = {}
     for score,count in frequency.items():
          if count == most_frequent_score:
               highest[score] = count
     return highest

def main():

    scores = [2, 0, 3, 2, 0, 1, 2, 3, 1, 0, 4, 2]

    print(counting_scores(scores))
    print(unique_scores(scores))
    print(most_frequent_score(scores))
    print(scoreless_match(scores))
    print(handle_ties(scores))

main()