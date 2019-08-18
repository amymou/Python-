SERVICE_CHARGE = 2
TICKET_PRICE = 10
tickets_remaining = 100  
# Outpout how many tickets are remaining using the ticket_remaining variable
# Gather the user's name and assign it to a new variable
names = input("Please provide your name: ")
# Prompt the user by name and ask how many tickets they would like
print("Hi {}.".format(names))
tickets_asked = int()
# Create the calculate_price function. It takes number of tickets and returns
#  num_tickets*TICKET_PRICE
def calculate_price(number_of_tickets):
  return(number_of_tickets*TICKET_PRICE)+SERVICE_CHARGE
# Run this code continuously until we run of tickets
while tickets_remaining-tickets_asked>0:
  # Expect a ValueError to happen and handle it appropriately...remember to test it out!
  try:
      tickets_asked = int(input("How many tickets would you like? "))
      #Raise a ValueError if the request is for more tickets than are available
      if tickets_asked > tickets_remaining:
        raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
  except ValueError as err:
    #Include the error text in the output
     print("Oh no, we ran into an issue {}. Please try again!".format(err))
  else:
      # Calculate the price (number of tickets multiplied by the price) and assign it to variable
      total_price = calculate_price(tickets_asked)
      # Output the price to the screen
      print("Okay, the total price is ${}".format(total_price))
      # Prompt user if they want to proceed. Y/N?
      proceed =input("Would you like to proceed? Yes/No ")
      # If they want to proceed
      if proceed == 'Yes':
      # print out to the screen "SOLD!" to confirm purchase
        print("SOLD!")
        # and then decrement the tickets remaining by the number of tickets purchased
        tickets_remaining -= tickets_asked
        print("There are {} tickets remaining.".format(tickets_remaining))
        # Otherwise...
        print("Thank you, {}!".format(names))
        user_keep_buying =input("Would you like more tickets? Yes/No ")
      if user_keep_buying == 'No':
        # Thank them by name
        print("Thank you for visiting {}!".format(names))
        break
           
# Nofify user that the tickets are sold out 
else:
           print("There are no more tickets for this event")
