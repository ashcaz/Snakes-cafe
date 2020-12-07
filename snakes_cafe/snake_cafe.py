
#Variables for menu

appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Unicorn Tears']

#Variables for the menu
header = '*' * 37
welcome = """
**   Welcome to the Snakes Cafe!   **

**    Please see our menu below.   **

**                                 **

** To quit at anytime, type 'quit' **
"""
menu_details = "-" * 10
order_question = '\n**  What would you like to order?  **\n'


#Function for keeping track of order

  

#Function for menu header and footer
def create_menu_header(text):
  print(header)
  print(text)
  print(header)

#Function to create menu
def create_menu_sections(title, menu_items_list):
  print(f'\n\n{title}')
  print(menu_details)
  for item in menu_items_list:
    print(f'{item}\n')



create_menu_header(welcome)

create_menu_sections('Appeitizers', appetizers)
create_menu_sections('Entrees', entrees)
create_menu_sections('Desserts', desserts)
create_menu_sections('Drinks', drinks)

create_menu_header(order_question)
order = {}
user_input = input("\n>")
print(user_input)