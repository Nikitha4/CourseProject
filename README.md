# Messenger Text Search

## Overview of the function of the Code
The code allows for user to find out what participant in messenger text history is ranked highest for a specific query. This can give users a sense of what particiapnt would be most likely to say a certain phrase. Queries can be one more words long.

## How the software is implemeneted

### Rankings
This function return a dictionary with the participant as the key and the count of how many times they said the query as the value. This helpful to rank what participant has said the query most often and therefore what participant is most likely to say the query.

### Search Engine
This function finds the query in the messages and outputs all the messages that include the query in it/

### Main
This is the driver function. This function is what prompts the user to specify the file that has the messenger text data and prompts the user to enter what query they would like to search for. With the inputs from the user, this function processes the messenger text data and outputs the result of the rankings on all the participants in the messenger text data based on how often they said the query.

## Usage of the software
In order to use this software, all the user needs to do is upload a json file of the messenger data, which can be directly downloaded from facebook, and follow the prompts outputted by the software. The software is all run by project.py
 
## Brief description of contribution of each team member
Every team member contributed to developing the code, we worked on the software together. Nikitha worked on the documentation. Ishan and Moksh worked on the presentation. All team member looked over each other's work and critiqued each other.
