'''
Author: John Eric Ragos
Purpose: To develop a working ticket booking system with a graphical user interface.
Version 1: Created the class and GUI
'''

from tkinter import *

ADULT = 15
CHILD = 5
STUDENT = 10
max_ticket = 3

class Ticket():
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
    
    def calc_sub(self):
        '''Calculate and return the sub total'''
        return self.price * self.quantity

def collect_ticket():
    '''Create an object for each ticket type and store them in a list'''
    order_list = []
    order_list.clear()
    order_list.append(Ticket(ADULT,int(adult_entry.get())))
    order_list.append(Ticket(CHILD,int(child_entry.get())))
    order_list.append(Ticket(STUDENT,int(student_entry.get())))
    return order_list

def check_ticket():
    '''Check if the tickets is sold out'''
    global max_ticket

    if max_ticket <= 0:
        ticket_label.configure(text="Sold Out")
        total_label.configure(text="Sold Out")
    elif max_ticket > 0:
        proceed()
        

def proceed():
    '''Make user continue and check how many tickets are left'''
    global max_ticket

    adult = int(adult_entry.get())
    child = int(child_entry.get())
    student = int(student_entry.get())
    zein = adult + child + student
    max_ticket -= zein

    ticket_label.configure(text=f"Ticket Left: {max_ticket}")
    adult_num.set("")
    child_num.set("")
    student_num.set("")
    total_label.configure(text=f"")

def calculate():
    ''' Calculate the total for all object in the list '''
    total_price = int()
    for order in collect_ticket():
        total_price += order.calc_sub()
    total_label.configure(text=f"${total_price:.2f}")

def quit():
    '''destroy the window'''
    root.destroy()

# GUI
root = Tk()
root.title("Ticket Booking System")
root.geometry("500x215")
root.configure(bg="#1E1E1E")
photo = PhotoImage(file="ticket2.gif")

root.resizable(0,0)
root.iconphoto(False,photo)

adult_num = IntVar()
child_num = IntVar()
student_num = IntVar()


adult_num.set("")
child_num.set("")
student_num.set("")

ticket_label = Label(root, text=f"Ticket Left: {max_ticket}", font=("Courier",15,"bold"), fg="white", bg="#1E1E1E")

label_adult = Label(root, text="Adult $15:", font=("Courier",15,"bold"), fg="black", bg="#FFCCCB")
label_child = Label(root, text="Child $5:", font=("Courier",15,"bold"), fg="black", bg="#FFCCCB")
label_student = Label(root, text="Student/Senior $10:", font=("Courier",15,"bold"), fg="black", bg="#FFCCCB")
label1 = Label(root, text="Total Price:", font=("Courier",15,"bold"), fg="black", bg="#FFCCCB")

total_label = Label(root, text="",font=("Courier",17,"bold"), fg="black", bg="#CCFEFF")

button_calc = Button(root, text="Calculate", font=("Courier",15,"bold"), fg="black", bg="#F75D59",command=calculate)
button_proc = Button(root, text="Proceed", font=("Courier",15,"bold"), fg="black", bg="#F75D59",command=check_ticket, width=19)

adult_entry = Entry(root, textvariable = adult_num, justify = "left", font = ("Courier", 17, "bold"), fg="black", bg="#CCFEFF", width=18)
child_entry = Entry(root, textvariable = child_num, justify = "left", font = ("Courier", 17, "bold"), fg="black", bg="#CCFEFF", width=18)
student_entry = Entry(root, textvariable = student_num, justify = "left", font = ("Courier", 17, "bold"), fg="black", bg="#CCFEFF", width=18)

ticket_label.grid(row=0, columnspan=2, sticky="WE")
label_adult.grid(row=1, column=0, sticky="WE", padx=3, pady=3)
label_child.grid(row=2, column=0, sticky="WE", padx=3, pady=3)
label_student.grid(row=3, column=0, sticky="WE", padx=3, pady=3)
label1.grid(row=4, column=0, sticky="WE", padx=3, pady=3)
button_calc.grid(row=5, column=0, sticky="WE", padx=3, pady=3)
adult_entry.grid(row=1, column=1, sticky="W", padx=1, pady=3)
child_entry.grid(row=2, column=1, sticky="W", padx=1, pady=3)
student_entry.grid(row=3, column=1, sticky="W", padx=1, pady=3)
total_label.grid(row=4, column=1, sticky="WE", padx=1, pady=3)
button_proc.grid(row=5, column=1, sticky="WE", padx=1, pady=3)

root.mainloop()