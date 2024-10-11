# Bones/Start of Media Class
import random, string
import tkinter as tk
from tkinter import ttk

class Media:
    def __init__(self, name, media_type, genre, author, in_stock, tags):
        self.name = name
        self.media_type = media_type #Book, Magazine, CD, DVD, etc.
        self.genre = genre
        self.author = author
        self.serial_num = self.generate_serial_num() #function to generate serial number
        self.in_stock = in_stock
        self.tags = tags                             

    # Generates 8 digit serial number    
    def generate_serial_num(self, length=8):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    
    # Prints report of media item
    def print_details(self):
        details = (
            f"Name: {self.name}\n"
            f"Type: {self.media_type}\n"
            f"Genre: {self.genre}\n"
            f"Author: {self.author}\n"
            f"Serial Number: {self.serial_num}\n"
            f"In Stock: {'Yes' if self.in_stock else 'No'}\n"
            f"Tags: {', '.join(f'{key}: {value}' for key, value in self.tags.items())}"
        )

    # Method to add new media items    
    @classmethod
    def add_new_media(cls):
        name = input("Enter the name of the media: ")
        media_type = input("Enter the type of media (Book, Magazine, CD, DVD): ")
        genre = input("Enter the main genre of the media: ")
        author = input("Enter the author of the media: ")
        in_stock = input("Is the media in stock? (yes/no): ").lower() == 'yes' #not sure if this redundent or not. if were adding wouldn't it be in stock?
        tags = {}
        while True:
            key = input("Enter a tag key (or 'done' to finish): ")
            if key.lower() == 'done':
                break
            value = input(f"Enter the value for tag '{key}': ")
            tags[key] = value
        # not sure what exactly we will add here. Maybe things like condition: new or cut: Director's
        # key will store the first, value stores the second.
        return cls(name, media_type, genre, author, in_stock, tags)
class MediaClass(tk.TK):
    def__init__(self):
        super().__init__()
        self.geometry('400x300')
        self.title("Staff Login for Media Creation")

        #create login interface
        self.create_login_interface()
    def create_login_interface(self):
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

    def login(self):
        username = self.username_input.get()
        password = self.password_input.get()

        #check for valid credentials
        if username == "Admin" and password == "Password01":
            self.show_media_creation_interface()
        else:
            messagebox.showerror("Login Error", "Invalid username or password.")
    def show_media_creation_interface(self):
        #clear login interface
        for widget in slef.winfo_children():
            widget.destroy()


        #media title input
        name_label = tk.Label(self, text="Media Name:")
        name_label.grid(column=0, row=0, padx=10, pady=5)

        self.name_input = Text(self, height=1, relief="raised")
        self.name_input.grid(column=1, row=0, padx=10, pady=5)

        #media type input
        media_type_label = tk.Label(self, text="Media Type:")
        media_type_label.grid(column=0, row=1, padx=10, pady=5)

        self.media_type_input = tk.Entry(self, relief="raised")
        self.media_type_input.grid(column=1, row=1, padx=10, pady=5)

        #genre input
        genre_label = tk.Label(self, text="Genre:")
        genre_label.grid(column=0, row=2, padx=10, pady=5)

        self.genre_input = tk.Entry(self, relief="raised")
        self.genre_input.grid(column=1, row=2, padx=10, pady=5)

        #author input
        author_label = tk.Label(self, text="Author:")
        author_label.grid(column=0, row=3, padx=10, pady=5)

        self.author_input = tk.Entry(self, relief="raised")
        self.author_input.grid(column=1, row=3, padx=10, pady=5)

        #in stock input
        in_stock_label = tk.Label(self, text="In Stock (yes/no):")
        in_stock_label.grid(column=0, row=4, padx=10, pady=5)

        self.in_stock_input = tk.Entry(self, relief="raised")
        self.in_stock_input.grid(column=1, row=4, padx=10, pady=5)

        #tags input
        tags_label = tk.Label(self, text="Tags (key:value, separated by commas):")
        tags_label.grid(column=0, row=5, padx=10, pady=5)

        self.tags_input = tk.Entry(self, relief="raised")
        self.tags_input.grid(column=1, row=5, padx=10, pady=5)

        #add media button
        add_media_button = tk.Button(self, text="Add Media", command=self.add_new_media)
        add_media_button.grid(column=0, row=6, columnspan=2, pady=10)

    def add_new_media(self):
        name = self.name_input.get("1.0", "end-1c").strip()
        media_type = self.media_type_input.get().strip()
        genre = self.genre_input.get().strip()
        author = self.author_input.get().strip()
        in_stock = self.in_stock_input.get().strip().lower() == 'yes'
        tags = self.tags_input.get().strip()

        #process tags
        tags_dict = {}
        if tags:
            for tag in tags.split(','):
                key_value = tag.split(':')
                if len(key_value) == 2:
                    tags_dict[key_value[0].strip()] = key_value[1].strip()

        if not name or not media_type or not genre or not author:
            messagebox.showerror("Error", "All fields must be filled in.")
            return

        #create new media instance and add it to the media list
        new_media = Media(name, media_type, genre, author, in_stock, tags_dict)
        new_media.print_details() #print to console

        #clear input fields
        self.name_input.delete("1.0", "end")
        self.media_type_input.delete(0, "end")
        self.genre_input.delete(0, "end")
        self.author_input.delete(0, "end")
        self.in_stock_input.delete(0, "end")
        self.tags_input.delete(0, "end")

        messagebox.showinfo("Success", f"Media '{name}' added successfully!")

#debug
if __name__ == "__main__":
    media_class = MediaClass()
    media_class.mainloop()
