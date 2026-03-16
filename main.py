"""
my_name = "Ayoub Belkich"
my_age = 21
my_favorite_food = "durum"
is_man = True

if is_man:
    gender = "man"
else :
    gender = "woman"

print(f"My name is {my_name} and I am {my_age} years old and I love {my_favorite_food} and I am a {gender}")

while True:
    input("Press enter to continue...")
    input_name = input("What is your name? ")

    if input_name.strip().lower() == my_name.lower():
        break
"""
import math

x = 1.111
y = -2.222
z = math.sqrt(3.3333)

volume = x * abs(y) * pow(z, 2)

had_wrong_answer = False

while True:
    answer = input("Do you want the result? YES OR NO ANSWER ME: ").strip().lower()
    if answer == "yes":
        if had_wrong_answer:
            print("Yes — a wise choice, though I admit I had nearly given up hope of hearing one.")
        else:
            print("Well then — a proper answer. I should be pleased, had the path to it been less laborious.")
            while True:
                try:
                    decimals = int(input("To how many decimal places shall I refine the result for you? "))
                    rounded_volume = round(volume, decimals)
                    print(f"Surely, the volume is {rounded_volume}.")
                    break
                except ValueError:
                    print("Kindly provide a whole number; even simplicity, it seems, has its casualties.")
        break
    elif answer == "no":
        print("You are so studiously incurious that one begins to suspect your ignorance is not a misfortune, but a vocation. Huh.")
        had_wrong_answer = True
    else:
        print("The choice was between 'yes' and 'no'; how you contrived a third answer is beyond me.")
        had_wrong_answer = True