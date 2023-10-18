import requests
import os
import json


# create user
user_data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "johnDdoe@gmail.com",
    "password": "password",
    "gender": "male",
    "date_of_birth": "2000-02-17T22:46:38.883037",
    "display_name": "BigJohn"
}

data = {"data": json.dumps(user_data)}

response = requests.post("http://127.0.0.1:5000/api/users", data=user_data)
try:
    user_folder = response.json()["folder"]
except Exception:
    pass

# upload book
book_data = {
    "name": "A new Book",
    "author": "John Doe",
    "public": True,
    "user_folder": user_folder
}

data = {"data": json.dumps(book_data)}

file_path = os.path.join(os.getcwd(), "ANewBook.pdf")

with open(file_path, "rb") as book_file:
    files = {"book_file": ("ANewBook.pdf", book_file)}
    response = requests.post(f"http://127.0.0.1:5000/api/books", data=book_data, files=files)

if response.status_code == 201:
    print("Book created successfully.")
    print("Response data:", response.json())
else:
    print("Failed to create the book. Status code:", response.status_code)
    print("Response content:", response.text)
