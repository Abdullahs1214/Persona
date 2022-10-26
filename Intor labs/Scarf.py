#--------------------------------------------------
# Change these variables to design your own scarf!
# Add a comment describing what each variable does.
#--------------------------------------------------

# this variable...
colours = ['#', '|', "^"]

# this variable dtermines how many # or | will appear
colour_length = 6

# this variable detemnes how long the pattern goes
pattern_length = 20

# this variable detemines how wide in the line the pattern can go
pattern_width = 15

#--------------------------------------------------
# Don't change anything below this line!
#--------------------------------------------------

print("Here is your scarf:\n")
for pos in range(int(pattern_width * pattern_length)):
    print( colours[ int ((pos)/colour_length) % len(colours)], end="")
    if (pos % pattern_width) == pattern_width-1:
        print("")