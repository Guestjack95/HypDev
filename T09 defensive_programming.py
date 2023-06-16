import re

#Define function num_input. When called only accepts float input from the user
def num_input(entry):
   while True:
      try:
         user_entry = float(input(entry))
      except ValueError:
         print("Error: Please enter a number.")
         continue
      else:
         return user_entry
      
#Define function to check for valid filename as Windows does not accept <>:\"/\|?*.
#Used Regular Expression to search for special characters which are not allowed
def valid_filename(file_name):
   invalid = r"[<>:\"/\\|?*]"
   if re.search(invalid, file_name):
      return False
   else:
      return True

print("This program saves equations to a text file.")
while True:

   file_name = input("Please enter a name for this file (cannot include <>:\"/\\|?*): ")

   #If the input does not meet the criteria in valid_filename function, ask user to try again
   while valid_filename(file_name) == False:
      file_name = input("Error: Filename cannot include <>:\"/\\|?* please try again: ")

   file_name = (f"{file_name}.txt")

   f = open(file_name, "a") 
   f.close()
   break

results = "n"
while True:
   
    if results == "n":
       #Assign a numerical value to num1 using the num_input function as above
      num1 = num_input("Please enter your first number: ")

      #Asks user to enter a numerical operator, input is checked against list to ensure it is valid
      operator = input("Please enter an operator (+, -, *, /): ")
      while operator not in ["+", "-", "*", "/"]:
         operator = input("Error: Please enter a valid operator (+, -, *, /): ")

      num2 = num_input("Please enter your second number: ")   

      #4 conditional statements, one for each operator (+, -, *, /)
      #Each one opens/creates the text file equations.txt, writes the user entered equation to it and then prints the result.

      if operator == "+":
         f = open(file_name, "a")
         f.write(f"{num1} + {num2} = {num1 + num2}\n")
         f.close()
         print(f"{num1} + {num2} = {num1 + num2}")

      elif operator == "-":
         f = open(file_name, "a")
         f.write(f"{num1} - {num2} = {num1 - num2}\n")
         f.close()
         print(f"{num1} - {num2} = {num1 - num2}")

      elif operator == "*":
         f = open(file_name, "a")
         f.write(f"{num1} * {num2} = {num1 * num2}\n")
         f.close()
         print(f"{num1} * {num2} = {num1 * num2}")

      elif operator == "/" and num2 != 0:
         f = open(file_name, "a")
         f.write(f"{num1} / {num2} = {num1 / num2}\n")
         f.close()
         print(f"{num1} / {num2} = {num1 / num2}") 

      else:
         print("You cannot divide by 0")    
      
      results = input("Type 'n' to enter a new equation, 'f' to read from a text file or 'e' to exit: ")


    #Try/except checks user input to see if the file requested exists. If it does contents are printed out, if not user is prompted to try again
    elif results == "f":
       try:
         open_file = (input(f"Please enter the name of the text file you would like to open (results from this calculator are stored in '{file_name}'): "))
         f = open(f"{open_file}", "r")
         print(f.read())
       except FileNotFoundError:
         print("That file was not found. Please try again")

       results = input("Type 'n' to enter a new equation, 'f' to read from a text file or 'e' to exit: ")

    elif results == "e":
       print(f"Your results are saved to '{file_name}'. Thank you for using this calculator")
       break

    else:
      results = input("Error: Invalid entry, try again.\nType 'n' to enter a new equation, 'f' to read from a text file or 'e' to exit: ")
      continue   