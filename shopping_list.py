# Create a new empty list name shopping_list
shopping_list = []

def show_help():
  print("What should we pick up at the store?")
  print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")

  
# Create a function named add_to_list that declares a parameter named item
# Add the item to the list
def add_to_list(item):
  shopping_list.append(item)
  # Notify user that the item was added, and state the number of items in the list currently
  print("The item was added, there are {} items in your list currently".format(len(shopping_list)))

  
# Define a function named show_list that prints all the items in the list
def prints_list(shopping_list):
  print("Here is the list of the items: ")
  for item in shopping_list:
    print("> "+item)

        
show_help()
while True:
  new_item = input("> ")
  if new_item.upper() =='DONE':
    break
  elif new_item.upper() == 'HELP':
    show_help()
    continue
  # Enable the SHOW command to show the list. Don't forget to update the HELP documentation
  # HINT: Make sure to run it.
  elif new_item.upper() =='SHOW':
    prints_list(shopping_list)
    continue
  # Call add_to_list with new_items as an argument
  add_to_list(new_item)
  
show_list()
