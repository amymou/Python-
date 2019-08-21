# TODO Create an empty list to maintain the player names
player_names = []

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'

askto_add_players=input("Would you like to add players to the list? Yes/No ")
while askto_add_players=='Yes':
  names=input("Please type in a name and add it to the list: ")
  player_names.append(names)
  askto_add_players = input("Would you like to add another player? (Yes/No) ")

# TODO print the number of players on the team
print("\nThere are {} players on the team".format(len(player_names)))
# TODO Print the player number and the player name
# The player number should start at the number one
player_number = 1
for player in player_names:
  print("{}:{}".format(player_number, player))
  player_number +=1
# TODO Select a goalkeeper from the above roster
select_goalkeeper = int(input("Please select the goalkeeper by selecting the play number. 1 - {}: ".format(len(player_names))))

# TODO Print the goal keeper's name
print("{}:{}".format(select_goalkeeper, player_names[select_goalkeeper-1]))
# Remember that lists use a zero based index
