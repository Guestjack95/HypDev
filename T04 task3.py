#Asks the user to enter their times for the 3 triathlon events.
swimming = int(input("Please enter your swimming time in minutes: "))

cycling = int(input("Please enter your cycling time in minutes: "))

running = int(input("Please enter your running time in minutes: "))

#Output the total time and any awards earned for this result.
triathlon = (swimming + cycling + running)
total = f"Your total triathlon time is {triathlon} minutes."
print(total) 

if triathlon < 100:
    print("Congratulations, you have earned the Provincial Colours award")

elif (100 <= triathlon < 105):
    print("Congratulations, you have earned the Provincial Half Colours award")

elif (triathlon < 110): 
    print("Congratulations, you have earned the Provincial Scroll award")

else:
    print("Unfortunately, you did not qualify for any award.")