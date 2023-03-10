from matplotlib import pyplot as plt


from io import BytesIO
import sys

# List of states with each containing a its own set with in the list containing the name of the state, its capital,
# population, state flower name, and image
states_and_capitals = [(["Alabama", "Montgomery", 4887681, "Camellia",
"https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/large/public/camellia-flower.jpg?itok=Q7a-_pZN"]),
(["Alaska", "Juneau", 735_139, "Alpine Forget-me-not",
"https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__"
"medium/public/primary-images/Alpineforgetmenot.jpg?itok=VxF44TUl"]),
(["Arizona", "Phoenix",	7_158_024 , "Saguaro Cactus Blossom",
 "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/"
 "saguaroflowersFlickr.jpg?itok=DxWnZav5"]),
(["Arkansas", "Little Rock", 3_009_733 , "Apple Blossom", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/"
 "styles/symbol_thumbnail__medium/public/primary-images/AppletreeblossomArkansasflower.JPG?itok=HRX6pZyN"]),
(["California", "Sacramento", 39_461_588, "California Poppy", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/"
"styles/symbol_thumbnail__medium/public/primary-images/CAflowerCaliforniaPoppy.jpg?itok=62onOuJf"]),
(["Colorado", "Denver",5_691_287, "Rocky Mountain Columbine", "https://statesymbolsusa.org/sites/statesymbolsusa.org/"
"files/styles/symbol_thumbnail__medium/public/Colorado_columbine2.jpg?itok=3bfYnk5Y"])]


# Function used by selection 1 to display all the states within the list state_and_capitals name, capital, population
# state flowers and images of the flowers.
def display_all_states():

    for i in range(0,6):
        print ("State: ", states_and_capitals[i][0],
               "\tCapital: ", states_and_capitals[i][1],
               "\tPopulation: ", states_and_capitals[i][2],
               "\tState Flower: ", states_and_capitals[i][3])
        print("")

def search_state():

    print("Enter The Name of The State You wish to display the Capital and state flower for")
    state_name = input()
    result = state_name.title()

    for i in range(0,6):
        if result == (states_and_capitals[i][0]):
            response = requests.get(states_and_capitals[i][4])
            images = Image.open(BytesIO(response.content))
            print ("State: ", states_and_capitals[i][0], "\tCapital: ", states_and_capitals[i][1],"\tPopulation: ",
                   states_and_capitals[i][2], "\tState Flower: ", states_and_capitals[i][3])
            images.show()
    print("")


def displays_top_five_populated_states():
    # loop wish has a range from zero to the entire of length of the states_and_capitals list
    # This loops through the list of states and displays within a graph 5 states that have the heighst population
    for i in range(0, len(states_and_capitals)):
        fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
        axs[0].bar(states_and_capitals[i][0], states_and_capitals[i][2])
        fig.suptitle('Categorical Plotting')







while 1:

    print("1. Display All U.S. States in Alphabetical Order Along With The Capital, State, Population, and Flower")

    print("3. Provide a Bar graph of the top 5 populated States showing their overall population.")

    print("4. Update the overall state population for a specific state.")

    print("5. Exit the program")
    selection = input()

    if selection == "1":
        display_all_states()

    elif selection == "2":
        search_state()

    elif selection == "3":
        displays_top_five_populated_states()

    elif selection == "5":
        print("WE ARE SAD TO SEE YOU GO", "\nCOME BACK AGAIN TO LEARN MORE ABOUT OUR STATES")
        break