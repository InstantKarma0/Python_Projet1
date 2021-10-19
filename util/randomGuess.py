from randomGen import randomInt

def randomGuesser(supp=10):
    """Do a random and make the user guess the randomised number
    
    Optional Keyword Arguments:\n
    supp -- the upper end point of the randomised number"""
    
    # Generate a randomised Integer beetween 0 and supp
    target = randomInt(supp)
    guess = int()

    while (guess != target):

        #Ask the user to insert a number in the console
        print("Entrez un nombre compris entre 0 et {}".format(supp))
        guess = int(input())

        # Case when the number guessed by the user is equal to the randomised number
        if guess == target:
            print("Vous avez trouver le nombre mystère!")

        # Case when the number guessed by the user is lower than to the randomised number 
        elif guess < target:
            print("Le nombre entré est inférieur au nombre mystère.")
            
        # Case when the number guessed by the user is greater than to the randomised number 
        elif guess > target:
            print("Le nombre entré est supérieur au nombre mystère")
        # EO if/elif/elif
        

    # print End of Program
    print("Fin du programme")

    # EO randomGuesseur



# For test purpose
if __name__ == "__main__":
    randomGuesseur()