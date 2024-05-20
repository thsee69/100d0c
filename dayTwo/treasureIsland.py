print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional
# .drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

choice1 = input('You\'re at a narrow & rocky crossroad, There is only 2 directions,\n'
                'where do you want to go? Type "left" or "right".\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to an eerie lake with a thick layer of mist above the surface..'
                    'the air seems heavy.\n'
                    'You spot a light on the other side of the lake, its dim, but it\'s there.\n'
                    'Type "Wait" to wait for a boat, "Swim" to swim across the lake,\n').lower()
    if choice2 == "wait":
        input('Alas, after what seemed to be hours, a small boat breaks through the fog,\n'
              'aboard is a mysterious, pale man, carrying a lantern.\n'
              'Slowly he pulls ashore, the light reflecting off his rough skin and stained beard.\n'
              '"Are ye coming about mate?.." he asks...')
        print(""" 

  @_     |       @    __  
        /|}    @__
       /_|\\         @
     ____|_____   
     \\_o_o_o_/     
~~%%~~~~~~~~~~~~~%~~~~""")
        print("\n")
        print("The mysterious man has delivered you safely across the lake,\n"
              "all while telling you about the dangers lurking below and around the island.\n"
              "You step off the boat and your feet sink into the muddy shore, after a short trek\n"
              "and you arrive at the light you spotted across the lake.\n"
              "It is a dimly lit cave...\n")
        choice3 = input("Upon entering the cave, you notice a series of 3 corridors.\n"
                        "One on the left,\n"
                        "one on the right,\n"
                        "and a dark, dingy, much narrower passage straight ahead.\n\n"
                        "Type 'Left' to go left\n"
                        "Type 'Right' to go right\n"
                        "Type 'Center' to continue ahead\n")
        if choice3 == "left":
            print("\nThe corridor to the left is the brightest of the 3, which sparks hope.\n"
                  "as you slowly explore the light begins to fade,\n"
                  "you hear scratching, growing louder and louder,\n"
                  "until it stops, completely..\n"
                  "you hesitantly push forward until the light dies out completely.\n"
                  "the scratching begins but this time it is next to you!\n"
                  "in this moment you feel the sharp claws of hundreds of mite-rats!\n"
                  "ungodly creatures barely the size of a quarter, bred for one thing...\n"
                  "to feast on the flesh of man!\n"
                  "you fall to your knees as they eat away from the toes up,\n"
                  "unable to fight back, you succumb to the horrific death..\n")
        elif choice3 == "right":
            print("\nSeconds after entering the right corridor you notice blood smears along the walls,\n"
                  "following the hallway the amount of blood grows as does your concern.\n"
                  "you come to an empty room, no bigger then a closet. \n"
                  "as you turn around, you notice the already dim light flutter in and out,\n"
                  "until......... darkness..... "
                  "you feel a dark force attach itself to each of your limbs.\n"
                  "the force pulling you back into the empty room, your fighting with all of your might..\n"
                  "until your swallowed into the darkness...\n")
        elif choice3 == "center":
            print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢯⠙⠩⠀⡇⠊⠽⢖⠆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠱⣠⠀⢁⣄⠔⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣷⣶⣾⣾⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡔⠙⠈⢱⡟⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡠⠊⠀⠀⣀⡀⠀⠘⠕⢄⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠞⠀⠀⢀⣠⣿⣧⣀⠀⠀⢄⠱⡀⠀⠀⠀
⠀⠀⡰⠃⠀⠀⢠⣿⠿⣿⡟⢿⣷⡄⠀⠑⢜⢆⠀⠀
⠀⢰⠁⠀⠀⠀⠸⣿⣦⣿⡇⠀⠛⠋⠀⠨⡐⢍⢆⠀
⠀⡇⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣦⡀⠀⢀⠨⡒⠙⡄
⢠⠁⡀⠀⠀⠀⣤⡀⠀⣿⡇⢈⣿⡷⠀⠠⢕⠢⠁⡇
⠸⠀⡕⠀⠀⠀⢻⣿⣶⣿⣷⣾⡿⠁⠀⠨⣐⠨⢀⠃
⠀⠣⣩⠘⠀⠀⠀⠈⠙⣿⡏⠁⠀⢀⠠⢁⡂⢉⠎⠀
⠀⠀⠈⠓⠬⢀⣀⠀⠀⠈⠀⠀⠀⢐⣬⠴⠒⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀"""
                  "\nThe dark dingy hole in the wall sits there, like a pungent abyss, filled with uncertainty.\n"
                  "you rethink your decision, but decide to continue..\n"
                  "you come to an unsteady wall of rocks, it looks like one push should do the job.\n"
                  "pushing on the rocks the wall collapses...\n"
                  "your eyes widen.. as an island of gold coins, jewelry and gems lay forth.\n"
                  "Congratulations!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⢀⣠⣤⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⢠⣾⣿⣿⣧⣿⣶⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⢀⣿⣿⡟⠉⠙⠛⠛⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⢸⣿⣿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⣼⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⣀⣤⣤⣤⣄⠀⠀⠀⠀⢰⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣶⣦⡀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣷⡄⠀⠀⣸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠐⠛⠛⠛⠓⠀⠀⠚⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀\n"""
              "You were attacked by a terrifying creature,\n"
              "you struggled, but nonetheless you were dragged into the murky depth...\n"
              "to meet your fate..")
else:
    print("You fell into a hole. Game Over.")
