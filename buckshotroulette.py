import time
import os
import sys
import colorama
from colorama import Fore

#Setup
colorama.init()

class Room:
    def __init__(self, name):
        self.name = name
        self.exits = {}

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def print_info(self):
        print(self.name)

#Rooms
desert = Room(Fore.GREEN + "Your only option is heading towards the light"
              +Fore.GREEN +"\n"
              +Fore.YELLOW + "\nTo the North, you can head towards the dim light.")
light = Room(Fore.GREEN + "You walk a little towards the light."
             "\n"
             +Fore.YELLOW +"\nTo the North, you can continue heading towards the dim light.")
caravan_outside = Room(Fore.GREEN +"You see an old, rusty caravan. The light seems to be emitting from inside."
                       +Fore.GREEN +"\n"
                       +Fore.YELLOW +"\nTo the North, you can go inside the caravan.")
caravan_inside = Room(Fore.GREEN +"You're inside the caravan. You see a bunch of books on an old table to the side of the door."
                      +Fore.GREEN +"\n"
                      +Fore.YELLOW +"\nTo the West, you can see a bedroom."
                      +Fore.YELLOW +"\nTo the North, you can explore the living room."
                      +Fore.YELLOW +"\nTo the East, you see a bathroom."
                      +Fore.YELLOW +"\nTo the South, you can exit the caravan.")
caravan_bedroom = Room(Fore.GREEN +"You enter the caravan bedroom. The closet doors are"
                       +Fore.GREEN +"\nmissing and the bed is broken. There is a key on the desk."
                       +Fore.GREEN +"\n"
                       +Fore.LIGHTBLUE_EX +"\nTo pick up the key, type 'pick up key'."
                       +Fore.YELLOW +"\nTo the South, you can head back to the main entrance of the caravan.")
caravan_bathroom = Room(Fore.GREEN +"You enter the bathroom. You see cracked tiles littering the floor, and "
                        +Fore.GREEN +"\nthe sink is caked with grime. The mirror is shattered, reflecting "
                        +Fore.GREEN +"\nonly fragments of your own image. Amidst the debris, you spot a rusty hammer, "
                        +Fore.GREEN +"\nits handle worn from neglect."
                        +Fore.GREEN +"\n"
                        +Fore.LIGHTBLUE_EX +"\nTo pick up the hammer, type 'pick up hammer'."
                        +Fore.YELLOW +"\nTo the South, you can head back to the main entrance of the caravan.")
caravan_livingroom = Room(Fore.GREEN +"As you step into the old abandoned caravan's living room, the moonlight"
                         +Fore.GREEN +"\nfilters through the tattered curtains, casting eerie shadows across the"
                         +Fore.GREEN +"\nworn furniture.  You spot a note lying on the ground, its edges frayed with age."
                         +Fore.GREEN +"\n"
                         +Fore.LIGHTBLUE_EX +"\nTo read the note, type 'read note'."
                         +Fore.YELLOW +"\nTo the South, you can head back to the main entrance of the caravan.")
caravan_livingroom_note = Room(Fore.GREEN + "Hey there,"
                               +Fore.GREEN + "\nIf you're reading this, then you're probably in the same boat as "
                               +Fore.GREEN +"\nme – lost, scared, and wondering what the heck is going on. I stumbled "
                               +Fore.GREEN +"\nupon this old caravan in the dead of night, hoping to find some shelter "
                               +Fore.GREEN +"\nfrom the cold desert. But let me tell you, what I found wasn't much better."
                               +Fore.GREEN +"\nI don't know how to explain it, but there's something out there,"
                               +Fore.GREEN +"\nsomething not quite right. It's like straight out of a nightmare – twisted,"
                               +Fore.GREEN +"\nshadowy figures creeping in the darkness, their eyes glowing with an"
                               +Fore.GREEN +"\nunholy light. I barely escaped with my life, and now I'm holed up in"
                               +Fore.GREEN +"\nthis caravan, praying for someone to come along and lend a hand. "
                               +Fore.GREEN +"\nIf you're out there and you can hear me, please, I beg you, help me."
                               +Fore.GREEN +"\nI don't know how much longer I can hold out on my own."
                               +Fore.GREEN +"\nJust be careful, though. Whatever's out there, it's not human. And it's definitely"
                               +Fore.GREEN +"\nnot friendly."
                               +Fore.GREEN +"\n"
                               +Fore.YELLOW +"\nTo back out, type 'back'.")
desert2 = Room(Fore.GREEN +"As you venture deeper into the cold desert, the biting chill seeps into your bones, "
              +Fore.GREEN +"\ncausing you to shiver involuntarily. The vast expanse of sand stretches out before you, "
              +Fore.GREEN +"\ndevoid of life save for the occasional scuttle of unseen creatures. Yet, despite the emptiness, "
              +Fore.GREEN +"\nyou can't shake the feeling of being watched. It's as if unseen eyes follow your every move, "
              +Fore.GREEN +"\ntheir presence lingering just beyond the edge of your perception. A sense of unease "
              +Fore.GREEN +"\nwashes over you, a feeling of non-belonging in this desolate landscape. With each step, "
              +Fore.GREEN +"\nthe weight of the unknown presses down upon you, urging you forward into the unknown."
                           "\n"
             +Fore.YELLOW +"\nTo the North, you can continue heading into the desert."
             +Fore.YELLOW +"\nTo the South, you can make your way back.")
desert_chest = Room(Fore.GREEN +"As you traverse the unforgiving cold desert, the howling wind whips grains"
                    +Fore.GREEN +"\nof sand against your skin, stinging like icy needles. The vast emptiness"
                    +Fore.GREEN +"\nstretches out before you, a desolate landscape devoid of life. Yet, amidst"
                    +Fore.GREEN +"\nthe barren expanse, you notice a glimmer of hope—a weathered chest"
                    +Fore.GREEN +"\nhalf-buried in the sand. It beckons to you, promising the possibility of "
                    +Fore.GREEN +"\ntreasure and respite from the harsh wilderness."
                                 "\n"
             +Fore.LIGHTBLUE_EX +"\nTo find out what's in the chest, type 'open chest'."
                    +Fore.YELLOW+"\nTo the North, you can continue heading into the desert."
                    +Fore.YELLOW+"\nTo the South, you can make your way back.")
desert_crying_girl = Room("")

#Exits
desert_chest.add_exit("south", desert2)
desert_chest.add_exit("north", desert_crying_girl)
desert2.add_exit("south", caravan_outside)
desert2.add_exit("north", desert_chest)
desert.add_exit("north", light)
caravan_outside.add_exit("south", light)
caravan_outside.add_exit("north", caravan_inside)
caravan_inside.add_exit("west", caravan_bedroom)
caravan_inside.add_exit("south", caravan_outside)
caravan_inside.add_exit("north", caravan_livingroom)
caravan_livingroom.add_exit("read note", caravan_livingroom_note)
caravan_livingroom.add_exit("south", caravan_inside)
caravan_livingroom_note.add_exit("back", caravan_livingroom)
caravan_bedroom.add_exit("south", caravan_inside)
caravan_bathroom.add_exit("south", caravan_inside)
light.add_exit("south", desert)
light.add_exit("north", caravan_outside)

#Items
key = "bathroom key"
hammer = "hammer"
dagger = "dagger"

#Useful
current_room = desert

#lists
desert_chest_items = [dagger]
caravan_bathroom_items = [hammer]
caravan_bedroom_items = [key]
caravan_bathroom_door = []
inventory = []

#Introduction
print(Fore.GREEN + "After what felt like years of sleep,")
#time.sleep(2)
print(Fore.GREEN + "you wake up in an empty desert, all alone.")
#time.sleep(2)
print(Fore.GREEN + "It's night and it's freezing, and the moon, the stars and a dim")
#time.sleep(2)
print(Fore.GREEN + "light coming from the horizon are the only things enlightening")
#time.sleep(2)
print(Fore.GREEN + "your way.")
#time.sleep(2)

#Game loops
#Bedroom/Bathroom + key loop
while True:
    current_room.print_info()
    command = input("\n>").strip().lower()
    os.system('cls')

    if command in current_room.exits:
        current_room = current_room.exits[command]

    elif command == ("east") and current_room == caravan_inside:
        if key in inventory:
            print(Fore.GREEN +"\nYou have unlocked the door.\n")
            caravan_bathroom_door.append(key)
            pass
        elif key in caravan_bathroom_door:
            pass
        else:
            print(Fore.RED +"The door seems to be locked.\n")

    elif command == ("inventory"):
        print(Fore.GREEN +"Your inventory is now composed of:", ", ".join(inventory))

    elif command == ("pick up key") and current_room == caravan_bedroom:
        caravan_bedroom_items.remove(key)
        inventory.append(key)
        print(Fore.BLUE +"You have picked up a key.\n")
        print(Fore.GREEN +"Your inventory is now composed of:", ", ".join(inventory))
        if key not in caravan_bedroom_items:
             caravan_bedroom.name = (Fore.GREEN +"You enter the caravan bedroom. The closet doors are"
                                     +Fore.GREEN +"\nmissing and the bed is broken. The desk is empty."
                                     +Fore.GREEN +"\n"
                                     +Fore.YELLOW +"\nTo the South, you can head back to the main entrance of the caravan.")
             caravan_inside.add_exit("east", caravan_bathroom)
        break

    else:
        print(Fore.RED +"You can't go that way!")

#Hammer loop
while True:
    current_room.print_info()
    command = input("\n>").strip().lower()
    os.system('cls')

    if command in current_room.exits:
        current_room = current_room.exits[command]

    elif command == ("inventory"):
        print(Fore.GREEN + "Your inventory is now composed of:", ", ".join(inventory))

    elif command == ("pick up hammer") and current_room == caravan_bathroom:
        inventory.append(hammer)
        caravan_bathroom_items.remove(hammer)
        caravan_outside.add_exit("east", desert2)
        caravan_outside.name = (Fore.GREEN +"You see an old, rusty caravan. The light seems to be emitting from inside."
                            +Fore.GREEN +"\n"
                           +Fore.YELLOW +"\nTo the North, you can go inside the caravan."
                           +Fore.YELLOW +"\nTo the East, you can continue heading into the desert.")
        print(Fore.GREEN +"You have picked up the hammer.\n")
        print(Fore.GREEN + "Your inventory is now composed of:", ", ".join(inventory))
        if hammer not in caravan_bathroom_items:
             caravan_bathroom.name = (Fore.GREEN +"You enter the bathroom once more. The cracked tiles and "
                                      +Fore.GREEN +"\ngrimy sink remain unchanged, but now, the shattered mirror "
                                      +Fore.GREEN +"\nreflects your determined gaze."
                                      +Fore.GREEN +"\n"
                                      +Fore.YELLOW +"\nTo the South, you can head back to the main entrance of the caravan.")
        break

    else:
        print(Fore.RED +"You can't do that.")
current_room = caravan_bathroom

#Chest loop
while True:
    current_room.print_info()
    command = input("\n>").strip().lower()
    os.system('cls')

    if command in current_room.exits:
        current_room = current_room.exits[command]

    elif command == ("open chest"):
        inventory.append(dagger)
        desert_chest_items.remove(dagger)
        print(Fore.GREEN + "You have picked up a dagger.")
        print(Fore.GREEN + "Your inventory is now composed of:", ", ".join(inventory))
        if dagger not in desert_chest_items:
            desert_chest.name = (Fore.GREEN + "As you trudge through the cold desert, the biting wind cuts through your clothing, "
                                    +Fore.GREEN +"\nchilling you to the bone. The desolation stretches endlessly before you, a bleak landscape "
                                    +Fore.GREEN +"\ndevoid of solace. You cast your eyes upon a weathered chest, its lid thrown open, "
                                    +Fore.GREEN +"\nrevealing emptiness within. The promise of treasure has been claimed,"
                                    +Fore.GREEN +"\nleaving only a hollow reminder of what once was."
                                                 "\n"
                                   +Fore.YELLOW +"\nTo the North, you can continue heading into the desert."
                                   +Fore.YELLOW +"\nTo the South, you can make your way back.")
        break

    elif command == ("inventory"):
        print(Fore.GREEN + "Your inventory is now composed of:", ", ".join(inventory))

    else:
        print(Fore.RED +"You can't do that.")


while True:
    current_room.print_info()
    command = input("\n>").strip().lower()
    os.system('cls')

    if command in current_room.exits:
        current_room = current_room.exits[command]

    elif command == ("inventory"):
        print(Fore.GREEN + "Your inventory is now composed of:", ", ".join(inventory))

    else:
        print(Fore.RED +"You can't do that.")