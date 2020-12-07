
#Variables for menu
menu = {
  'appetizers': ['Wings', 'Cookies', 'Spring Rolls'],
  'entrees': ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
  'desserts': ['Ice Cream', 'Cake', 'Pie'],
  'drinks': ['Coffee', 'Tea', 'Unicorn Tears']
}


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

#Function to track orders
def order_tracker():
  order = {}
  user_quit = False
  
  while not user_quit:
    user_input = input('\n> ')

    if user_input.lower() == 'quit':
      return
    else:
      #Kept getting KeyError and Remebered from doing the prework on Sololearn about try and except!
      try:
        order[user_input] += 1
        print(f'\n** {order[user_input]} orders of {user_input} have been added to your meal **')
      except:
        order[user_input] = 1
        print(f'\n** {order[user_input]} order of {user_input} have been added to your meal **')

create_menu_header(welcome)

create_menu_sections('Appeitizers', menu['appetizers'])
create_menu_sections('Entrees', menu['entrees'])
create_menu_sections('Desserts', menu['desserts'])
create_menu_sections('Drinks', menu['drinks'])

create_menu_header(order_question)

order_tracker()


  