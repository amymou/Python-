TICKET_PRICE = 10

tickets_remaining = 100  
# Outpout how many tickets are remaining using the ticket_remaining variable


# Gather the user's name and assign it to a new variable
names = input("Please provide your name: ")

# Prompt the user by name and ask how many tickets they would like

print("Hi {}.".format(names))
tickets_asked = int()
# Run this code continuously until we run of tickets
while tickets_remaining-tickets_asked>0:
  tickets_asked = int(input("How many tickets would you like? "))
  # Calculate the price (number of tickets multiplied by the price) and assign it to variable
  total_price = tickets_asked * TICKET_PRICE
# Output the price to the screen
  print("Okay, the total price is ${}".format(total_price))

    
# Prompt user if they want to proceed. Y/N?
  proceed =input("Would you like to proceed? Yes/No ")
# If they want to proceed
  if proceed == 'Yes':
    # print out to the screen "SOLD!" to confirm purchase
    print("SOLD!")
    # and then decrement the tickets remaining by the number of tickets purchased
    tickets_remaining = tickets_remaining - tickets_asked
    print("There are {} tickets remaining.".format(tickets_remaining))
# Otherwise...
  else:
    print("Come back when you are ready!")
    # Thank them by name
  print("Thank you, {}!".format(names))
  user_keep_buying =input("Would you like more tickets? Yes/No ")
  if user_keep_buying == 'No':
    break
# Nofify user that the tickets are sold out 
else:
  print("There are no more tickets for this event")
