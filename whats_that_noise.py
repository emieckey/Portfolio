start = "You are laying in bed when you hear a noise downstairs. Do you go investigate?"


print(start)


user_input = input("Type 'Y' for yes or 'N' for no. ")
if user_input.upper() == "Y":
    weapon = input("Ahh! There's a monster in your kitchen! What weapon will you use? wooden spoon or frying pan ")
    if weapon.lower() == "wooden spoon":
        method = input("The monster feels threatened. try to reason with it or fight ")
        if method.lower() == "reason with it":
            print("Oh no! The monster ate you!")
        elif method.lower() == "fight":
            print("You take your chance and WIN!")
        else:
            print("Invalid option")
    elif weapon == "frying pan":
        place = input("You wack the monster in the head and temporarly stun it. Where will you run and hide? bathroom or closet ")
        if place.lower() == "bathroom":
            where = input("You lock the door. Will you stay and try to find a weapon or jump out the window? stay or jump ")
            if where.lower() == "stay":
                bathweapons = input("Which weapon will you choose? blowdryer or cup of water ")
                if bathweapons.lower() == "blowdryer":
                    action = input("The hot air angers the monster and it bites you. You need to act quick! fight or escape or tend to wounds ")
                    if action.lower() == "fight":
                        print("The monster is stronger than you. You die.")
                    elif action.lower() == "escape":
                        print("You escape the monster. You WIN!")
                    elif action.lower() == "tend to wounds":
                        print("You try to get to the med kit but it's too late. You die.")
                elif bathweapons.lower() == "cup of water":
                    print("The water dissolves the monster and kills it. You WIN!")
                else:
                    print("Invalid option")
            elif where.lower() == "jump":
                tell = input("You open the window and jump out but you get stuck in the tree. Emergency services come and rescue you. Do you tell them about the monster? Y or N ")
                if tell.lower() == "Y":
                    print("They investigate the house and find nothing. They conclude that you are delusional, but at least you're safe from the monster")
                elif tell.lower() == "N":
                    print("The monster comes outside and eats everyone")
                else:
                    print("Invalid option")
            else:
                print("Invalid option")
        elif place.lower() == "closet":
            print("The monster sniffed you out and ate you!")
        else:
            print("Invalid option")
    else:
        print("Invalid option")

elif user_input.upper() == "N":
    print("Oh no! A monster came up the stairs and ate you!")
else:
    print("Invalid option")
