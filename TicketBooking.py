'''
Author: John Eric Ragos
Purpose: To develop a working ticket booking system with a graphical user interface.
Version 1: Created the class and GUI
'''

from tkinter import *

ADULT = 15
CHILD = 5
STUDENT = 10
MAX_TICKET = 100

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
    order_list.append(Ticket(ADULT,int(adult_entry.get())))
    order_list.append(Ticket(CHILD,int(child_entry.get())))
    order_list.append(Ticket(STUDENT,int(student_entry.get())))
    return order_list

def calculate():
    ''' Calculate the total for all object in the list '''
    total_price = int()
    for order in collect_ticket():
        total_price += order.calc_sub()
    total_label.configure(text=f"${total_price:.2f}")

# GUI
root = Tk()
root.title("Booking")
root.geometry("500x200")
root.configure(bg="black")
root.resizable(0,0)

adult_num = IntVar()
child_num = IntVar()
student_num = IntVar()


adult_num.set("")
child_num.set("")
student_num.set("")


label_adult = Label(root, text="Adult $15:", font=("Courier",15,"bold"), fg="black", bg="#FFCCCB")
label_child = Label(root, text="Child $5:", font=("Courier",15,"bold"), fg="black", bg="#FFCCCB")
label_student = Label(root, text="Student/Senior $10:", font=("Courier",15,"bold"), fg="black", bg="#FFCCCB")
label1 = Label(root, text="Total Price:", font=("Courier",15,"bold"), fg="black", bg="#FFCCCB")

total_label = Label(root, text="",font=("Courier",17,"bold"), fg="black", bg="#ADD8E6")

button_calc = Button(root, text="Calculate", font=("Courier",15,"bold"), fg="black", bg="#FA8072",command=calculate)

adult_entry = Entry(root, textvariable = adult_num, justify = "center", font = ("Courier", 17, "bold"), fg="black", bg="#ADD8E6")
child_entry = Entry(root, textvariable = child_num, justify = "center", font = ("Courier", 17, "bold"), fg="black", bg="#ADD8E6")
student_entry = Entry(root, textvariable = student_num, justify = "center", font = ("Courier", 17, "bold"), fg="black", bg="#ADD8E6")

label_adult.grid(row=0, column=0, sticky="WE")
label_child.grid(row=1, column=0, sticky="WE")
label_student.grid(row=2, column=0, sticky="WE")
label1.grid(row=3, column=0, sticky="WE")
button_calc.grid(row=4, column=0, sticky="WE")
adult_entry.grid(row=0, column=1, sticky="WE")
child_entry.grid(row=1, column=1, sticky="WE")
student_entry.grid(row=2, column=1, sticky="WE")
total_label.grid(row=3, column=1, sticky="WE")

root.mainloop()