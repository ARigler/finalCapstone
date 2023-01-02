'''
No pseudocode here because the code template literally says what to do; that is my pseudocode
'''
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost


    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return f"Identifier {self.code}, bound for {self.country}. Model {self.product}, costing {self.cost}. Quantity of stock: {self.quantity}"



#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    pass
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:
        f = open("inventory.txt",'r')
        for line in f:
            #Skip the first line as it shouldn't be considered a data point
            if "Country,Code,Product,Cost,Quantity" in line:
                continue
            current_line = line.split(",")
            shoe_list.append(Shoe(current_line[0],current_line[1],current_line[2],current_line[3],current_line[4]))
        print("Database populated\n")
    except FileNotFoundError:
        print("File not found\n")
    except PermissionError:
        print("The inventory.txt file does exist but this program does not have the permissions to open it\n")
    except EOFError:
        print("The file is empty\n")
    except OSError:
        print("An error occurred while reading the file.\n")
    except IndexError:
        print("One or more of the lines in inventory.txt did not have enough data points to make a shoe object.\n")
    finally:
        f.close()

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    try:
        country = input("What country is the set of shoes bound for?\n")
        code = input("What is the order's unique identifier?\n")
        product = input("What is the name of the product?\n")
        cost = int(input("What is the cost of the product? Enter a number\n"))
        quantity = int(input("How many pairs of shoes are in the order? Enter an integer\n"))
        shoe_list.append(Shoe(country,code,product,cost,quantity))
    except ValueError:
        print("A validation error occurred; a field which was supposed to have only a number did not have a number. Try again\n")
        capture_shoes()

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    for count, order in enumerate(shoe_list):
        print(str(count) + " " +str(order)+"\n")

def re_stock():
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    try:   
        f=open("inventory.txt","r+")
        lowest_qty = shoe_list[0]
        for shoe in shoe_list:
            if shoe.get_quantity()<lowest_qty.get_quantity():
                lowest_qty = shoe
        user_add = int(input("How many pairs of shoes would you like to restock? enter a whole number\n"))
        initial_qty = lowest_qty.get_quantity()
        lowest_qty.quantity += user_add
        identifier = lowest_qty.code

        lines = []
        for line in f:
            lines.append(line.split(","))
        
        for line in lines:
            if identifier in line[1]:
                line[4]=str(lowest_qty.get_quantity())+"\n"
        
        for i in range(0,len(lines)):
            lines[i] = ",".join(lines[i])

        f.seek(0)
        f.truncate(0)
        f.writelines(lines)

    except ValueError:
        print("The number entered was not a valid integer. Try again\n")
        re_stock()
    except FileNotFoundError:
        print("The inventory.txt file does not exist\n")
    except PermissionError:
        print("The inventory.txt file does exist but this program does not have the permissions to open it\n")
    except EOFError:
        print("The file is empty\n")
    except OSError:
        print("An error occurred while reading the file.\n")
    except IndexError:
        print("There aren't any shoes in the shoe database yet\n")
    finally:
        f.close()

def seach_shoe():
    '''
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    '''
    search_term = input("What is the shoe code?\n")
    for shoe in shoe_list:
        if search_term in shoe.code:
            print(shoe)
            return
    print("Shoe not found\n")

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    if len(shoe_list) == 0:
        print("There are no shoes in the database yet\n")
    for shoe in shoe_list:
        print(f"{shoe.code}: value = {(shoe.cost*shoe.quantity):.2f}")


def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    try:
        highest_shoe = shoe_list[0]
        for shoe in shoe_list:
            if shoe.get_quantity()>highest_shoe.get_quantity():
                highest_shoe = shoe
        print(f"{highest_shoe.product} is for sale!")
    except IndexError:
        print("The list of shoes has not been populated yet\n")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:
    user_choice = input('''Welcome to the Nike stock viewer.\nMake one of the following choices:
    r - read shoe data in from inventory.txt and populate the shoe database
    c - capture shoe data from user input
    v - view all shoes in the database
    s - search the shoe database by code
    h - display the product with the highest quantity
    z - restock shoes of the lowest quantity
    m - calculate the monetary value per item
    q - exit the application   
    ''').lower()
    if user_choice == "r":
        read_shoes_data()
    elif user_choice == "c":
        capture_shoes()
    elif user_choice == "v":
        view_all()
    elif user_choice == "s":
        seach_shoe()
    elif user_choice == "h":
        highest_qty()
    elif user_choice == "z":
        re_stock()
    elif user_choice == "m":
        value_per_item()
    elif user_choice == "q":
        print("Goodbye, enjoy your day")
        exit()
    else:
        print("That wasn't a valid option. Try again.\n")    