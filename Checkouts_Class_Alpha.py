import tkinter as tk
from tkinter import ttk
from tkinter import Text, messagebox
from datetime import date, timedelta

# Sample data structure to simulate media and checkouts
media_list = {}
checkouts_list = []


# Simple Media class to simulate media checkouts
class Media:
    @staticmethod
    def is_checked_out(media_unique_id):
        return any(checkout.media_unique_id == media_unique_id for checkout in checkouts_list)

    @staticmethod
    def checkout(media_unique_id):
        media_list[media_unique_id] = False  # Mark media as checked out

    @staticmethod
    def checkin(media_unique_id):
        media_list[media_unique_id] = True  # Mark media as checked in


# Checkout class as defined previously
class Checkout:
    def __init__(self, card_holder_number, media_unique_id, due_date):
        self.card_holder_number = card_holder_number
        self.media_unique_id = media_unique_id
        self.due_date = due_date

    @staticmethod
    def checkout(card_holder_number, media_unique_id, due_date=None):
        # Check if media is available
        if Media.is_checked_out(media_unique_id):
            raise Exception("Media is already checked out.")

        # Set default due date if not specified
        if due_date is None:
            due_date = date.today() + timedelta(days=14)

        # Create checkout record
        new_checkout = Checkout(card_holder_number, media_unique_id, due_date)

        # Save the new checkout record
        checkouts_list.append(new_checkout)

        # Mark media as checked out
        Media.checkout(media_unique_id)

        return new_checkout

    @staticmethod
    def checkin(media_unique_id):
        # Find the checkout record by media unique ID
        for checkout in checkouts_list:
            if checkout.media_unique_id == media_unique_id:
                Media.checkin(media_unique_id)
                checkouts_list.remove(checkout)
                return
        raise Exception("Checkout record not found.")


class CheckoutNew(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x850')
        self.title("Staff Login")

        self.create_login_frame()

    def create_login_frame(self):
        #create login labels and inputs
        username_label = tk.Label(self, text="Username:")
        username_label.grid(column=0, row=0, padx=10, pady=5)

        self.username_input = tk.Entry(self)
        self.username_input.grid(column=1, row=0, padx=10, pady=5)

        password_label = tk.Label(self, text="Password:")
        password_label.grid(column=0, row=1, padx=10, pady=5)

        self.password_input = tk.Entry(self, show="*")
        self.password_input.grid(column=1, row=1, padx=10, pady=5)

        #login button
        login_button = tk.Button(self, text="Login", command=self.login)
        login_button.grid(column=0, row=2, columnspan=2, pady=10)

        #frame to hold checkout functionality (initially hidden)
        self.checkout_frame = None

    def login(self):
        username = self.username_input.get()
        password = self.password_input.get()

        if username == "Admin" and password == "Password01":
            self.show_checkout_frame()
        else:
            messagebox.showerror("Login Error", "Invalid username or password.")

    def show_checkout_frame(self):
        #destroy login widgets
        for widget in self.winfo_children():
            widget.destroy()

        self.geometry('400x850')
        self.title("New Checkout")

        # Checkout form
        check_name_label = tk.Label(self, text="Clerk name:", relief="raised")
        check_name_label.grid(column=0, row=0, padx=10, pady=5)

        self.check_name_input = Text(self, height=1, relief="raised")
        self.check_name_input.grid(column=1, row=0, padx=10, pady=5)
        self.check_name_input.insert(1.0, "Lizzy")  # Placeholder name

        separator = ttk.Separator(self, orient='horizontal')
        separator.grid(column=0, row=2, columnspan=3, pady=10)

        # Card holder number input
        card_holder_label = tk.Label(self, text="Card Holder Number:", relief="raised")
        card_holder_label.grid(column=0, row=3, padx=10, pady=5)

        self.card_holder_input = tk.Entry(self, relief="raised")
        self.card_holder_input.grid(column=1, row=3, padx=10, pady=5)

        # Media unique ID input
        media_id_label = tk.Label(self, text="Media Unique ID:", relief="raised")
        media_id_label.grid(column=0, row=4, padx=10, pady=5)

        self.media_id_input = tk.Entry(self, relief="raised")
        self.media_id_input.grid(column=1, row=4, padx=10, pady=5)

        # Due date input
        due_date_label = tk.Label(self, text="Due Date (YYYY-MM-DD):", relief="raised")
        due_date_label.grid(column=0, row=5, padx=10, pady=5)

        self.due_date_input = tk.Entry(self, relief="raised")
        self.due_date_input.grid(column=1, row=5, padx=10, pady=5)

        # Checkout button
        checkout_button = tk.Button(self, text="Checkout", command=self.process_checkout)
        checkout_button.grid(column=0, row=6, columnspan=2, pady=10)

        # Checkin button
        checkin_button = tk.Button(self, text="Checkin", command=self.process_checkin)
        checkin_button.grid(column=0, row=7, columnspan=2, pady=10)

    def process_checkout(self):
        try:
            card_holder_number = int(self.card_holder_input.get())
            media_unique_id = int(self.media_id_input.get())
            due_date = self.due_date_input.get()
            due_date = date.fromisoformat(due_date) if due_date else None

            # Perform checkout
            checkout = Checkout.checkout(card_holder_number, media_unique_id, due_date)
            messagebox.showinfo("Success", f"Checked out successfully until {checkout.due_date}!")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def process_checkin(self):
        try:
            media_unique_id = int(self.media_id_input.get())

            # Perform check-in
            Checkout.checkin(media_unique_id)
            messagebox.showinfo("Success", "Checked in successfully!")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


# Debug: Create the window locally for rapid testing
if __name__ == "__main__":
    # Initialize media_list with some sample media (available status is True)
    media_list = {1: True, 2: True, 3: True}

    checkout_new = CheckoutNew()
    checkout_new.mainloop()
