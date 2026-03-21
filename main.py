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
"""
import time

anaHimaaron = False

print("please type the following letters one by one each followed by a separate enter click: a, n, a,  , h, i, m, a, a, r, o, n. \nRemember that to succeed you can't fail and that if you fail you can't succeed.")

while True:

    a = input("...")
    if a.strip().lower() != "a":
        anaHimaaron = True
        break

    an = input("...")
    if an.strip().lower() != "n":
        anaHimaaron = True
        break

    ana = input("...")
    if ana.strip().lower() != "a":
        anaHimaaron = True
        break

    ana_ = input("...")
    if ana_ != " ":
        anaHimaaron = True
        break

    ana_h = input("...")
    if ana_h.strip().lower() != "h":
        anaHimaaron = True
        break

    ana_hi = input("...")
    if ana_hi.strip().lower() != "i":
        anaHimaaron = True
        break

    ana_him = input("...")
    if ana_him.strip().lower() != "m":
        anaHimaaron = True
        break

    ana_hima = input("...")
    if ana_hima.strip().lower() != "a":
        anaHimaaron = True
        break

    ana_himaa = input("...")
    if ana_himaa.strip().lower() != "a":
        anaHimaaron = True
        break

    ana_himaar = input("...")
    if ana_himaar.strip().lower() != "r":
        anaHimaaron = True
        break

    ana_himaaro = input("...")
    if ana_himaaro.strip().lower() != "o":
        anaHimaaron = True
        break

    ana_himaaron = input("...")
    if  ana_himaaron.strip().lower() != "n":
        anaHimaaron = True
        break
    break

if anaHimaaron:
    print("congrats, you are a himaaron")
    time.sleep(5)
    print("CONGRATS, you are a himaaron")
    time.sleep(4)
    print("CONGRATS, YOU are a himaaron")
    time.sleep(3)
    print("CONGRATS, YOU ARE a himaaron")
    time.sleep(2)
    print("CONGRATS, YOU ARE A himaaron")
    time.sleep(1)
    print("CONGRATS, YOU ARE A HIMAARON")

meanWhile = 10

while meanWhile > 0:
    meanWhile = meanWhile - 1
    time.sleep(1)
    print(".", end="")

time.sleep(5)

while True:
    print("YOU'RE A HIMAARON")
    continue

if not anaHimaaron:
    print("congrats, you are not a himaaron")