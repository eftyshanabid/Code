def count_word(headlines,word):
        count = 0
        for headline in headlines:
            if word in headline.split():
                count += 1
        return count

def find_longest_character(headlines):
     max_length = len(headlines[0].split()[0])
     for headline in headlines:
          for word in headline:
               if len(word)>max_length:
                    max_length = len(word.len)
                    print(max_length)            
     return max_length         
     

def main():
    
    headlines = [
    "Messi scores twice against Madrid",
    "Ronaldo scores winning goal",
    "Barcelona defeats Real Madrid",
    "Messi provides two assists",
    "Liverpool defeats Barcelona",
    "Ronaldo reaches new milestone"
   ]

    word_count = count_word(headlines,"Messi")
    print(f"Total word count is {word_count}")
    max_length = find_longest_character(headlines)
    print(max_length)


if __name__ == "__main__":
    main()
