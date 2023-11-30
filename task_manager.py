
import datetime

def credentials_check(username, password):

    # Create two empty lists to store usernames and passwords while checking credentials
    usernames = []
    passwords = []

    # Open the user.txt file in read mode
    with open("user.txt", "r") as user_file:

        # For each line in the file, strip away the '\n' and split the string into a list
        for lines in user_file:
            temp = lines.strip()
            temp = temp.split(", ")
            # Add the usernames and passwords in the file to the 'usernames' and 'passwords' lists
            usernames.append(temp[0])
            passwords.append(temp[1])

        # Check if the username entered is in the usernames list
        if username in usernames:
            # If so, if the password entered is the same as the password in the passwords list thats at the same index, return True
            if password == passwords[usernames.index(username)]:
                return True
            # Else, print error message and return False
            else:
                print("Oops! That password doesn't match. Please start again.")
                return False
        # Else, print an error message and return False
        else:
            print("Oops! That username doesn't exist. Please try again.")
            return False


def login():

    while True:
        # Ask the user for their login details
        print("Login:\n")
        username = input("Username: ").lower()
        password = input("Password: ")

        # If the credentials check is True, break from the loop
        if credentials_check(username, password) == True:
            break
    # Print a new line and return the username value for later use
    print("\n")
    return username


def menu_choice(current_user):

    # Check if user is admin or not and present the relevent menu options
    if current_user == 'admin':
        # If user is admin, present the full menu and convert the users input to lower case
        menu = input('''Select one of the following options below:
r  - Register a User
a  - Add a Task
va - View All Tasks
vm - View / Edit My Tasks
s  - Show Statistics
gr - Generate Reports
e  - Exit
: ''').lower()
    
    else:
        # Else, present the limited menu and convert the users input to lower case
        menu = input('''Select one of the following options below:
a  - Add a Task
va - View All Tasks
vm - View / Edit My Tasks
gr - Generate Reports
e  - Exit
: ''').lower()
    # Return the users input value for later use
    return menu


def does_username_exist(new_username):

    # Create an empty list called usernames
    usernames = []

    # Open the User file
    with open("user.txt", "r") as user_file:
        # For each line in the file, remove whitespace and split the line into a list of words or phrases
        for lines in user_file:
            temp = lines.strip()
            temp = temp.split(", ")
            #Append the first word in the line to the list called usernames
            usernames.append(temp[0])
        if new_username in usernames:
            # If the username being checked is in the list usernames
            return True
        else:
            # Else, return false
            return False


def register_user():
            
            # Print a new line
            print("\n")

            while True:
                # Ask for new username
                new_username = input("Please enter the username for the new account: ")
                # Check its at least 1 character long
                if len(new_username) >= 1:
                    # If the username doesnt already exist, break from the loop
                    if does_username_exist(new_username) == False:
                        break
                    else:
                        # Else, print an error message
                        print("\nThat user already exists!\n")
                else:
                    # Else, print an error message
                    print("\nYou must enter a username with a length of at least 1 character.\n")
            
            while True:
                while True:
                    # Ask for new password and check its at least one character long
                    new_password1 = input("Please enter the password you would like to use for the account: ")

                    # Check that the password enetered is at least 1 character long
                    if len(new_password1) >= 1:
                        break
                    else:
                        print("\nPlease enter a password with a length of at least 1 character.\n")

                # Ask for password confirmation and check it matches the new password
                new_password2 = input("Please confirm the password: ")
                if new_password1 == new_password2:
                    break
                else:
                    print("\nThe passwords do not match, please try again.\n")
                
            # Open the user file in append-mode         
            with open("user.txt", "a") as user_file:
                # Write the new username and password on the same line at the end of the file
                user_file.write(f"\n{new_username}, {new_password1}")
                
            # Notify the user that the new user has been added
            print(f"\n{new_username} has been added.\n")


def possible_days_and_months():

    # Create hardcode lists of possible string entries for days and months
    possible_days = []
    possible_months = []
    for i in range(1, 10):
        possible_days.append(f"0{i}")
        possible_months.append(f"0{i}")
    for i in range(10, 32):
        possible_days.append(str(i))
    for i in range(10, 13):
        possible_months.append(str(i))
    return [possible_days, possible_months]


def date_input_error_check(date):
    
    # Create a nested list with possible days and months
    possible_days_months_list = possible_days_and_months()
    
    # Check the length of the input is 8
    if len(date) == 8:
        
        # Check the input is a digit
        if date.isdigit():
            
            # Check if the days entered are possible
            if date[:2] in possible_days_months_list[0]:
                
                # Check if the months entered are possible
                if date[2:4] in possible_days_months_list[1]:
                    
                    # If all the tests are passed, return True, else, print an appropriate error message and return False
                    return True
                
                else:
                    print("\nThe date entered is not possible.\n")
                    return False 
            else:
                print("\nThe date entered is not possible.\n")
                return False       
        else:
            print("\nPlease only enter numbers for the due date.\n")
            return False  
    else:
        print("\nPlease enter a date with exactly 8 numbers.\n")
        return False


def date_format_num_to_word(date): 

    # Create a list of possible months in string format
    str_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Create empty string value
    word_month = ""
    # Convert the date to a string
    date = str(date)
    # Get the integer numerical date
    num_month = int(date[2:4])
    # Loop through a range of the length of the months list
    for i in range(len(str_months)):
        # If number of months is equal to the index number plus one
        if num_month == i + 1:
            # Concatinate the empty string with the str_months value at that index
            word_month += f"{str_months[i]}"
    # Format the new date
    new_date = f"{str(date)[:2]} {word_month} {str(date)[4:9]}"
    # Return the new date value
    return new_date


def dates_format_num_to_word(date1, date2):
    dates = [date1, date2]
    new_dates = []
    # For each input date, format the date and return the value
    for date in dates:
        new_date = date_format_num_to_word(date)
        new_dates.append(new_date)
    return new_dates


def date_format_word_to_num(date):

    # Split the entry date into a list of 3 words
    date = date.split()
    # Create a string of possible entry date months
    str_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    str_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    # For each month in the list, if the month of the entry date is the same as the month in the list:
    for month in str_months:
        if month == date[1]:
            # Change the month of the entry date to the index of the month, plus one
            date[1] = str(str_months.index(month) + 1)
    
    # If the date is in the list str_numbers, add a zero character before it
    if date[1] in str_numbers:
        date[1] = f"0{date[1]}"
    
    # Join the list 'entry date' together again into a string'
    numeric_entry_date = "".join(date)
    return numeric_entry_date


def is_date1_before_date2(date1, date2):
    
    # Check if date 1 is before date 2 using the datetime module
    check_date1 = datetime.datetime(int(date1[4:8]), int(date1[2:4]), int(date1[:2]))
    check_date2 = datetime.datetime(int(date2[4:8]), int(date2[2:4]), int(date2[:2]))
    if check_date1 <= check_date2:
        return True
    else:
        return False


def append_data_to_task_file(task_username, task_title, task_description, new_dates):
    
    # Append the data to the file task.txt in the correct format
    whole_task = f"{task_username}, {task_title}, {task_description}, {new_dates[0]}, {new_dates[1]}, No"
    with open("tasks.txt", "r") as task_file:
        
        lines = task_file.readlines()
        
        if len(lines) > 0:
            # If there are already 1 or more lines, add a newline character before the task
            with open("tasks.txt", "a") as task_file:
                task_file.write(f"\n{whole_task}")
        else:
            # Else, write the task on the first line without a newline character
            with open("tasks.txt", "a") as task_file:
                task_file.write(f"{whole_task}")
    
    # Notify the user that the task has been added
    print(f"\nThe task for {task_username} has been added.\n")


# Add a task to task.txt file
def add_task():
    
    # Print a new line
    print("\n")
    
    while True:
        # Ask for the new username
        task_username = input("Please enter the username of the person whom the task is assigned to: ")
        
        # Check if the new username is in user.txt file
        if does_username_exist(task_username) == True:
            break
        else:
            print("\nOops! That username doesnt exist, please try again.\n")
        
    # Ask for the task title and check the input is at least 1 character long
    while True:
        task_title = input("Please enter the title of the task: ")
        if len(task_title) >= 1:
            break
        else:
            print("\nPlease enter a title with a length of at least 1 character.\n")

    # Ask for the task description and check the input is at least 1 character long
    while True:
        task_description = input("Please enter a description of the task: ")
        if len(task_description) >= 1:
            break
        else:
            print("\nPlease enter a description with a length of at least 1 character.\n")
    
    # Ask for the current date and check for date errors
    while True:
        entry_date = input("Please enter todays date using 8 digits (ddmmyyyy): ")
        if date_input_error_check(entry_date):
            break

    # Ask for the due date of the task and check for errors
    while True:
        task_due_date = input("Please enter the due-date of the task using 8 digits (ddmmyyyy): ")
        if date_input_error_check(task_due_date):
            if is_date1_before_date2(entry_date, task_due_date):
                break

    # Format the numerical dates to 'word' dates
    new_dates = dates_format_num_to_word(entry_date, task_due_date)

    # Append all the data to the task file
    append_data_to_task_file(task_username, task_title, task_description, new_dates)


def view_all():

    # Open tasks.txt in read-mode
    with open("tasks.txt", "r") as task_file:
        
        # Copy the file to variable called lines
        lines = task_file.readlines()
        
        # Check that the file has at least one line
        if len(lines) > 0:
            
            # If so, notify the user that all the lines will be printed
            print("\nPrinting all the tasks: ")

            # Set up a counter variable for the task number
            task_num = 0
            
            # For each line in the file, strip the whitespace and split the line at each instance of ", " 
            for line in lines:
                line = line.strip()
                line = line.split(", ")

                # Increment the counter by 1 and set each item of the list to a readable variable for printing
                task_num += 1
                
                # Set variables for each section
                user_name = line[0]
                task_title = line[1] 
                task_description = line[2]
                date_assigned = line[3]
                due_date = line[4]
                completed_bool = line[5]

                # Print the task in a presentable format
                print(f'''
                Task number {task_num}:
                ---------------------------------------------------------------------
                | Task:             | {task_title}
                | Assigned to:      | {user_name}
                | Date asigned:     | {date_assigned}
                | Due Date:         | {due_date}
                | Task Complete?    | {completed_bool}
                | Task description: | {task_description}
                ----------------------------------------------------------------------''')
            
            print("\nAll the tasks have been printed.\n")
        
        else: 
            print("\nThere are no tasks in the task file.\n")


def check_for_zero_tasks(current_user):
    
    # Open the tasks.txt file in read-mode
    with open("tasks.txt", "r") as task_file:
        # Set up counter variales to count up the number of tasks and user tasks
        number_of_user_tasks = 0
        total_numer_of_tasks = 0
        
        # Count up the number of loops to check if the user has zero tasks
        for lines in task_file:
            # For each line in the file, strip the whitespace and split the line at each instance of ", "
            total_numer_of_tasks += 1
            temp = lines.strip()
            temp = temp.split(", ")
            
            # If the username in the txt file is the same as the username entered to login;
            if temp[0] == current_user:
                # increment the counter variable by 1
                number_of_user_tasks += 1

    # If the couter variable is zero, print message diplaying zero tasks and return to main menu
    if number_of_user_tasks == 0:
        print("\nYou dont have any tasks yet.\n")
        return True
        
    # Else print all tasks for the current user
    else:
        print("\nPrinting your tasks:\n")
        return False


def print_user_tasks(current_user):
    
    # Open tasks.txt in read-mode
    with open("tasks.txt", "r") as task_file:
        
        # Set up a counter variable for the task number
        task_num = 0

        # For each line in the file, strip the whitespace and split the line at each instance of ", "
        for lines in task_file:
            temp = lines.strip()
            temp = temp.split(", ")
            
            # If the username in the txt file is the same as the username entered to login;
            if temp[0] == current_user:
                
                # Increment the counter variable by 1
                task_num += 1
                
                # Create readable variables for printing the outputs
                task_title = temp[1] 
                task_description = temp[2]
                date_assigned = temp[3]
                due_date = temp[4]
                completed_bool = temp[5]
                
                # Print the tasks in a presentable format
                print(f'''
                Task number {task_num}:
                ---------------------------------------------------------------------
                | Task:             | {task_title}
                | Date asigned:     | {date_assigned}
                | Due Date:         | {due_date}
                | Task Complete?    | {completed_bool}
                | Task description: | {task_description}
                ----------------------------------------------------------------------''')
        return task_num


def mark_task_complete(task_num_to_edit):
    
    # Open the task file in read mode
    with open("tasks.txt", "r") as task_file:
       
        # Copy the task file into a list of lines
        lines = task_file.readlines()
        # Create a variable for the line being edited
        line = lines[task_num_to_edit - 1]
        # Split the line into sections
        words = line.split(", ")
        # Change the value in the 'completed' section to "Yes"
        words[5] = "Yes"
        # Join the sections together again
        new_line = ", ".join(words)
        # Turn the old line into the new line with the new "Yes" variable
        lines[task_num_to_edit -1] = new_line + "\n"
        # Join all the lines together to make a new file
        new_file = "".join(lines)
    
    # Open the task file in write mode
    with open("tasks.txt", 'w') as task_file:
        
        # Write the new file in the task file
        task_file.write(new_file)
    
    # Notify the user that the test has been marked as complete
    print("\nTest marked as complete.\n")


def edit_username(task_num_to_edit):
    
    while True:
        # Ask for the new username
        new_username = input("What should the new username be? ").lower()
        
        # If new username doesnt exist already print error and loop to the question again
        if does_username_exist(new_username) == False:
            print("\nThat username doesnt exist. Please only change the username to one that already exists.\n")
        else:
            break
    
    # Open the task file in read mode
    with open("tasks.txt", "r") as task_file:
        
        # Copy the task file into a list of lines
        lines = task_file.readlines()
        
        # Create a variable for the line being edited
        line = lines[task_num_to_edit - 1]
        # Split the line into sections
        words = line.split(", ")
        # Change the value of the data in the first section to the new username
        words[0] = new_username
        # Join the sections together again
        new_line = ", ".join(words)
        # Turn the old line into the new line with the new username variable
        lines[task_num_to_edit -1] = new_line
        # Join the lines to create a new file
        new_file = "".join(lines)
    
    # Open the task file in write mode
    with open("tasks.txt", 'w') as task_file:

        # Write the new file to the task file
        task_file.write(new_file)

    # Notify the user that the username has been updated
    print("\nUsername updated.\n")


def edit_task(task_num_to_edit):
    
    while True:
        # Ask for the new username and task description
        new_task_title = input("What is the new title? ")
        new_task_description = input("What is the new description? ")
        
        # Check if the new title and description are both at least 1 character long
        if len(new_task_title) >= 1 and len(new_task_description) >= 1:
            break
        else:
            print("\nThe title and description must both have 1 or more characters.\n")
    
    # Open the task file in read mode
    with open("tasks.txt", "r") as task_file:
        
        # Copy the task file into a list of lines
        lines = task_file.readlines()
        
        # Create a variable for the line being edited
        line = lines[task_num_to_edit - 1]
        # Split the line into a list of words
        words = line.split(", ")
        # Change the value of the word at index 1 to the new title
        words[1] = new_task_title
        # Change the value of the word at index 2 to the new description        
        words[2] = new_task_description
        # join the list together to make a new line
        new_line = ", ".join(words)
        # Change the line in the file-copy to the newly created line
        lines[task_num_to_edit -1] = new_line
        # join the list of lines together to make a new file
        new_file = "".join(lines)
    
    # Open the file in write mode and write in the new file
    with open("tasks.txt", 'w') as task_file:
        
        # Write the new file to the task file
        task_file.write(new_file)
    
    # Notify the user that the task has been edited
    print("\nTask has been edited.\n")


def which_task_to_edit(input_task_to_edit):
    
    # Convert the input to an int data type
    input_task_to_edit = int(input_task_to_edit)
    # Set up counter variales to count up the number of tasks and user tasks
    non_user_task_counter = 0
    user_task_counter = 0
    task_to_edit = 0
    
    # Work out which task to edit. Open the task file in read mode
    with open("tasks.txt", "r") as task_file:
        
        # for each line in the file
        for lines in task_file:
            
            # Work out the username
            temp = lines.strip()
            temp = temp.split(", ")
            
            # If the username in that line of the file is the same as the username entered to login;
            # And if the user task counter is less than the task number the user wants to edit;
            if temp[0] == current_user and user_task_counter < input_task_to_edit:
                # Increment the user task counter variable by 1
                user_task_counter += 1
            
            # Else if th username in that line of the file is not the same as the username entered to login;
            # And if the user task counter is tess than the task number the user wants to edit;
            elif temp[0]!= current_user and user_task_counter < input_task_to_edit:
                # Increment the non-user task counter variable by 1
                non_user_task_counter += 1
    
    # The task to edit is the value of the non-user task counter plus the value of the user task counter
    task_to_edit = non_user_task_counter + user_task_counter
    return task_to_edit


def is_task_complete(task_number):
    
    # Open the task file
    with open("tasks.txt", "r") as task_file:
    
        # Read the file to a variable called lines
        lines = task_file.readlines()
        
        # Create a variable for the line being edited
        line_to_edit = lines[task_number - 1]
        # Remove whitespace from the end of the line
        line_to_edit = line_to_edit.strip()
        # Split the line into a list of words
        words = line_to_edit.split(", ")
        # Store the 'completed' value in a variable
        word = words[5]
    
    # If the word at that location is "Yes", return True, else, return False
    if word.lower() == 'yes':
        return True
    else:
        return False


def update_due_date(task_num_to_edit):

    while True:
        # Ask for the new due date and check for input errors
        new_due_date = input("Please enter the new due date in 8 digit format (ddmmyyyy): ")
        if date_input_error_check(new_due_date):

            # Open the task file and check if the entry date of the task is before the new due date
            with open("tasks.txt", "r") as task_file:
                # Read the file to a variable called lines
                lines = task_file.readlines()
                # Create a variable for the line being edited
                line_to_edit = lines[task_num_to_edit - 1]
                # Split the line into a list of words
                words = line_to_edit.split(", ")
                # Store the entry date in a variable
                entry_date = words[3]
                # Change the date to numerical form
                numeric_entry_date = date_format_word_to_num(entry_date)
                # Check if new due date is after numeric entry date
                if is_date1_before_date2(numeric_entry_date, new_due_date):
                    break
                else:
                    print("\nYou cannot set a due date in the past\n")

    # Change the due month from numeric to word
    new_due_date = date_format_num_to_word(new_due_date)   
   
   # Change the due date. Open the task file in read mode
    with open("tasks.txt", "r") as task_file:
        
        # Copy the task file into a list of lines
        lines = task_file.readlines()
        
        # Create a variable for the line being edited
        line = lines[task_num_to_edit - 1]
        line = line.strip()
        # Split the line into a list of words
        words = line.split(", ")
        # Change the value of the word at index 1 to the new due date
        words[4] = new_due_date
        # join the list together to make a new line
        new_line = ", ".join(words)
        # Change the line in the file-copy to the newly created line
        lines[task_num_to_edit -1] = new_line + "\n"
        # join the list of lines together to make a new file
        new_file = "".join(lines)
    
    # open the file in write mode and write in the new file
    with open("tasks.txt", 'w') as task_file:
        task_file.write(new_file)
    
    # Notify the user that the due date has been updated
    print("\nDue date has been updated\n")


def view_mine(current_user):
    
    # If the user has more than zero tasks:
    if check_for_zero_tasks(current_user) == False:
        
        # Print the users tasks and store the counter variable for later use
        counter = print_user_tasks(current_user)
        print("\n")
        
        while True:
            # Ask for a number of a task or -1 to exit
            input_task_to_edit = input("Access your incomplete tasks by entering the task number (or enter -1 to save and return to the main menu).\n: ")
            
            # Check if the input is a digit or "-1":
            if input_task_to_edit.isdigit() or input_task_to_edit == "-1":
                
                # If the user enters -1, break from the loop
                if input_task_to_edit == "-1":
                    print("\nMain menu:\n")
                    break

                # Else if the number entered is a task number:
                elif int(input_task_to_edit) <= counter and int(input_task_to_edit) > 0:
                    
                    # Work out which task to edit
                    task_to_edit = which_task_to_edit(input_task_to_edit)
                    
                    # Check if the task is complete or not
                    if is_task_complete(task_to_edit) == False:
                        
                        # If not, ask if the user wants to mark the test complete or edit the task 
                        option1 = input('''\nSelect one of the following options below:
mc  - Mark the task complete
et  - Edit the task
m   - Return to main menu
: ''').lower()
                                    
                        # If they want to mark the test complete, mark the test complete
                        if option1 == 'mc':
                           mark_task_complete(task_to_edit)
                        
                        # Else, if the user want to edit the task
                        elif option1 == 'et':
                            
                            # Ask which section the user wants to edit
                            option2 = input('''\nWhich section would you like to edit?
u  - Username the task is assigned to
td - Task Title and Description
d  - Due date of the task
m  - Return to the main menu
: ''').lower()
                                    
                            # If the user wants to edit the username
                            if option2 == 'u':
                                edit_username(task_to_edit)
                                
                            
                            # Else if the user wants to edit the due date
                            elif option2 == 'd':
                                update_due_date(task_to_edit)

                            # Else if the user wants to edit the totle and description
                            elif option2 == 'td':
                                edit_task(task_to_edit)

                            # Else if the user wants to go back to the main menu
                            elif option2 == 'm':
                                print("\nMain menu:\n")
                                break
                            
                            # Else print an error and loop to the questio again
                            else:
                                print("\nThat was not an option, please start again.\n")

                        # Else if the user wants to go back to the main menu
                        elif option1 == 'm':
                            print("\nMain menu:\n")
                            break

                        # Else print an error and loop to the question again
                        else:
                            print("\nThat was not an option, please start again.\n")
                    
                    # Else print an error and loop to the question again
                    else:
                        print("\nThat task is completed. You cannot edit tasks that have been completed.\n")
                
                # Else print an error and loop to the question again
                else:
                    print("\nYou dont have that mant tasks.\n")            
            
            # Else print an error and loop to the question again
            else:
                print("\nThat was not a valid task number, please start again.\n")


def generate_reports():

    while True:
        # Ask for todays date and check for date input errors
        todays_date = input("\nTo generate reports, please enter todays date using 8 digits (ddmmyyyy): ")
        if date_input_error_check(todays_date):
            break
    
    # Set up counter variables
    total_tasks = 0
    complete_tasks = 0
    incomplete_overdue_tasks = 0
    
    # Open the task file:
    with open("tasks.txt", "r") as task_file:

        # Create a copy of the file
        task_lines = task_file.readlines()

        # For each line in the task file copy
        for line in task_lines:
            
            # Increment the total tasks value by 1
            total_tasks += 1
            
            # Split the line up into sections
            temp = line.strip()
            temp = temp.split(", ")
            
            # Format the due date from words to numbers
            num_due_date = date_format_word_to_num(temp[4])

            # If the 'completed' section is "Yes", increment the complete tasks value by 1
            if temp[5] == "Yes":
                complete_tasks += 1
            
            # else if it is incomplete, and the due date is before todays date
            elif temp[5] == "No" and is_date1_before_date2(num_due_date, todays_date):
                # Increment the incomplete and overdue tasks value by 1    
                incomplete_overdue_tasks += 1
    
    # Work out all the variables for the task report, checking for zero-division errors
    incomplete_tasks = total_tasks - complete_tasks
    if total_tasks != 0:
        percent_overdue = round((incomplete_overdue_tasks / total_tasks) * 100, 2)
        percent_incomplete = round((incomplete_tasks / total_tasks) * 100, 2)
    else:
        percent_overdue = 0
        percent_incomplete = 0

    # Write the task report to the task overview txt file
    with open("task_overview.txt", "w") as task_report:
        
        task_report.write(f'''TASK REPORT:
Total Tasks:                {total_tasks}
Complete Tasks:             {complete_tasks}
Incomplete Tasks:           {incomplete_tasks}
Incomplete & Overdue Tasks: {incomplete_overdue_tasks}

{percent_overdue}% of the tasks are overdue.
{percent_incomplete}% of the tasks are incomplete.''')
    
    # Create an empty list variable to store usernames in
    usernames = []

    # Open the user file to get the list of usernames
    with open("user.txt", "r") as user_file:

        # Read the file and copy the lines to a variable
        user_lines = user_file.readlines()

        # Calculate the total number of users by working out the number of lines in the file
        total_users = len(user_lines)

        # For each line in the copy of the file
        for line in user_lines:
            
            # Append the usrname to the usrnames list
            temp = line.strip()
            temp = temp.split(", ")
            usernames.append(temp[0])

    # Open the user report file in write mode, or create it if it doesnt exist yet.
    with open("user_overview.txt", "w") as user_report:
        
        # Write the user report to the file
        user_report.write(f'''USER REPORT:
Total Users:   {total_users}
Total Tasks:   {total_tasks}\n''')
    
    # For each username in the usernames list
    for username in usernames:

        # Create counter variables
        total_user_tasks = 0
        completed_user_tasks = 0
        incomplete_overdue_tasks = 0

        # Open taskk file in read mode
        with open("tasks.txt", "r") as task_file:
            
            # Create a copy of the task file
            task_lines = task_file.readlines()

            # For each line in the copy of the task file:
            for line in task_lines:
            
                # Split the line up into sections
                temp = line.strip()
                temp = temp.split(", ")

                # Format the due date from words to numbers
                num_due_date = date_format_word_to_num(temp[4])

                # If the username on the line is the same as the username being checked
                if temp[0] == username:
                    
                    # Increment the total user tasks variable by 1
                    total_user_tasks += 1
                    
                    # if the 'completed' variable is "Yes"
                    if temp[5] == "Yes":

                        # Increment the completed user tasks variable by 1
                        completed_user_tasks += 1
                    
                    # Else, if the 'completed' variable is "No"
                    elif temp[5] == "No":

                        # If todays date is not before the due date
                        if is_date1_before_date2(todays_date, num_due_date) == False:
                            
                            # Increment the incomplete and overdue tasks value by 1    
                            incomplete_overdue_tasks += 1
        
        # Check for zero tasks and set variables accordingly
        if total_user_tasks == 0:
            percentage_of_all_tasks = 0
            percent_complete = 0
            percent_incomplete = 0
            percent_incomplete_overdue = 0
        else:
            percentage_of_all_tasks = round((total_user_tasks / total_tasks) * 100, 2)
            percent_complete = round((completed_user_tasks / total_user_tasks) * 100, 2)
            percent_incomplete = round(100 - percent_complete, 2)
            percent_incomplete_overdue = round((incomplete_overdue_tasks / total_user_tasks) * 100, 2)

        # Open the user report file in append mode and write a summary of statistics for each username
        with open("user_overview.txt", "a") as user_report:
            user_report.write(f'''\n{username}:
Number of Tasks:                           {total_user_tasks}
% of all tasks:                            {percentage_of_all_tasks}
% of user tasks completed:                 {percent_complete}
% of user tasks not completed:             {percent_incomplete}
% of user tasks not completed and overdue: {percent_incomplete_overdue}\n''')


def show_stats():

    # Generate reports
    generate_reports()

    # Open task report file in read mode
    with open("task_overview.txt", "r") as task_report_file:
        
        # Copy the lines
        task_report = task_report_file.readlines()
        # Join the lines together to make a new file
        task_report = "".join(task_report)
    
    # Open the user report file  in read mode
    with open("user_overview.txt", "r") as user_report_file:
        
        # Copy the lines
        user_report = user_report_file.readlines()
        # Jpin the lines together to make a new file
        user_report = "".join(user_report)
    
    # Print the stats
    print("\n-------------------------------")
    print(task_report)
    print("\n-------------------------------")
    print(user_report)
    print("---------------------------------\n")


# MAIN

# Ask the user to log in and store their username in a variable called current_user
current_user = login()

# Present the relevent menu on a loop to the user that is logged in, and store their menu choice in a variable called menu
while True:
    menu = menu_choice(current_user)


    # If the user choses 'r' and the user is the admin, add a new user to the user.txt file
    if menu == 'r' and current_user == 'admin':
        register_user()
    # If the user choses 's' and the user is the admin, show statistics   
    elif menu == 's' and current_user == 'admin':
        show_stats()
    # If the user choses 'a', allow a user to add a new task to the task.txt file
    elif menu == 'a':
        add_task()
    # If the user choses 'va', read all the tasks from task.txt file and print to the console
    elif menu == 'va':
        view_all()
    # If the user choses 'vm', print only their tasks to the console
    elif menu == 'vm':
        view_mine(current_user)
    # If the user choses 's' and the user is the admin, show statistics   
    elif menu == 'gr':
        generate_reports() 
    # If the user choses 'e', exit
    elif menu == 'e':
        print(f"\nGoodbye {current_user}!!")
        exit()
    # Else print an error message
    else:
        print("\nThat is not a valid option, please try again.\n")
