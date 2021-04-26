import subprocess
import inquirer
import re

# commands
create_list = "adb shell pm list packages > ~/package_list.txt"
package_list = "adb shell pm list packages"
remove = "adb shell pm uninstall --user 0 "  # Space needed at the end. -k: Keep data and cache directories after package removal.
adb_shell = "adb shell"
search_command = "adb shell pm list packages "  # Space needed at the end.
text_append = " > ~/package_list.txt"  # Space needed in front.


def remove_packs(list_file):  # CREATE TEXT FILE:
    with open('package_list.txt', 'w+'):
        subprocess.call(list_file, shell=True)

    with open('package_list.txt', 'r') as f:  # READ TEXT FILE:
        lines = f.readlines()

    items = []  # CLEANUP STRINGS AND GET LIST OF PACKAGES
    for i in lines:
        the_list = i.split(":")
        items.append(the_list[1].replace("\n", ""))

    if len(items) == 0:
        print("\n***Nothing found")
    else:
        print("### TOTAL PACKAGES:", len(items))

    package_object = [
        inquirer.Checkbox('packages_name',
                          message="Select the packages you would like to remove with the space bar",
                          choices=items,
                          ),
    ]
    package_selections = inquirer.prompt(package_object)
    packs_for_removal = package_selections.get('packages_name')
    i = 0 #Probably don't need it

    # This is just confirmation that at least one package has been selected:
    if len(packs_for_removal) == 0:
        print("\n***No selection: back to menu...\n")
    elif packs_for_removal:
        selection = input("\n***Are you sure you want to remove these package(s)? y/N: ").lower()
        if selection == "y":
            while i < len(packs_for_removal):
                print("Removing package: ", i, ":", packs_for_removal[i], "...")
                subprocess.call(remove + packs_for_removal[i], shell=True)
                i += 1
        elif selection == "n":
            print("\n***Nothing to remove, back to menu...\n")
        elif selection != "y" or selection != "n":
            print("\n***Bad input, only 'y' or 'n'.\n")
    #return items


print("### Package Remover Interface for adb ###")
results = 0
while results != 4:
    choose = [
        inquirer.List('menu',
                      message="Please, choose an option",
                      choices=[('List all packages and select for removal', '1'), ('Search packages by keyword', '2'),
                               ('Spawn adb shell', '3'), ('Exit', '4')],
                      ),
    ]
    choice = inquirer.prompt(choose)
    results = choice['menu'][0]  # Option selected by user

    if results == "1":
        remove_packs(create_list)

    elif results == "2":
        search_filter = input("Search any part of the package hierarchy:").lower()
        while True:
            if not re.match("^[A-Za-z0-9_]*$", search_filter):
                print("\n***Only alphanumeric and underscore characters!\n")
                break
            elif not search_filter:
                print("\n***Please search for something.\n")
                break
            else:
                triumvirate = search_command + search_filter + text_append
                remove_packs(triumvirate)
                break

    elif results == "3":
        subprocess.call(adb_shell, shell=True)

    elif results == "4":
        print("Bye!")
        break
