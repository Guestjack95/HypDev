import random

#Define minesweep function using argument minefield, result is an appended version of the 2D list. 
#When the original value was "#" it remains as "#", where it was "-" it is set to 0 and then incremented by +1 for each adjacent "#"
def minesweep(minefield):
    nested_list = []
    for x in range(len(minefield)):
        lists = []
        for y in range(len(minefield[x])):
            count = 0

            if minefield[x][y] == "#":
                count = "#"
            
            else:
                # N - if x is not on the first row then check if the N index is == "#" add 1 to count if so
                if x > 0 and minefield[x-1][y] == "#":
                    count += 1
                # NE - if x is not on the first row and y is not in the final column then check if the NE index is == "#" add 1 if so
                if x > 0 and y < len(minefield[x]) - 1 and minefield[x-1][y+1] == "#":
                    count += 1
                # E - if y is not in the final column then check if the E index is == "#" add 1 if so
                if y < len(minefield[x]) - 1 and minefield[x][y+1] == "#":
                    count += 1
                # SE - if x is not on the final row and y is not in the final column then check if the SE index is == "#" add 1 if so
                if x < len(minefield) - 1 and y < len(minefield[x]) - 1 and minefield[x+1][y+1] == "#":
                    count += 1
                # S - if x is not on the final row then check if the S index is == "#" add 1 if so
                if x < len(minefield) - 1 and minefield[x+1][y] == "#":
                    count += 1
                # SW - if x is not on the final row and y is not in the first column then check if the SW index is == "#" add 1 if so
                if x < len(minefield) - 1 and y > 0 and minefield[x+1][y-1] == "#":
                    count += 1
                # W - if y is not in the first column then check if the W index is == "#" add 1 if so
                if y > 0 and minefield[x][y-1] == "#":
                    count += 1
                # NW - if x is not on the first row and y is not in the first column then check if the NW index is == "#" add 1 if so
                if x > 0 and y > 0 and minefield[x-1][y-1] == "#":
                    count += 1

            #appended as str type, will only be used to display results from this point
            lists.append(str(count))
        nested_list.append(str(lists))
    return nested_list

#Two variables that will determine size of minefield
rows = cols = 5

#minefield size is 5x5 as above and all elements are set to "-"
minefield = [["-" for y in range(cols)] for x in range(rows)]

#Iterate over the minefield, creating up to 2 mines per row in the minefield (possible to generate repeat coordinates which will not add any additional mines)
#Sets value of selected indexes to "#" representing a mine
for i in range(rows * 2):
    row = random.randint(0, rows - 1)
    col = random.randint(0, cols - 1)
    minefield[row][col] = "#"

print("Generated a minefield: ")
for row in minefield:
    print(row)

#Call minesweep function on 2D list minefield, assign it to solved_minefield and print
print("\nThe solved minefield: ")
solved_minefield = minesweep(minefield)
for row in solved_minefield:
    print(row)