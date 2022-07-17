import tkinter as tk


class Bill_Maker_GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bill Maker")
        self.root.geometry("800x800")
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
        # add a label for the item name
        self.item_name_label = tk.Label(self.root, text="Item name:", background="white", font=("Arial", 12), width=10)
        self.item_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.item_name_entry = tk.Entry(self.root, width=20)
        self.item_name_entry.grid(row=1, column=1)
        # add a label for the quantity
        self.quantity_label = tk.Label(self.root, text="Quantity:", background="white", font=("Arial", 12), width=10)
        self.quantity_label.grid(row=1, column=2, padx=10, pady=10)
        self.quantity_entry = tk.Entry(self.root, width=20)
        self.quantity_entry.grid(row=1, column=3)
        # add a label for the unit price
        self.unit_price_label = tk.Label(self.root, text="Unit price:", background="white")
        self.unit_price_label.grid(row=1, column=4, padx=10, pady=10)
        self.unit_price_entry = tk.Entry(self.root, width=20)
        self.unit_price_entry.grid(row=1, column=5)
        # add a label for the VAT
        self.vat_label = tk.Label(self.root, text="VAT Rate:", background="white")
        self.vat_label.grid(row=1, column=6, padx=10, pady=10)
        self.vat_entry = tk.Entry(self.root, width=20)
        self.vat_entry.grid(row=1, column=7)

        # create a button to add the item to the bill
        self.add_item_button = tk.Button(
            self.root, text="Add item", command=self.add_item)
        self.add_item_button.grid(row=2, column=2, padx=10, pady=10)
        # create a button to save the bill
        self.save_bill_button = tk.Button(
            self.root, text="Save bill", command=self.save_bill)
        self.save_bill_button.grid(row=2, column=0, padx=10, pady=10)
        # create a button to quit the program
        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit)
        self.quit_button.grid(row=2, column=6, padx=10, pady=10)
        # create a label for the bill
        self.bill_label = tk.Label(self.root, text="Bill:", background="white")
        self.bill_label.grid(row=2, column=4, padx=10, pady=10)
        # create a listbox to display the bill
        self.bill_listbox = tk.Listbox(self.root, width=50)
        self.bill_listbox.grid(row=3, column=1, columnspan=8)
        # create a label to display the total price
        self.total_price_label = tk.Label(self.root, text="Total price:"+str(self.calculate_total_price_cart()))
        self.total_price_label.grid(row=3, column=0)
        # create a button to clear the cart
        self.clear_cart_button = tk.Button(
            self.root, text="Clear cart", command=self.clear_cart)
        self.clear_cart_button.grid(row=3, column=6, padx=10, pady=10)

        self.root.mainloop()
    def calculate_total_price_cart(self):
        total_price = 0.0
        # calculate the total price
        for i in range(len(self.cart)):
            total_price += float(self.cart[i][5])
        return total_price
    def display_bill(self):
        # display the bill
        # check if bill_listbox is empty
        if self.bill_listbox.size() != 0:
            # clear the bill_listbox
            self.bill_listbox.delete(0, tk.END)
        # display the bill
        for items in self.cart:
            self.bill_listbox.insert(tk.END, items)
    def quit(self):
        self.root.destroy()
    def clear_cart(self):
        # clear the cart
        self.cart.clear()
        self.bill_listbox.delete(0, tk.END)
        self.total_price_label.configure(text="Total price:")
    def save_bill(self):
        # save the bill to a file
        pass
    def compute_vat(self):
        # compute the VAT
        ut_price= float(self.unit_price_entry.get())
        vat_rate= float(self.vat_entry.get())
        vat= ut_price * vat_rate
        return round(vat,3)
    def compute_total_price_item(self):
        # compute the total price
        unit_price_with_vat= float(self.unit_price_entry.get())+self.compute_vat()
        total_price_item= unit_price_with_vat * float(self.quantity_entry.get())
        return round(total_price_item,3)
    def add_item(self):
        # add the item to the bill
        data=[]
        data.append(self.item_name_entry.get())
        data.append(self.quantity_entry.get())
        data.append(self.unit_price_entry.get())
        data.append(self.vat_entry.get())
        unit_price_with_vat= round(float(self.unit_price_entry.get())+self.compute_vat(),3)
        data.append(unit_price_with_vat)
        total_price_item= self.compute_total_price_item()
        data.append(total_price_item)
        self.cart.append(data)
        print(self.cart)
        self.display_bill()
        self.total_price_label.configure(text="Total price:"+str(self.calculate_total_price_cart()))
        self.item_name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.unit_price_entry.delete(0, tk.END)
        self.vat_entry.delete(0, tk.END)
        pass


if __name__ == "__main__":
    bill_maker = Bill_Maker_GUI()
    

    pass
