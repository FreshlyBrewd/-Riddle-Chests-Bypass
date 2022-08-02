"""
Python riddle chest lookup tool
Created by FreshlyBrewed#6362
"""
#Imports
import os
import glob

#Variables
back_check = ['Back', 'B', 'back', 'b']
yes_check = ['Yes', 'Y', 'yes', 'y']
no_check = ['No', 'N', 'no', 'n']
removal_list = ['{"category":"riddlechests:betrayal_at_krondor","lang":"en_us",', ',"type":"riddlechests:word"}']
confirm_checks = True

#Functions
def search_function():
    while True:
        clearConsole()
        print("Input riddle keywords. This can be the starting letters or riddle itself.")
        solver_command = input(" : ").lower()
        clearConsole()
        #Finds the line and prints it of where the answer is.
        # string to search in file
        with open("riddle_data.txt", 'r') as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                # check if string present on a current line
                if line.find(solver_command) != -1:
                    print("\nMatch: " + solver_command + "." + "\n")
                    print(line)
        confirm_alert()
        break
    fp.close()
    
def manual_update():
    clearConsole()
    print("Type the starting characters on a chest. (When you first open it)")
    manual_update_command_start = input(" : ")
    clearConsole()
    print("\n Type the full riddle.")
    manual_update_command_riddle = input(" : ")
    clearConsole()
    print("\n Type the solution.")
    manual_update_command_solution = input(" : ")
    clearConsole()

    #combines the data together
    riddle_data = ('"original":"'+ manual_update_command_start +'","riddle":["'+ manual_update_command_riddle +'"],"solution":"'+ manual_update_command_solution +'"')
    complete_riddle_data = riddle_data.lower()
    #Confirm if they want to append data
    print("Input Data: " + complete_riddle_data)
    print('\n Are you sure that you want to append? Y | N')
    user_confirmation = input(" : ")
    if user_confirmation in yes_check:
        file = open('riddle_data.txt', 'a')
        file.write(str(complete_riddle_data)+"\n")
        file.close()
        clearConsole()
        print("\nManual Update Completed\n")
        confirm_alert()
    else:
        print("\nAction Aborted\n")
        confirm_alert()
        return

def automatic_update():
    clearConsole()
    print("Warning this Automatic update will overwrite all of the answers. If you wish to keep this current list and add more please use the manual command.\n")
    confirm_alert()
    print("Path to .json files")
    #Gets the programs cwd and saves it for later
    program_working_directory = os.getcwd()
    add_command_path = input(" : ")
    #Backs out if user wants too
    if add_command_path in back_check:
        return
                        
    #Checks if directory is valid
    existance_check = os.path.exists(add_command_path)
                        
    #Changes Directory
    if existance_check == True:
        #Checks if there are actually any .json files in the cwd
        file_name_list = glob.glob1(add_command_path,"*.json")
        json_ammount = len(file_name_list)
        if json_ammount >= 1:
            #Wipes the old file
            try:
                os.remove("riddle_data.txt")
            except:
                print("\nNo file present creating new one.\n")
            os.chdir(add_command_path)
            #Dumps contents into .txt3
            for file in file_name_list:
                with open(file, 'r') as f:
                    file_content = f.read()
                    #Makes it lowercase
                    file_content = file_content.lower()
                    #Makes removes certain junk
                    for word in removal_list:
                        file_content = file_content.replace(word, "")
                    f.close()
                    #Creates a new .txt file if there isnt one already.
                    file = open('riddle_data.txt', 'a')
                    file.write(str(file_content)+"\n")
                    file.close()
            file.close()
            #Changes back the directory so everything is back to normal.
            os.chdir(program_working_directory)
            os.rename(add_command_path + "\\riddle_data.txt", program_working_directory + "\\riddle_data.txt")
            clearConsole()
            print("Automatic Update Complete \n")
            confirm_alert()
        else:
            no_usable_file_types()
                    
                    
                            
            return
                        
    else:
        invalid_directory()

def confirm_alert():
    if confirm_checks:
        confirm_check_input = input("___")

def clearConsole():
    os.system("cls")

def wrong_input():
    print(" \n Error: Wrong input \n ")
    confirm_alert()

def invalid_directory():
    print(" \n Error: Invalid Directory\n ")
    confirm_alert()

def no_usable_file_types():
    print(" \n Error: No Usable File Types \n ")
    confirm_alert()

def answer_not_found():
    print(" \n Error: Answer Not Found \n ")
    confirm_alert()
    
#Main Loop
print("Riddle Chest Solver v0.1")
while True:
    clearConsole()
    print("\nCommands: \n 1. 'Help' 'H' \n 2. 'Solve' 'S' \n 3. 'Update' 'U' \n 4. 'Quit' 'Q'")
    main_command = input(" : ")
    if main_command in ['Help', "H", "help", "h", "1"]:
        print("Its very simple I'm tired so im not gonna spend my time writing a help function.")
        confirm_alert()
    elif main_command in ['Solve', "S", "solve", "s", "2"]:
        search_function()   
    elif main_command in ['Update', "U", "update", "u", "3"]:
        while True:
            clearConsole()
            print("\nUpdate Commands: \n 1. 'Add' 'A' \n 2. 'Remove' 'R' \n 3. 'View' 'V' \n 4. 'Back' 'B'")
            update_command = input(" : ")

            if update_command in ['Add', 'A', 'add', 'a', '1']:
                clearConsole()
                while True:
                    clearConsole()
                    print("Add Commands: \n 1. 'Manual' 'M' \n 2. 'Automatic' 'A' \n 3. 'Back' 'B'")
                    add_command = input(" : ")
                    if add_command in ['Manual', 'M', 'manual', 'm', '1']:
                        clearConsole()
                        manual_update()
                        
                    elif add_command in['Automatic', 'A', 'automatic', 'a', '2']:
                        clearConsole()
                        automatic_update()
                        
                    elif add_command in ["Back", "B", "back", "b", "3"]:
                        break
                    else:
                        wrong_input()
                
            elif update_command in ['Remove', 'R', 'remove', 'r', '2']:
                print("\nIm too lazy to program this feature so just do add instead and automatic. It will wipe the file and create a whole new database.\n")
                confirm_alert()
            elif update_command in ['View', 'V', 'view', 'v', '3']:
                #Opens .txt in another window
                os.startfile("riddle_data.txt")
            elif update_command in ['Back', 'B', 'back', 'b', '4']:
                break
            else:
                wrong_input()
    elif main_command in ['\nQuit', 'Q', 'quit', 'q', '4']:
        quit()
    else:
        wrong_input()
