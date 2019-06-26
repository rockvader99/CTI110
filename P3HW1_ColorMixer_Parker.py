# CTI-110
# P3HW1 - Color Mixer
# Ethan Parker
# 6/25/2019
# This program mixes primary colors. If any other color than Red, Yellow, or Blue is entered, the program will not mix.
Color1 = input( "Would you please give me the first color?:")
Color2 = input( "Would you please give me the second color?:")
if (Color1 == "red" and Color2 == "blue") or \
   (Color1 == "blue" and Color2 == "red"):
    print( Color1 + " and " + Color2 + " are purple." )
elif (Color1 == "red" and Color2 == "yellow")or \
   (Color1 == "yellow" and Color2 == "red"):
    print( Color1 + " and " + Color2 + " are orange." )
elif (Color1 == "yellow" and Color2 == "blue") or \
   (Color1 == "blue" and Color2 == "yellow"):
    print( Color1 + " and " + Color2 + " are green." )
else:
    print("I don't recognize either " + Color1 + " or " + Color2 + ". Did you use a primary color?" )
