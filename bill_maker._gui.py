import tkinter as tk


class Bill_Maker_GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bill Maker")
        self.root.geometry("500x500")
        self.root.resizable(True, True)
        # put the bill maker in the center of the screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"+{x}+{y}")
        self.root.configure(background="white")
        # create 4 entry boxes
        self.cart=[]
        self.item_name_entry = tk.Entry(self.root, width=20)
        self.item_name_entry.grid(row=0, column=0)
        self.quantity_entry = tk.Entry(self.root, width=20)
        self.quantity_entry.grid(row=0, column=1)
        self.unit_price_entry = tk.Entry(self.root, width=20)
        self.unit_price_entry.grid(row=0, column=2)
        self.vat_entry = tk.Entry(self.root, width=20)
        self.vat_entry.grid(row=0, column=3)
        self.total_price_entry = tk.Entry(self.root, width=20)
        self.total_price_entry.grid(row=0, column=4)
        # create a button to add the item to the bill
        self.add_item_button = tk.Button(
            self.root, text="Add item", command=self.add_item)
        self.add_item_button.grid(row=0, column=5)
        # create a button to save the bill
        self.save_bill_button = tk.Button(
            self.root, text="Save bill", command=self.save_bill)
        self.save_bill_button.grid(row=0, column=6)
        # create a button to quit the program
        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit)
        self.quit_button.grid(row=0, column=7)
        # create a listbox to display the bill
        self.bill_listbox = tk.Listbox(self.root, width=50)
        self.bill_listbox.grid(row=1, column=0, columnspan=8)
        # create a label to display the total price
        self.total_price_label = tk.Label(self.root, text="Total price:")
        self.total_price_label.grid(row=2, column=0)
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

    def save_bill(self):
        # save the bill to a file
        pass

    def add_item(self):
        # add the item to the bill
        data=[]
        data.append(self.item_name_entry.get())
        data.append(self.quantity_entry.get())
        data.append(self.unit_price_entry.get())
        data.append(self.vat_entry.get())
        data.append(self.total_price_entry.get())
        self.cart.append(data)
        pass


if __name__ == "__main__":
    bill_maker = Bill_Maker_GUI()
    

    pass
