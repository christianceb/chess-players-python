from app.Parser import Parser
from app.Player import Player
from app.mergesort import merge_sort
from app.search import *


def initialise(filepath):
    """
    Initialises program to encapsulate processing of csv file
    :param filepath: File path to valid csv file containing valid data
    :return: List of chess players in Players object
    """
    csv = Parser(filepath)
    players = []

    # Create Player objects from CSV
    for player in csv.list:
        players.append(Player(player[0], player[1], player[2], player[3], player[4], player[5]))

    # Sort Player objects
    return merge_sort(players)


def search(list, keywords):
    """
    Run search routine given keyword to find in list. Also runs routine for results

    :param list: List of Players to search to
    :param keywords: Keywords to use in search
    :return: Nothing
    """
    found = player_bs_l(players, keywords)

    if found:
        found.print()
    else:
        print("\nChess player not found!")


def prompt(list):
    """
    Run routine to prompt user
    :param list: List of Players to search to
    :return: Nothing
    """

    # Prompt user last name to find
    name = input("Enter last name to find: ")
    search(list, name)


players = initialise("app/chess-players.csv")

if players:
    # Set flag that program is running.
    run = True

    # Keep running this program as long as this is true
    while run:
        prompt(players)

        # Awesome code gymnastics where if we get Y/y, rerun prompt()
        run = True if input("\nAnother search? ('y' to continue, otherwise exits): ").lower() == "y" else False
else:
    print("List is empty (could be because target CSV file is really empty or not found)")