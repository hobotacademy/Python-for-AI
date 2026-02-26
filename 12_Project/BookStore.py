# pip install customtkinter -> install GUI library

import json
import customtkinter as ctk
import tkinter.messagebox as messagebox


# ------------------------------------------ function to load or create bookstore database
def handle_database():
    try:
        with open(path, "r") as f:
            bookstore = json.load(f)
    except:
        bookstore = {}
        with open(path, "w") as f:
            json.dump(bookstore, f, indent=4)

    return bookstore


# ------------------------------------------ function to add a new book
def add_book():
    name = book_name.get().strip()
    price = book_price.get().strip()
    author = book_author.get().strip()

    # Check if any field is empty
    if not name or not price or not author:
        messagebox.showerror("Error", "All fields must be filled!")
        return

    # Validate price is a number
    try:
        price = float(price)  # Convert price to a float
    except ValueError:
        messagebox.showerror("Error", "Price must be a numeric value!")
        return

    if name not in database:
        database[name] = {
            "price": price,
            "author": author
        }

        with open(path, "w") as f:
            json.dump(database, f, indent=4)

        book_name.delete(0, ctk.END)
        book_price.delete(0, ctk.END)
        book_author.delete(0, ctk.END)

        messagebox.showinfo("Book Added", f"The book '{name}' was added successfully.")
    else:
        messagebox.showinfo("Book Exists", f"The book '{name}' already exists.")


# ------------------------------------------ function to search for a book
def search_book():
    query = search_entry.get().strip()
    # Clear previous result
    search_result_label.configure(text="")

    if not query:
        search_result_label.configure(text="Please enter a search term.", text_color="red")
        return

    found = False
    result_text = ""
    for book_name, details in database.items():
        if query.lower() in book_name.lower():
            result_text += f"{book_name} - Price: {details['price']}, Author: {details['author']}\n"
            found = True

    if not found:
        search_result_label.configure(text="No matching books found.", text_color="red")
    else:
        search_result_label.configure(text=result_text.strip(), text_color="green")


# ------------------------------------------ load bookstore database with specified path
path = "./bookstore.json"
database = handle_database()


# ------------------------------------------ appearance & theme
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


# ------------------------------------------ application
app = ctk.CTk()
app.title("Book Store")
app.geometry("800x400")

# Create a tabview and place it in the application
tabview = ctk.CTkTabview(app, width=760, height=350)
tabview.place(x=20, y=20)

t1 = tabview.add("Add")
t2 = tabview.add("Search")

# ------------------------------------------ tabview 1 -> Add books to database
add_label = ctk.CTkLabel(t1, text="Add Book To Database", font=("Arial", 18))
add_label.place(x=20, y=20)

book_name = ctk.CTkEntry(t1, placeholder_text="Book Name", width=700, height=40)
book_name.place(x=20, y=70)

book_price = ctk.CTkEntry(t1, placeholder_text="Book Price", width=700, height=40)
book_price.place(x=20, y=120)

book_author = ctk.CTkEntry(t1, placeholder_text="Book Author", width=700, height=40)
book_author.place(x=20, y=170)

add_button = ctk.CTkButton(t1, text="Add Book", command=add_book, width=120)
add_button.place(x=600, y=250)

# ------------------------------------------ tabview 2 -> Search for a book
search_label = ctk.CTkLabel(t2, text="Search Book", font=("Arial", 18))
search_label.place(x=20, y=20)

search_entry = ctk.CTkEntry(t2, placeholder_text="Enter Book Name", width=550)
search_entry.place(x=20, y=70)

search_button = ctk.CTkButton(t2, text="Search", command=search_book, width=120)
search_button.place(x=600, y=70)

search_result_label = ctk.CTkLabel(t2, text="", font=("Arial", 14), wraplength=700, justify="left")
search_result_label.place(x=20, y=170)

app.mainloop()