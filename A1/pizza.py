#name: Angela(Qingchen) Hu, McGill student ID: 261075832
import math

PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED = 4.0
PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED = 3.0
SPECIAL_INGREDIENT = "guacamole"
SPECIAL_INGREDIENT_COST = 19.99
FAIR = True

def get_pizza_area(diameter):
    '''(float) -> float
    Returns the area of a pizza given its diameter
    which is a positive float.
    
    >>> get_pizza_area(2.5)
    4.908738521234052
    >>> get_pizza_area(3.00)
    7.0685834705770345
    >>> get_pizza_area(3.456)
    9.380745398136664
    '''
    return math.pi*((diameter/2)**2)

def get_fair_quantity(diameter1, diameter2):
    '''(float, float) -> int
    According to the pizza areas calculated given the 2
    positive floats: diameter1 and diameter2, if the FAIR variable
    is set to True, returns the minimum amount of small pizzas one
    must orders to acquire at least the same amount of one large
    pizza by area; if the FAIR variable is set to False,
    returns 1.5 times the calculated minimum amount and
    rounds it down to the nearest integer.
    
    >>> FAIR = True
    >>> get_fair_quantity(5.0, 15.0)
    9
    >>> get_fair_quantity(3.5, 12.5)
    13
    >>> FAIR = False
    >>> get_fair_quantity(3.5, 12.5)
    19
    '''
    if diameter1>diameter2:
        remainder=get_pizza_area(diameter1)%get_pizza_area(diameter2)
        number=(get_pizza_area(diameter1)//get_pizza_area(diameter2))
    else:
        remainder=get_pizza_area(diameter2)%get_pizza_area(diameter1)
        number=(get_pizza_area(diameter2)//get_pizza_area(diameter1))
    if remainder!=0:
        number+=1
    if not FAIR:
        number=int(number*1.5)
    return number

def pizza_formula(d_large, d_small, c_large, c_small, n_small):
    '''(num, num, num, num, num) -> float
    Returns the value of the 'missing' input, which is represented
    by the integer '-1' within the 5 inputs. The four positive float
    inputs are d_large, d_small, c_large, c_small, and the one positive
    integer input is n_small. The number of large pizzas is assumed
    to be 1. The missing value is calculated by using the other
    4 inputs and rounded to 2 decimal places.
    
    >>> pizza_formula(12.5, 3.5, 12.0, -1, 13)
    12.23
    >>> pizza_formula(15.0, 5.0, 9.5, -1, 9)
    9.5
    >>> pizza_formula(14.0, -1, 8.6, 10.5, 5)
    6.92
    '''
    if d_large==-1:
        d_large=math.sqrt((n_small*c_large*d_small**2)/c_small)
        return round(d_large,2)
    elif d_small==-1:
        d_small=math.sqrt((c_small*d_large**2)/(c_large*n_small))
        return round(d_small,2)
    elif c_large==-1:
        c_large=(c_small*d_large**2)/(n_small*d_small**2)
        return round(c_large,2)
    elif c_small==-1:
        c_small=(n_small*c_large*d_small**2)/(d_large**2)
        return round(c_small,2)
    else:
        n_small=(c_small*d_large**2)/(c_large*d_small**2)
        return round(n_small,2)
    #too many returns

def get_pizza_cake_cost(base_diameter, height_per_level):
    '''(int, float) -> float
    If the FAIR variable is set to True, returns the cost
    of the pizza cake through calculations with the given
    base_diameter as a  positive integer, height_per_level
    as  a positive float and the global variable:
    PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED of the pizza cake.
    If the FAIR variable is set to False,
    returns 1.5 times the original cost and rounded to
    2 decimal places.
    
    >>> FAIR = True
    >>> get_pizza_cake_cost(8, 3.22)
    2063.65
    >>> get_pizza_cake_cost(3, 1.0)
    43.98
    >>> FAIR = False
    >>> get_pizza_cake_cost(3, 1.0)
    65.97
    '''
    area=get_pizza_area(base_diameter)
    diameter=base_diameter-1
    while diameter>=1:
        area+=get_pizza_area(diameter)
        diameter-=1
    cost=PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED*area*height_per_level
    if not FAIR:
        cost=cost*1.5
    return round(cost,2)

def get_pizza_poutine_cost(diameter, height):
    '''(int, float) -> float
    If the FAIR variable is set to True, returns the cost
    of the pizza poutine through calculations with the given
    diameter as a positive integer, height as a positive float
    and the global variable: PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED
    of the pizza poutine. If the FAIR variable is set to False,
    returns 1.5 times the original cost and rounded to
    2 decimal places.
    
    >>> FAIR = True
    >>> get_pizza_poutine_cost(2, 1.5)
    14.14
    >>> get_pizza_poutine_cost(11, 2.0)
    570.2
    >>> FAIR = False
    >>> get_pizza_poutine_cost(11, 2.0)
    855.3
    '''
    volume=math.pi*height*(diameter/2)**2
    cost=volume*PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED
    if not FAIR:
        cost=cost*1.5
    return round(cost,2)

def display_welcome_menu():
    '''() -> NoneType
    Displays a welcome message and three available options
    to the screen for the user.
    
    >>> display_welcome_menu()
    Welcome To Freddy Fazbear's Pizza.
    Please choose an option:
    A. Special Orders
    B. Formula Mode 
    C. Quantity Mode
    '''
    print("Welcome To Freddy Fazbear's Pizza.")
    print("Please choose an option:")
    print("A. Special Orders\nB. Formula Mode \nC. Quantity Mode")

def special_orders():
    '''() -> NoneType
    Displays the message to ask the user to choose
    a meal between cake or poutine and enter their
    desired diameter value and height value. Cost of
    the special ingredient would be added to the order's
    cost if the user types in 'y' or 'yes'.
    If anything else is typed, the cost of
    the special ingredient would not be added.
    
    >>> special_orders()
    Would you like the cake or poutine? cake
    Enter diameter: 2
    Enter height: 1.0
    Do you want the guacamole? yes
    The cost is $35.7
    >>> Would you like the cake or poutine? cake
    Enter diameter: 3
    Enter height: 1.0
    Do you want the guacamole? no
    The cost is $43.98
    >>> special_orders()
    Would you like the cake or poutine? poutine
    Enter diameter: 4
    Enter height: 2.5
    Do you want the guacamole? yes
    The cost is $114.24
    '''
    choice=input("Would you like the cake or poutine? ")
    diameter=int(input("Enter diameter: "))
    height=float(input("Enter height: "))
    special_ingredient=input("Do you want the "+SPECIAL_INGREDIENT+"? ")
    if choice == "cake":
        cost=get_pizza_cake_cost(diameter, height)
    else:
        cost=get_pizza_poutine_cost(diameter, height)
    if special_ingredient == 'y' or special_ingredient =='yes':
        cost+=SPECIAL_INGREDIENT_COST
    print("The cost is $"+str(cost))

def quantity_mode():
    '''() -> NoneType
    Displays the message to ask the user to enter the diameters
    for 2 pizzas, and then tells the minimum amount of small pizzas
    the users need to buy to acquire at least the same amount of
    one large pizza by area.
    
    >>> quantity_mode()
    Enter diameter 1: 14.0
    Enter diameter 2: 8.0
    You should buy 4 pizzas.
    >>> quantity_mode()
    Enter diameter 1: 15.5
    Enter diameter 2: 2.5
    You should buy 39 pizzas.
    >>> quantity_mode()
    Enter diameter 1: 5.5
    Enter diameter 2: 14.25
    You should buy 7 pizzas.
    '''
    diameter1=float(input("Enter diameter 1: "))
    diameter2=float(input("Enter diameter 2: "))
    number=get_fair_quantity(diameter1, diameter2)
    print("You should buy "+str(number)+" pizzas.")
    
def formula_mode():
    '''() -> NoneType
    Displays the message to ask the users to enter the
    diameter of one large pizza and one small pizza, the respective
    costs of 2 pizzas and the amount of small pizzas. Then,
    prints out the actual value of the missing
    input which was given as -1 among the 5 inputs entered.
    
    >>> formula_mode()
    Enter large diameter: 12.0
    Enter small diameter: 6.0
    Enter large price: 10.0
    Enter small price: -1
    Enter small number: 2
    The missing value is: 5.0
    >>> formula_mode()
    Enter large diameter: 14.0
    Enter small diameter: -1
    Enter large price: 8.6
    Enter small price: 10.5
    Enter small number: 5
    The missing value is: 6.92
    >>> formula_mode()
    Enter large diameter: 15.0
    Enter small diameter: 5.0
    Enter large price: -1
    Enter small price: 9.5
    Enter small number: 9
    The missing value is: 9.5
    '''
    d_large=float(input("Enter large diameter: "))
    d_small=float(input("Enter small diameter: "))
    c_large=float(input("Enter large price: "))
    c_small=float(input("Enter small price: "))
    n_small=float(input("Enter small number: "))
    missing_value=pizza_formula(d_large, d_small, c_large, c_small, n_small)
    print("The missing value is: "+str(missing_value))
    
def run_pizza_calculator():
    '''() -> NoneType
    Displays a welcome message, some program options to the screen,
    and asks the user to choose by inputting an option. Then calls
    the corresponding function. If the user inputs an option that's
    invalid, prints out "Invalid mode.".
    
    >>> run_pizza_calculator()
    Welcome To Freddy Fazbear's Pizza.
    Please choose an option:
    A. Special Orders
    B. Formula Mode 
    C. Quantity Mode
    Your choice: C
    Enter diameter 1: 10.5
    Enter diameter 2: 5.2
    You should buy 5 pizzas.
    >>> run_pizza_calculator()
    Welcome To Freddy Fazbear's Pizza.
    Please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: B
    Enter large diameter: 12.0
    Enter small diameter: 6.0
    Enter large price: 10.0
    Enter small price: -1
    Enter small number: 2
    The missing value is: 5.0
    >>> run_pizza_calculator()
    Welcome To Freddy Fazbear's Pizza.
    Please choose an option:
    A. Special Orders
    B. Formula Mode 
    C. Quantity Mode
    Your choice: E
    Invalid mode.
    '''
    display_welcome_menu()
    choice = input("Your choice: ")
    if choice == "A":
        special_orders()
    elif choice == "B":
        formula_mode()
    elif choice == "C":
        quantity_mode()
    else:
        print("Invalid mode.")
