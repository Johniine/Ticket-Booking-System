'''
Author: John Eric Ragos
Purpose: To develop a working ticket booking system with a graphical user interface.
Version 1: Created the class and GUI
Version 2: Program wa able to be save
'''

# Import
from tkinter import *

# Constants
ADULT = 15
CHILD = 5
STUDENT = 10

# Maximumn ammount of tickets
max_ticket = 0

# Files
with open('tickets.txt','r') as file_tickets:
    ticket_left = file_tickets.read()
    max_ticket += int(ticket_left)

# Object Oriented Programming
class Ticket():
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
    
    def calc_sub(self):
        '''Calculate and return the sub total'''
        return self.price * self.quantity
# Functions
def collect_ticket():
    '''Create an object for each ticket type and store them in a list'''
    order_list = []
    order_list.clear()
    order_list.append(Ticket(ADULT,int(adult_entry.get())))
    order_list.append(Ticket(CHILD,int(child_entry.get())))
    order_list.append(Ticket(STUDENT,int(student_entry.get())))
    return order_list

def check_ticket():
    '''
        Check if the tickets is sold out ( if it is sold out it will overwrite 
        the label and says 'Sold out' if not sold out it will call function proceed )
    '''
    global max_ticket
    if max_ticket <= 0:
        ticket_label.configure(text="Sold Out")
        total_label.configure(text="Sold Out")
    elif max_ticket > 0:
        proceed()

def check_entry():
    '''Check if the user entered a valid number or not'''
    # Used for calculations
    global max_ticket
    check_adult = int(adult_entry.get())
    check_child = int(child_entry.get())
    check_student = int(student_entry.get())
    # Add all entries
    legend = check_adult + check_child + check_student
    # Check if entry entered exceed maximumn tickets
    if max_ticket - legend == 0:
        calculate()
        error_label.configure(text="Ticket Sold Out")
        ticket_label.configure(text="Sold Out")
        button_calc.destroy()
    elif max_ticket - legend > 0:
        error_label.configure(text="Error Message")
        calculate()
    elif max_ticket - legend < 0:
        error_label.configure(text="You Exceeded Maximumn Ticket")

def proceed():
    '''
    calculate how many tickets are left and will overwrite the label for 'Tickets Left:'
    will also remove itself after the user click it to ensure that they do not click it first before calculating
    '''
    # Global 3 variables to be able to use on calculation and GUI
    global max_ticket
    global button_proc
    global button_quit
    # Get the total tickets of all entries and substract it to 'max_tickets'
    adult = int(adult_entry.get())
    child = int(child_entry.get())
    student = int(student_entry.get())
    zein = adult + child + student
    max_ticket -= zein
    # Files ' Overwrite the total of the other max ticket ( This add the new ticket left ) '
    with open('tickets.txt','w') as dump_tickets:
        dump_tickets.write(str(max_ticket))
    # Overwrite the ticket_label and destroy itself
    ticket_label.configure(text=f"Ticket Left: {max_ticket}")
    adult_num.set("")
    child_num.set("")
    student_num.set("")
    total_label.configure(text=f"")
    button_proc.destroy()
    button_quit = Button(root, text="Quit", font=("Courier",15,"bold"), fg="black", bg="#F75D59",command=quit, width=19)
    button_quit.grid(row=5, column=1, sticky="WE", padx=1, pady=3)

def calculate():
    ''' Calculate the total for all object in the list '''
    # Global two variables to be able to remove and add them back to the GUI
    global button_proc
    global button_quit
    # Calculate the total price for all entries
    total_price = int()
    for order in collect_ticket():
        total_price += order.calc_sub()
    total_label.configure(text=f"${total_price:.2f}")
    # This will add the 'Proceed' Button back to the window after the user click calculate
    button_proc = Button(root, text="Proceed", font=("Courier",15,"bold"), fg="black", bg="#F75D59",command=check_ticket, width=19)
    button_proc.grid(row=5, column=1, sticky="WE", padx=1, pady=3)
    button_quit.destroy()

def quit():
    '''destroy the window'''
    # Destroy the window
    root.destroy()

# Main Program
# Graphical User Interface

# Configuring the window and making sure that it is not resisable so that I can work confidently on the window's width and height.
root = Tk()
root.title("Ticket Booking System")
root.geometry("500x225")
root.configure(bg="#1E1E1E")
# Makes it nor resisable and added a icon
root.resizable(0,0)
photo = PhotoImage(file="ticket2.gif")
root.iconphoto(False,photo)
# IntVar for all entries
adult_num = IntVar()
child_num = IntVar()
student_num = IntVar()
# Set the it to "" to make the entry clean
adult_num.set("")
child_num.set("")
student_num.set("") 
# Labels and editable Labels
error_label = Label(root,text="Error Message", font=("Courier",10,"bold"), fg="white", bg="#1E1E1E")
ticket_label = Label(root, text=f"Ticket Left: {max_ticket}", font=("Courier",15,"bold"), fg="white", bg="#1E1E1E")
label_adult = Label(root, text="Adult $15:", font=("Courier",15,"bold"), fg="black", bg="#FFCCCB")
label_child = Label(root, text="Child $5:", font=("Courier",15,"bold"), fg="black", bg="#FFCCCB")
label_student = Label(root, text="Student/Senior $10:", font=("Courier",15,"bold"), fg="black", bg="#FFCCCB")
label1 = Label(root, text="Total Price:", font=("Courier",15,"bold"), fg="black", bg="#FFCCCB")
total_label = Label(root, text="",font=("Courier",17,"bold"), fg="black", bg="#CCFEFF")
# Buttons
button_calc = Button(root, text="Calculate", font=("Courier",15,"bold"), fg="black", bg="#F75D59",command=check_entry)
button_quit = Button(root, text="Quit", font=("Courier",15,"bold"), fg="black", bg="#F75D59",command=quit, width=19)
# Entries
adult_entry = Entry(root, textvariable = adult_num, justify = "left", font = ("Courier", 17, "bold"), fg="black", bg="#CCFEFF", width=18)
child_entry = Entry(root, textvariable = child_num, justify = "left", font = ("Courier", 17, "bold"), fg="black", bg="#CCFEFF", width=18)
student_entry = Entry(root, textvariable = student_num, justify = "left", font = ("Courier", 17, "bold"), fg="black", bg="#CCFEFF", width=18)
# Grids ' To make the GUI look clean '
error_label.grid(row=0, column=1, sticky="WE", padx=3, pady=3)
ticket_label.grid(row=0, column=0, sticky="WE", padx=3, pady=3)
label_adult.grid(row=1, column=0, sticky="WE", padx=3, pady=3)
label_child.grid(row=2, column=0, sticky="WE", padx=3, pady=3)
label_student.grid(row=3, column=0, sticky="WE", padx=3, pady=3)
label1.grid(row=4, column=0, sticky="WE", padx=3, pady=3)
button_calc.grid(row=5, column=0, sticky="WE", padx=3, pady=3)
adult_entry.grid(row=1, column=1, sticky="W", padx=1, pady=3)
child_entry.grid(row=2, column=1, sticky="W", padx=1, pady=3)
student_entry.grid(row=3, column=1, sticky="W", padx=1, pady=3)
total_label.grid(row=4, column=1, sticky="WE", padx=1, pady=3)
button_quit.grid(row=5, column=1, sticky="WE", padx=1, pady=3)
# Mainloop
root.mainloop()