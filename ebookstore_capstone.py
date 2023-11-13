import sqlite3

# Create the database
db = sqlite3.connect('ebookstore_db')
cursor = db.cursor()

print('Database Created!\n')

# Create the table structure 
cursor.execute('''
                CREATE TABLE IF NOT EXISTS books(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title VARCHAR,
                    author VARCHAR,
                    qty INTEGER);
''')

db.commit()
print('Table Created!\n')

# Create function that inserts data into a databse
def insert_data():
    book_data = [
        (3001, "A Tale of Two Cities", "Charles Dickens", 30), 
        (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40), 
        (3003, "The Lion, the Witch, and the Wardrobe", "C.S. Lewis", 25),
        (3004, "The Lord of the Rings", "J.R.R Tolkien", 37), 
        (3005, "Alice in Wonderland", "Lewis Caroll", 12)]
    
    cursor.executemany('''
                    INSERT OR REPLACE INTO books(id, title, author, qty)
                    VALUES(?,?,?,?)
    ''', book_data)
        
    db.commit()
    print("Data successfully added!")
    
insert_data()

# Create a function that displays all books
def display_data():
    cursor.execute('''
        SELECT * FROM books
    ''')
    book_data = cursor.fetchall()
    print(book_data)
    
# Create a function that allows the user to enter a new book into the existing database
def enter_book():
    title_ = input("Please enter the 'title' of your book: ")
    author_ = input("Please enter the 'author' of your book: ")
    qty_ = int(input("Please enter the 'quantity' of this book: "))
    
    cursor.execute('''
                    INSERT INTO books(title, author, qty)
                    VALUES(?,?,?)
    ''', (title_, author_, qty_))
        
    db.commit()
    print("Book successfully added!")
    
# Create a function that allows the user to update various attributes of a book
def update_book():
    display_data()
    
    user_option = int(input("Please choose the 'id' of the book you want to update from the displayed books above: "))
    
    updated_title = input("Please enter updated title: ")
    updated_author = input("Please enter updated author: ")
    updated_qty = int(input("Please enter updated quantity: "))
    
    cursor.execute('''
        UPDATE books SET title = ?, author = ?, qty = ? WHERE id = ?
    ''', (updated_title, updated_author, updated_qty, user_option,))
    
    db.commit() 
    print("Database Updated successfully!")

# Create a function that allows the user to delete a book based on the 'id' of the book entered
def delete_book():
    display_data()
    
    user_option = int(input("Please choose the 'id' of the book you want to delete: "))
    
    cursor.execute('''
        DELETE FROM books WHERE id = ?
    ''', (user_option,))
    
    db.commit() 
    print("Data deleted successfully!")
    
# Create a function that allows the user to search for a book based on the 'title' of the book entered
def search_book():
    search_title = input("Please enter the title of the book you want to search for: ")
    
    cursor.execute('''
        SELECT * FROM books WHERE title = ?
        ''', (search_title,))
    
    data_ = cursor.fetchmany()
    print(data_)

# Menu options
while True:
    print("\nMenu:")
    menu = input('''1. Display all books
2. Enter book
3. Update book
4. Delete book
5. Search book
0. Exit
Please enter a menu option: ''')   

    # 'if, elif, else' statements used to differentiate the various menu options and their allocated functions
    if menu == '1':
        display_data()
    elif menu == '2':
        enter_book()
    elif menu == '3':
        update_book()
    elif menu == '4':
        delete_book()
    elif menu == '5':
        search_book()
    elif menu == '0':
        print("Ebookstore closing, goodbye...")
        break
    else:
        print("Invalid menu option, please try again.")