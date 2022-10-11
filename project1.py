import random
def shuffleWord(wrd):
    pw=random.sample(wrd,k=len(wrd))
    return ''.join(pw)
def printPuzzleQuestion(word,score):
    problemWord=shuffleWord(word)
    print("\n Arrange the letters from a valid word : ")
    print(problemWord)
    userWord=input()
    print()
    if userWord.upper()==word:
        print("Correct")
        score+=1
    else:
        print("Wrong")
        score-=1
    return score


def main():
    score=0
    words=['FATHER','BREAK','COUNTRY']
    words=random.sample(words,k=len(words))
    
    for word in words:
        score=printPuzzleQuestion(word,score)
        
    print("your Score is",score)
    print()
main()