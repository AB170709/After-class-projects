tickets_available=10
passenger_name=input("enter the passenger's name:")
destination=input("enter the passenger's destination:")
ticket_price=int(input("enter value of single ticket:"))
tickets_booked=int(input("enter value of tickets booked:"))
morning_ticket_price=700
evening_ticket_price=900
print(type(tickets_available))
print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(tickets_booked))
print(type(morning_ticket_price))
print(type(evening_ticket_price))

total_cost=ticket_price*tickets_booked
discount=78
final_cost=total_cost-discount
print("Total Cost: Rs", total_cost)
print("Discount: Rs", discount)
print("Final Cost: Rs", final_cost)

print("Is ticket price under Rs1000?", ticket_price < 1000)
print("Are more than 2 tickets booked?", tickets_booked > 2)
print("Is destination Goa?", destination == "Goa")
print("Is final cost more than Rs2000?", final_cost > 2000)

travel_message = passenger_name + " is travelling to " + destination + "."
print("Travel Message:", travel_message)
print("Destination in uppercase:", destination.upper())
print("Passenger name in lowercase:", passenger_name.lower())
print("First letter of destination:", destination[0])
print("Length of passenger name:", len(passenger_name))

print("Morning Ticket Price: Rs", morning_ticket_price)
print("Evening Ticket Price: Rs", evening_ticket_price)
morning_ticket_price=evening_ticket_price
evening_ticket_price = morning_ticket_price
print("After Swapping:")
print("Morning Ticket Price: Rs", morning_ticket_price)
print("Evening Ticket Price: Rs", evening_ticket_price)
 

 








