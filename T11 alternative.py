#Define and then print the starting string
string = "This program handles strings"
print(f"Starting string: {string}")

#Using a for loop to iterate over the entire length of string, set odd values to lowercase and even values to uppercase
case = ""
for i in range(len(string)):
    if i % 2 == True:
        case = case + string[i].lower()
    else: 
        case = case + string[i].upper()
    
print(f"Alternate letters: {case}")

#Convert string to a list using split()
list = string.split()

#As above, this time looping over the elements in list. 
for i in range(len(list)):
    if i % 2 == True:
        list[i] = list[i].lower()
    else:
        list[i] = list[i].upper()


#Using whitespace as a separator, rejoin the elements from list into final_string and print
separator = " "
final_string = separator.join(list)
print(f"Alternate words: {final_string}")



