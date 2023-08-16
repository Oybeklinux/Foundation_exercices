# Use these cells to answer the question - build the function step-by-step
import math
def cost_of_trip(flight_cost, hotel_rate, car_rental_rate, trip_duration):
    total_cost = flight_cost + (hotel_rate * trip_duration) + (car_rental_rate * math.ceil(trip_duration/7))
    return total_cost

# Solution 1
paris = cost_of_trip(flight_cost=200, hotel_rate= 20, car_rental_rate=200,trip_duration=7)
london = cost_of_trip(flight_cost=250, hotel_rate= 30, car_rental_rate=120,trip_duration=7)
dubai = cost_of_trip(flight_cost=370, hotel_rate= 15, car_rental_rate=80,trip_duration=7)
mumbai = cost_of_trip(flight_cost=450, hotel_rate= 10, car_rental_rate=70,trip_duration=7)

xdict = {'paris':paris, 'london':london, 'dubai':dubai, 'mumbai':mumbai}
print(xdict)
print("City you should visit with least amount of money to spend for 1 week :",min(xdict.keys(), key=xdict.get))
