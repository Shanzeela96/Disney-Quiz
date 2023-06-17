print("Welcome to my disney quiz!")

name = input ("What is your name? \n")

score =0

answer = input ("1. What is the name of the toy store in Toy Story 2? \n[1] Woodys house \n[2]  Al's Toy Barn \n[3] Buzz tree house \n")
if answer == "2":
    print("That is correct!")
    score += 1

else:
    print("Incorect")



answer = input ("2. In what year did Disney World Florida open? \n[1] 1971 \n[2]  1990 \n[3] 1976 \n")
if answer == "1":
    print("That is correct!")
    score += 1

else:
    print("Incorect")



answer = input ("3. What is Dory's signature saying in Finding Nemo? \n[1] Lets go swimming \n[2]  Sail Away \n[3] Just keep swimming \n")
if answer == "3":
    print("That is correct!")
    score += 1

else:
    print("Incorect")




answer = input ("4. For Olaf, some people are worth what? \n[1] Letting go of \n[2]  Melting for \n[3] Keeping hold of \n")
if answer == "2":
    print("That is correct!")
    score += 1

else:
    print("Incorect")    




answer = input ("5. How many official Disney Princesses are there? \n[1] 12 \n[2]  25 \n[3] 37 \n")
if answer == "1":
    print("That is correct!")
    score += 1

else:
    print("Incorect")   



answer = input ("6. What were the first words Mickey Mouse ever spoke? \n[1] Rubber \n[2]  Hot Dog \n[3] Doggie \n")
if answer == "2":
    print("That is correct!")
    score += 1

else:
    print("Incorect")   


























print(f"Congratulation {name}, You Scored {score}.")
