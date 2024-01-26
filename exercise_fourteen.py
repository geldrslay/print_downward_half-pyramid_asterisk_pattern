# Print a downward Half-Pyramid Pattern of Star (asterisk)

# Defining function
def half_pyramid_star(rows):
    for i in range (rows,0,-1):
        for j in range (0, i):
            print ('*', end=" ")
        print ("\n")

half_pyramid_star(5)