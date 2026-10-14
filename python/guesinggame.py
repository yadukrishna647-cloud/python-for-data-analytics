import random
secret_number = random.randint(1, 10)
count = 1
guess = int(input("Guess a number between 1 and 10: "))
while guess != secret_number:
    
    if guess < secret_number:
        print("wrong,the number is higher than", guess)
    else:
        print("wrong,the number is lower than", guess)
    count += 1
    guess = int(input("Guess again: "))
print("Congratulations! You guessed the correct number:", secret_number)
print("Number of guesses:", count)