import random

fourwords = ['four', 'five', 'carl', 'able', 'acid','aged','also','area','army','away',
    'baby','back','ball','band','bank','base','bath','bear','beat','been','beer',
    'bell','belt','best','bill','bird','blow','blue','boat','body','bomb','bond',
    'bone','book','boom','born','boss','both','bowl','bulk','burn','bush','busy',
    'call','calm','came','camp','card','care','case','cash','cast','cell','chat',
    'chip','city','club','coal','coat','code','cold','come','cook','cool','cope',
]
    #https://www.thefreedictionary.com/4-letter-words.htm - Copy

word = random.choice(fourwords)

user_guess = '....'
guess_count = 10

for i in range(11):
    print(f'You have {guess_count} guesses remaining.')
    
    if user_guess != word and guess_count == 0:
        print("You Lose!")
        break
        
    elif user_guess != word:
        
        #check if the letters match up in each word
        for i in range(0,len(word)):
            if user_guess[i] == word[i]:
                print('1')
            else:
                print('0')
        
        user_guess = input("Please type in your guess here: ")
        guess_count += -1
                
    else:
        print("You Win!")
        break
        
