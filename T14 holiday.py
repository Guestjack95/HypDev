#function to only accept integer inputs
def num_input(entry):
   while True:
      try:
         user_entry = int(input(entry))
      except ValueError:
         print("Error: Please enter a number.")
         continue
      else:
         return user_entry

#function to calculate total cost of hotels, cost of hotel at location multiplied by number of nights stayed
def hotel_cost(city_flight, num_nights):
   if city_flight in destination_hotel:
      cost = destination_hotel[city_flight] * num_nights
      return cost
   else:
      return None

#function to calculate flight costs, cost to fly to user's choice of city multiplied by 2 (for the return flight)
def plane_cost(city_flight):
   if city_flight in destination_flight:
      cost = destination_flight[city_flight] * 2
      return cost
   else:
      return None

#function to calculate cost of renting a car for the holiday, cost of car rental per day multiplied by number of days rented
def car_rental(city_flight, rental_days):
   if city_flight in destination_flight:
      cost = destination_flight[city_flight] * rental_days
      return cost
   else:
      return None

#function to total the outcomes from the previous 3 functions
def holiday_cost(hotel_cost, plane_cost, car_rental):
   total = hotel_cost + plane_cost + car_rental
   return total

#dictionaries containing available locations and costs for hotels, flights and car rental
destination_hotel = {"paphos" : 155, "malta" : 214, "belfast" : 97, "copenhagen" : 317, "bergen" : 169}
destination_flight = {"paphos" : 188, "malta" : 163, "belfast" : 40, "copenhagen" : 119, "bergen" : 95}
destination_car_rental = {"paphos" : 31, "malta" : 22, "belfast" : 17, "copenhagen" : 45, "bergen" : 38}

menu_message = "Please choose a holiday destination: "
print(menu_message)

#iterates over dictionary to print available locations to the user
for index, value in enumerate(destination_hotel):
    menu_message = f"{index+1}. {value.capitalize()}\n"
    print(menu_message)

city_flight = input("Enter the name of the city you wish to visit: ")
city_flight = city_flight.lower()

#print user selection or prompt user to retry if city_flight input does not match choices shown
if city_flight in destination_hotel:
    print(f"You have selected {city_flight.capitalize()}.\n")
else:
    print(f"Error: Invalid selection. Please choose from {list(destination_hotel)}")

num_nights = num_input("How many nights are you staying at the hotel? ")

rental_days = num_input("\nHow many days will you rent a car? ") 

print("\n\nThis is the breakdown of your holiday costs:")

#assign outputs from functions to variables then print to display holiday costs
hotel_total = hotel_cost(city_flight, num_nights)
print(f"\nThe total cost of your hotel is £{hotel_total}\n")

plane_total = plane_cost(city_flight)
print(f"The total cost of your flights (including return) is £{plane_total}\n")

car_total = car_rental(city_flight, rental_days)
print(f"The total cost of your car rental is £{car_total}\n")

print(f"The total cost of your holiday is £{holiday_cost(hotel_total, plane_total, car_total)}")