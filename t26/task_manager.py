#======
# I have not written pseudocode for this task, as the comments provided with the exercise were sufficient themselves to act as pseudocode.

#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date,datetime
import os.path #this is to check for if a file already exists or not

#====Login Section====
def reg_user():
    '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
    user_registered = False
    while not user_registered:
        new_user = input("Enter a new username:\n")
        new_pass = input("Enter a password:\n")
        pass_confirm = input("Re-enter that password:\n")
        user_clash = False #boolean flag to represent whether username is already in the file
        f = open("user.txt",'r')
        for line in f:
            if line.split(", ")[0] == new_user:
                user_clash = True
        if pass_confirm == new_pass and not user_clash:
            f = open("user.txt",'a')
            f.write("\n"+new_user+", "+new_pass)
            f.close()
            user_registered = True
        elif user_clash:
            print("That user was already defined in user.txt, clashes not allowed. Try another username.")
        else:
            print("Passwords did not match.")


def add_task():
    '''In this block you will put code that will allow a user to add a new task to task.txt file
    - You can follow these steps:
        - Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task.
        - Then get the current date.
        - Add the data to the file task.txt and
        - You must remember to include the 'No' to indicate if the task is complete.'''
    user_query = input("What is the username of the person being assigned this task?:\n")
    task_title = input("Name the task:\n")
    task_description = input("Describe the task (without commas):\n") #if commas are used, the logic breaks. So don't do that.
    #if this were anything more than a relatively short exercise I would have to look into encoding commas in a way that does not break the logic.
    due_date = input("When is the task due? (enter in format %d %b %Y):\n")
    current_date = date.today().strftime("%d %b %Y")
    task_complete = input("Is the task complete?\n").capitalize()+"\n"
    f = open("tasks.txt",'a')
    f.write(f"{user_query}, {task_title}, {task_description}, {current_date}, {due_date}, {task_complete}")
    f.close()

def view_all():
    '''In this block you will put code so that the program will read the task from task.txt file and
        print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
        You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''
    f = open("tasks.txt",'r')
    for line in f:
        if line!="":
            task_list = line.split(", ")
            print(f"User: {task_list[0]}\nTask name: {task_list[1]}\nTask description: {task_list[2]}\nCurrent Date: {task_list[3]}\nDue Date: {task_list[4]}\nTask Complete: {task_list[5]}")
    f.close()

def view_mine():
    #pass
    '''In this block you will put code the that will read the task from task.txt file and
    print to the console in the format of Output 2 presented in the L1T19 pdf
    You can do it in this way:
        - Read a line from the file
        - Split the line where there is comma and space.
        - Check if the username of the person logged in is the same as the username you have
        read from the file.
        - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
    f = open("tasks.txt", 'r')
    count = 0 #I know I can use enumerate(), but this is more efficient
    list_of_tasks = []
    for line in f:
        if line == "":
            continue
        count += 1
        task_list = line.split(", ")
        list_of_tasks.append(task_list)
        if logged_in_user == task_list[0]:
            print(f"Task Number:{count}\nTask name: {task_list[1]}\nTask description: {task_list[2]}\nCurrent Date: {task_list[3]}\nDue Date {task_list[4]}\nTask Complete: {task_list[5]}")
    f.close()
    task_select = int(input("Enter the number of your task, or -1 to return to the main menu:\n"))
    if task_select == -1:
        return
    elif task_select > 0:
        print(f"Task number:{task_select}\nTask name: {list_of_tasks[task_select-1][1]}\nTask description: {list_of_tasks[task_select-1][2]}\n Current Date: {list_of_tasks[task_select-1][3]}\n Due date: {list_of_tasks[task_select-1][4]}\nTask Complete: {list_of_tasks[task_select-1][5]}")
        mark_edit_input = input("Mark the task complete? (m) or edit the task (e)").lower()
        if mark_edit_input == "m":
            list_of_tasks[task_select-1][5]="Yes\n" #a little trick, \n is encoded by design here
        if mark_edit_input == "e" and list_of_tasks[task_select-1][5]!="Yes":
            user_swap_input = input("Who should this task be assigned to? Leave this field blank for no change\n")
            if user_swap_input == "":
                pass
            else:
                list_of_tasks[task_select-1][0] = user_swap_input
            due_date_input = input("Input a new due date. Leave blank for no change\n")
            if due_date_input == "":
                pass
            else:
                list_of_tasks[task_select-1][4] = due_date_input
    f = open("tasks.txt",'w')
    for i in list_of_tasks:
        for j in i:
            if j!=i[5]:
                f.write(j+", ")
            else:
                f.write(j)
    f.close()

def generate_reports():
    #===================================Generate task_overview.txt
    #-------------------Read tasks.txt
    f = open("tasks.txt", 'r')
    count = 0 #I know I can use enumerate(), but this is more efficient
    list_of_tasks = []
    for line in f:
        if line == "":
            continue
        count += 1
        
    #-------------------Buffer output for task_overview.txt
        task_list = line.split(", ")
        list_of_tasks.append(task_list)
        
    f.close()    
    #-------------------Write to task_overview.txt
    f = open("task_overview.txt",'w')
    complete_count = 0
    unfinished_count = 0
    overdue_count = 0
    current_date = datetime.now()
    for i in list_of_tasks:
        due_date = datetime.strptime(i[4],"%d %b %Y")
        if i[5] == "Yes\n" or i[5] == "Yes":
            complete_count+=1
        elif i[5] == "No\n" == "Yes":
            unfinished_count+=1
            if current_date>due_date:
                overdue_count+=1
    percentage_incomplete = (unfinished_count/count)*100
    percentage_overdue = (overdue_count/count)*100
            
    f.write(f"Total number of tasks: {count}\nTotal number of completed tasks: {complete_count}\nTotal number of incomplete tasks: {unfinished_count}\nTotal number of overdue tasks: {overdue_count}\nPercentage of incomplete tasks: {percentage_incomplete}\nPercentage of overdue tasks: {percentage_overdue}\n")
    f.close()
    #================================Generate user_overview.txt
    #----------------------Read input in from user.txt
    f = open("user.txt", 'r')
    c_count = 0
    users = []
    for line in f:
        if line == "":
            continue
        c_count += 1
        user_list = line.split(", ")
        users.append(user_list[0])
    f.close()

    #---------------------reuse list_of_tasks for needed data
    user_task_counts = []
    user_task_percentages = []
    user_percentages_complete = []
    user_percentages_incomplete = []
    user_percentages_overdue = []
    for user in users:
        user_task_count = 0
        user_task_completed_count = 0
        user_task_incomplete_count = 0
        user_task_overdue_count = 0
        for line in list_of_tasks:
            if line[0]==user:
                user_task_count += 1
                if line[5]=="Yes\n" or line[5]=="Yes":
                    user_task_completed_count += 1
                elif line[5]=="No\n" or line[5]=="No":
                    user_task_incomplete_count += 1
                    if current_date>datetime.strptime(line[4],"%d %b %Y"):
                        user_task_overdue_count += 1
        user_task_percentage = (user_task_count/count) * 100
        if user_task_count == 0:
            user_percentage_complete = 0
            user_percentage_incomplete = 0
            user_percentage_overdue = 0
        else:
            user_percentage_complete = (user_task_completed_count/user_task_count)*100
            user_percentage_incomplete = (user_task_incomplete_count/user_task_count)*100
            user_percentage_overdue = (user_task_overdue_count/user_task_count)*100
        user_task_counts.append(user_task_count)
        user_task_percentages.append(user_task_percentage)
        user_percentages_complete.append(user_percentage_complete)
        user_percentages_incomplete.append(user_percentage_incomplete)
        user_percentages_overdue.append(user_percentage_overdue) 
        #Using 2d lists for these would be more efficient but A) we've not been shown those yet,
        #and B) I don't want to inadvertently mess up my indexing or semantics

    #---------------------Write to user_overview.txt
    f = open("user_overview.txt",'w')
    f.write(f"Total number of users registered: {c_count}\nTotal number of tasks: {count}")
    user_iter_count = 0
    for user in users:
        f.write(f"\n\nUser {user}:\nTotal tasks: {user_task_counts[user_iter_count]}\nPercentage of total tasks assigned to this user: {user_task_percentages[user_iter_count]}\nPercentage of tasks assigned to this user completed:{user_percentages_complete[user_iter_count]}\nPercentage of tasks assigned to this user incomplete: {user_percentages_incomplete[user_iter_count]}\nPercentage of tasks assigned to this user that are overdue: {user_percentages_overdue[user_iter_count]}")
        user_iter_count += 1
    f.close()

def display_statistics():
    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        generate_reports()
    f = open("task_overview.txt",'r')
    for line in f:
        print(line,end="")
    f.close()
    print()
    f = open("user_overview.txt",'r')
    for line in f:
        print(line,end="")
    print()
    f.close()

'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
logged_in = False
logged_in_user = ""
while not logged_in:
    login_prompt = input("Enter your username:\n")
    password_prompt = input("Enter your password:\n")
    f = open("user.txt",'r')
    for line in f:
        user_list = line.split(", ")
        user_list[1] = user_list[1].replace("\n","")
        if user_list[0] == login_prompt and user_list[1] == password_prompt:
            logged_in = True
            logged_in_user = login_prompt
    f.close()
    if not logged_in:
        print("Username and password combination not found in user.txt, try again")
        #remember that the user-pass combination stored in user .txt is admin, adm1n

while True:
    #presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    if logged_in_user == "admin":
        menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
ds - Display statistics
gr - Generate Reports
va - View all tasks
vm - view my tasks
e - Exit
: ''').lower()
    else:
        menu = input('''\nSelect one of the following Options below:
a - Adding a task
gr - Generate Reports
va - View all tasks
vm - view my tasks
e - Exit
: ''').lower()

    if menu == 'r' and logged_in_user == "admin":
        reg_user()
        

    elif menu == "ds" and logged_in_user == "admin":
        display_statistics()

    elif menu == 'a':
        add_task()

    elif menu == 'gr':
        generate_reports()

    elif menu == 'va':
        view_all()
        

    elif menu == 'vm':
        view_mine()
        

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")