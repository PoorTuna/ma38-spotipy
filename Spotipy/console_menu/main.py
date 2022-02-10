from consolemenu import *
from consolemenu.items import *


def spotipy_console():
    # Create a menu
    menu = ConsoleMenu("Spotipy", "Main Menu")

    menu_item = MenuItem("menu item test")
    func_item = FunctionItem("Running a command", input, ["Enter an input"])
    command_item = CommandItem("Run a console command", "color a")

    selection_menu = SelectionMenu(["1 M", "2 M ", "3 M"])

    submenu_menu = SubmenuItem("Submenu spotipy", selection_menu, menu)

    menu.append_item(menu_item)
    menu.append_item(func_item)
    menu.append_item(command_item)
    menu.append_item(submenu_menu)

    menu.show()


spotipy_console()
