# CombatTracker

Currently I am working on an initiative tracker for my home D&D games as it's something that interests me and I figured it would be a good way to get me in to programming a little bit more.

In the CLI I needed to allow for two types of input, one being the Character name as a string, the other being an initiative score input as a float value.
To do this I declare the function and create an empty list. I then use a while loop to create an empty dictionary and take the 'Player Name' input and move on to two nested while loops.
The purpose of which is to first take the initiative score input and perform validation to check that the input is a float value as well as append the input to the list.
The second loop allows the user to input more data if needed, otherwise it returns the data.

The purpose of the empty dictionary was to pair up the initiative scores to their respective character names, for example 'Player1' might have an initiative score of '16' and 'Player2' might have an initiative score of '18'.

After this I used a lambda function to get each character's initiative score and sort them into descending order as during a game of d&d the highest initiative scoring player goes first and the rest follow in descending order.
Finally I used a for loop to print the character names and their respective initiative scores using f strings.
