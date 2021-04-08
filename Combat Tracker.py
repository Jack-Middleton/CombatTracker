def request_player_names():
    player_list = []
    players = False
    while not players:
        player_total = {}  # Creating a new character dictionary each time the data is input
        player_total['Name'] = input("Input player name: ")
        while True:
            try:
                player_total['Initiative Score'] = float(input("Enter initiative count: "))  # Convert value entered to int
            except ValueError:
                print("Please enter a number")
                continue
            else:
                player_list.append(player_total)
                break
        finished = False
        while not finished:  # Validation to check the input is only Y or N
            all_names = input("All player data entered? (Y/N): ")
            if all_names.upper() == "Y":
                return player_list
            elif all_names.upper() == "N":
                finished = True
            else:
                print("Please enter Y or N")

player_list = request_player_names()

player_list.sort(key=lambda x: x.get('Initiative Score'), reverse=True)  # Get initiative score and print list in descending order

for player_total in player_list:
    print(f"{player_total.get('Name')}, {player_total.get('Initiative Score')}")

