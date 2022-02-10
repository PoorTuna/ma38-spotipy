from consolemenu import *
from consolemenu.items import *

from Spotipy.spotipy import Spotipy


def spotipy_console():
    # Main Menu:
    my_spotipy = Spotipy()

    # Related menu functions
    def login_input():
        username = input("Enter a username : ")
        password = input("Enter a password : ")

        my_spotipy.user_manager.login(username, password)

    def signup_input():
        username = input("Enter a username : ")
        password = input("Enter a password : ")

        my_spotipy.user_manager.signup(username, password)

    menu = ConsoleMenu("Spotipy", "Main Menu")

    func_item = FunctionItem("Running a command", input, ["Enter an input"])

    selection_menu = SelectionMenu(["1 M", "2 M ", "3 M"])

    # Login Menu:

    login_menu = FunctionItem("Sign In", login_input)

    # Register Menu:
    register_menu = FunctionItem("Sign Up", signup_input)

    # Logout Menu:

    logout_menu = FunctionItem("Log Out", my_spotipy.user_manager.sign_out)

    # Menu init :
    menu.append_item(login_menu)
    menu.append_item(register_menu)
    menu.append_item(logout_menu)

    menu.show()


spotipy_console()
