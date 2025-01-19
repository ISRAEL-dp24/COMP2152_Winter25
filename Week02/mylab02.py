# import random
# def number_guessing_game():
#     targetNumber = random.randint(1, 100)
#
#     play = input("DO you want to play a number guessing game? (yes/no): ").strip().lower()
#
#     attempts = 0
#     max_attempts = 10
#
#     while attempts < max_attempts:
#         try:
#             userGuess = int(input("Enter your guess: "))
#             #attempts = attempts + 1
#             attempts += 1
#             if userGuess < targetNumber:
#                 if (userGuess - targetNumber) <= 5:
#                     print("Too low! You're very close! Try again.")
#                 else:
#                     print("Too low! Try again.")
#             elif userGuess > targetNumber:
#                 if abs(userGuess - targetNumber) <= 5:
#                     print("Too high! You're very close! Try again.")
#                 else:
#                     print("Too high! Try again.")
#                     else:
#                     print(f"Congragulation! You've guessed it in {attempts} attempts.")
#                     return
#                 except ValueError:
#                 print("Invalid input! Please enter a number between 1 and 100")
#             print(f"Game over! The target number was {targetNumber}.")
#
#
#             return  True
#         except:
#             print("")
#
#     play = input()
#     return True