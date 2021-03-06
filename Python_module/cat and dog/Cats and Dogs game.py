'''
                            Cats and Dogs game
===============================================================================
Create a program that will play the “cats and dogs” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they have a “cat”.
 For every digit the user guessed Incorrectly is a “dog.” Every time the user makes a guess, 
 tell them how many “cats” and “dogs” they have. Once the user guesses the correct number
 (until he/she gets 4 cats) the game is over.

E.g. Say the number generated by the computer is 1038. An example interaction could look like this:

Welcome to the cats and dogs Game!
Enter a number:
>>> 1234
2 cats, 2 dogs
>>> 1256
1 cat, 3 dog
>>> 1238
3 cat, 1 dog

...
Until the user guesses the number.
User should have the option to exit the game like Enter 'Exit' to end the game
'''
# User
def user():
    print("-*-*-*-*-*-*-*-*-*-Welcome to Dog And Cat Game-*-*-*-*-*-*-*-*-*-*-")
    user_num = int(input("Enter any 4 digit number : "))
    user_num = str(user_num)
    l = len(user_num)
    if l<4 or l>4:
        print("Entered number is not a four digit number, Try Again ")
        user()
    else:
        print("User Selected : ", user_num)
    return user_num

# Computer
def computer():
    import random
    comp_num = random.randint(1000,9999)
    comp_num = str(comp_num)
    print("computer selected : ",comp_num)
    return comp_num

w  =  False
while not w:
    user_num = user()
    comp_num = computer()

    k = 0
    cats = 0
    dogs = 0
    for i in range(len(user_num)):
        if comp_num[k] == user_num[k]:
            cats = cats+1
        else:
            dogs = dogs+1 
        k = k+1
        
    print(cats,"cats",end = ",")
    print(dogs,"dogs")


    exit_game = input("Do you want to Exit the game, press (y / n): ")
    if exit_game == "y" or exit_game == "yes":
        print("--------------------------- Thanks for playing ---------------------------")
        break 
    else:
        pass
    