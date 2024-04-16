import random
import math

def guess_number(lower, upper):
    # tạo số ngẫu nhiên giữa dưới và trên
    x = random.randint(lower, upper)
    print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n")

    # Initializing the number of guesses - Đang khởi tạo số lần đoán.
    count = 0

    # để tính số lần đoán tối thiểu tùy thuộc vào phạm vi
    while count < math.log(upper - lower + 1, 2):
        count += 1
        
        # taking guessing number as input
        guess = int(input("Guess a number: "))
        
        # Condition testing
        if x == guess:
            print("Congratulations you did it in ", count, " try")
            # Sau khi đoán được, vòng lặp sẽ bị ngắt
            return
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You guessed too high!")
            
    # Nếu Đoán nhiều hơn yêu cầu, hãy hiển thị kết quả này.
    if count > math.log(upper - lower + 1, 2):        
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")

# Taking Inputs
lower = int(input("Enter Lower bound: "))
upper = int(input("Enter Upper bound: "))

# Running the guessing game
guess_number(lower, upper)

# Ask if user wants to play again
while True:
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes' and play_again != 'no':
        print("Invalid input! Please enter 'yes' or 'no'.")
    elif play_again == 'yes':
        # Taking Inputs again
        lower = int(input("Enter Lower bound: "))
        upper = int(input("Enter Upper bound: "))
        guess_number(lower, upper)
    else:
        print("Thanks for playing!")
        break

