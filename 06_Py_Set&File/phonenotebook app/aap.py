from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize an empty phone book dictionary
phone_book = {}

# Function to add a contact
def add_contact(name, phone, email):
    phone_book[name] = {
        'phone': phone,
        'email': email
    }

# Function to search for a contact
def search_contact(name):
    return phone_book.get(name)

# Function to delete a contact
def delete_contact(name):
    if name in phone_book:
        del phone_book[name]

# Main route to display all contacts
@app.route('/')
def index():
    return render_template('index.html', phone_book=phone_book)

# Route to add a new contact
@app.route('/add', methods=['POST'])
def add_contact_route():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    add_contact(name, phone, email)
    return redirect(url_for('index'))

# Route to search for a contact
@app.route('/search', methods=['POST'])
def search_contact_route():
    name = request.form['name']
    contact = search_contact(name)
    return render_template('search.html', name=name, contact=contact)

# Route to delete a contact
@app.route('/delete/<name>')
def delete_contact_route(name):
    delete_contact(name)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/