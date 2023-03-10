# import modules used by application
from matplotlib import pyplot as plt
from PIL import Image
from io import BytesIO
import seaborn as sns
import requests

# List of states with each containing its own set with in the state name, capital,population, state flower, and image
states = (['Alabama', 'Montgomery', 4_918_689, 'Camellia',
           "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/large/"
           "public/camellia-flower.jpg?itok=Q7a-_pZN"],
          ['Alaska', 'Juneau', 727_951, 'Alpine Forget-me-not',
           'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/'
           'public/primary-images/Alpineforgetmenot.jpg?itok=VxF44TUl'],
          ['Arizona', 'Phoenix', 7_399_410, 'Saguaro Cactus Blossom',
           'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public'
           '/saguaroflowersFlickr.jpg?itok=DxWnZav5'],
          ['Arkansas', 'Little Rock', 3_025_875, 'Apple Blossom',
           'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public'
           '/primary-images/AppletreeblossomArkansasflower.JPG?itok=HRX6pZyN'],
          ['California', 'Sacramento', 39_562_858, 'California Poppy',
           'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/' 
           'public/primary-images/CAflowerCaliforniaPoppy.jpg?itok=62onOuJf'],
          ['Colorado', 'Denver', 5_826_185, 'Rocky Mountain Columbine',
           'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/'
           'public/primary-images/Mountain-Laural-flowers2.jpg?itok=b7tlfk4G'],
          ['Connecticut', 'Hartford', 3_559_054, 'Mountain Laurel',
           'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles'
           '/symbol_thumbnail__medium/public/primary-images/Mountain-Laural-flowers2.jpg?itok=b7tlfk4G'])


# Function used to display all the states within the state_and_capitals name, capital, population, state flowers
def display_all_states():

    # iterates through array and displays each states contents within each set by its element location within the set
    for i in range(len(states)):
        print(f'State: {states[i][0]}',
              f'\nCapital: {states[i][1]}',
              f'\nPopulation: {states[i][2]}',
              f'\nState Flower: {states[i][3]}')
        print("")


# Functions used to search for a specific state and display all the contents in set including image of state flower
def search_states():

    # message to user to enter the state name of the state info they want to display
    print("Enter The Name of The State You wish to display the Capital and state flower for")
    state_name = input().title()  # Capitalizes the first letter of the input to ensure match with name in array

    # loop iterates through states array and if the name matches the state set contents are displayed
    for i in range(len(states)):
        if state_name == (states[i][0]):
            response = requests.get(states[i][4])
            images = Image.open(BytesIO(response.content))
            print("State Name: ", states[i][0],
                  "\tState Capital: ", states[i][1],
                  f'\t{states[i][0]} Population: ', states[i][2],
                  f'\t{states[i][0]} State Flower: ', states[i][3],
                  images.show())
            break

        else:
            print('Try Again, Invalid Input!')
            search_states()
    print("")


# function which populates a bar graph with the 5 most populated states within the array
def displays_top_five_populated_states():
    x = []
    y = []

    # for loop iterates 5 times and takes in the values for name and population of the one with the highest population
    for i in range(0, 5):
        population_max = max(states[i][2])
        state_name = states[i][0]
        x.append(state_name)
        y.append(population_max)

    fig = plt.figure(figsize=(10, 5))
    plt.bar(x, y, color="blue", width=0.4)
    sns.set(font_scale=1.5)
    plt.xlabel('Population', labelpad=12)  # x
    plt.ylabel('State', labelpad=12)
    plt.title('State Populations', y=1.015, fontsize=22)
    plt.show()


while True:

    print("1. Display All U.S. States in Alphabetical Order Along With The Capital, State, Population, and Flower")

    print("2. Search for a specific state and display the appropriate Capital name, \
            State Population, and an image of the associated State Flower.")

    print("3. Provide a Bar graph of the top 5 populated States showing their overall population.")

    print("4. Update the overall state population for a specific state.")

    print("5. Exit the program")
    selection = int(input())

    if selection == 1:
        display_all_states()

    elif selection == 2:
        search_states()

    elif selection == 3:
        displays_top_five_populated_states()

    elif selection == '4':
        print("Come back for more state information")
        break

    else:
        print("Invalid Input!", "\nEnter a number based on selection in menu")

