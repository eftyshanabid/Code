def count_word(headlines,word):
        count = 0
        for headline in headlines:
            if word in headline.split():
                count += 1
        return count


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


if __name__ == "__main__":
    main()
