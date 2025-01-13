#Name Generator

#Functions

def name_generator():
    print("Welcome to What Hero Are You")
    print("Answer all the questions to see what superhero you are")
    ans = input("Marvel (m) or DC (d)?")
    if ans == "m":
        ans = input("Autumn (a) or Winter (w)?")
        if ans == "a":
            ans = input("Pumpkin Spice (ps) or Cider Donuts (cd)?")
            if ans == "ps":
                print("You are Spiderman!")
            else:
                print("You are Captain America!")
        if ans == "w":
            ans = input("Snow (sn) or Hot Coco (hc)?")
            if ans == "sn":
                print("You are Black Widow!")
            else:
                print("You are Ironman!")
    if ans == "d":
        ans = input("Summer (su) or Spring (spr)?")
        if ans == "su":
            ans = input("Pool (p) or Beach (b)?")
            if ans == "p":
                print("You are Superman!")
            else:
                print("You are Batman!")
        if ans == "spr":
            ans = input("Flowers (f) or Rain (r)?")
            if ans == "f":
                print("You are Wonder Woman!")
            else:
                print("You are Flash!")

#Main

name_generator()
