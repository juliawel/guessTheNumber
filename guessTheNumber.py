import random
import math

try_again = True

while try_again == True:
    if try_again == True:
        
        while True:
            try:
                #get the lowest number to choose
                lower = int(input("Enter the lower bound: "))
                #get the maximum number to choose
                upper = int(input("Enter the upper bound: "))
                
                break
            except ValueError:
                print("That wasn't a valid number, try again.")

        #generate a random number between the lower and the upper
        x = random.randint(lower, upper)

        #calculate how many chances
        chances = round(math.log(upper-lower + 1, 2))

        print(f"""
            You have 
                {chances}
            changes to guess the number!
            """)

        #initialize the number of guesses
        count = 0

        #catch an exeption
        while True:
            try:
                while count < round(math.log(upper-lower + 1, 2)):
                    count = count + 1
                    
                    guess = int(input("Guess a number: "))
                    
                    #See if the number is out of range
                    if guess >= lower and guess <= upper:
                        #Give hints on what to guess next based if the number is higher or lower than expected
                        if x == guess:
                            print(f"Congrats! You did it in {count} try\n")
                            break
                        elif x < guess:
                            print("Hmm.. It seems like you guessed too high\n")
                        elif x > guess:
                            print("Hmm.. It seems like you guessed too low\n")
                        
                        #If guesses aren't right at the end, it gives the right number
                        if count >= chances:
                            print(f"\nThe right number is {x}, better luck next time!\n")
                    else:
                        print("Number out of range.\n")
                    
                choice = input("You want to try again? (Yes or No):\n ")
                
                #The program runs again based on the given answer for the question above        
                if choice == "Yes" or choice == "YES" or choice == "yes":
                        try_again = True
                elif choice == "No" or choice == "NO" or choice == "no":
                        try_again = False
                        break 
            #Catch an exeption       
            except ValueError: 
                print("That wasn't a valid number...")
                #count = count - 1
                chances = chances + 1
                print("You were given one more chance...\n")

#End of the game
print("\nThanks for playing!\n")
            
        

