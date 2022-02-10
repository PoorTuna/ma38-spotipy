from consolemenu import *
from consolemenu.items import *

from Spotipy.spotipy import Spotipy


def login_input():
    username = input("Enter a username : ")
    password = input("Enter a password : ")

    return [username, password]


def spotipy_console():
    # Main Menu:
    my_spotipy = Spotipy()
    menu = ConsoleMenu("Spotipy", "Main Menu")

    # menu_item = MenuItem("menu item test")
    func_item = FunctionItem("Running a command", input, ["Enter an input"])
    # command_item = CommandItem("Run a console command", "color a")

    selection_menu = SelectionMenu(["1 M", "2 M ", "3 M"])

    # Login Menu:

    login_menu = FunctionItem("Sign In", login_input)

    register_menu = SubmenuItem("Sign Up", selection_menu, menu)

    menu.append_item(login_menu)
    menu.append_item(register_menu)

    menu.show()


spotipy_console()
