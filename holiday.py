print("City Break Destinations")
def city_destinations():    #function to print destination menu
    print("1: London")
    print("2: Paris")
    print("3: Tokyo")
    print("4: Dubai")
    print("5: Amsterdam")

def city_chosen():      #function to get user input where they want to go
    while True:
        try:            #making sure they select from options   
            city_chosen = int(input("Enter number of your chosen destination (1 - 5): "))
            if 1<= city_chosen <= 5:
                return city_chosen
            else:
                print("Invalid choice. Please enter between 1 and 5.")
        except ValueError:  
            print("Invalid input. Please enter valid number.")      

#error handling to make sure positive integers are entered for num nights and rental days
def get_positive_integer(prompt):  
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


#function for hotel cost multiplied with days staying
def hotel_cost(num_nights): 
    cost_per_night = 200
    return num_nights * cost_per_night

#function for plane cost depending on the destination
def plane_cost(city_flight):
    if city_flight == 1:
        return 300
    elif city_flight == 2:
        return 500
    elif city_flight == 3:
        return 1000
    elif city_flight == 4:
        return 1100
    elif city_flight == 5:
        return 1200
    else:
        return ("Invalid. Please choose from the list.")

#function for car hire per day
def car_rental(rental_days):
    rental_cost_perday = 70
    return rental_days * rental_cost_perday

#function for total holiday cost
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental


city_destinations() #print function for user to select from
city_flight = city_chosen() 
num_nights = get_positive_integer("Enter the number of nights you will be staying at a hotel: ")
rental_days = get_positive_integer("Enter the number of days for which you will be hiring a car: ")

#Calculating total costs
hotel_total_cost = hotel_cost(num_nights)
plane_total_cost = plane_cost(city_flight)
car_total_cost = car_rental(rental_days)
total_holiday_cost = holiday_cost(hotel_total_cost, plane_total_cost, car_total_cost)

print("\nHoliday Details:")
print(f"Flight to {'London' if city_flight == 1 else 'Paris' if city_flight == 2 else 'Tokyo' if city_flight == 3 else 'Dubai' if city_flight == 4 else 'a'}: ${plane_total_cost}")
print(f"Hotel cost for {num_nights} nights: ${hotel_total_cost}")
print(f"Car rental cost for {rental_days} days: ${car_total_cost}")
print(f"Total holiday cost: ${total_holiday_cost}")