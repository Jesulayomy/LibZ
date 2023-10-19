import requests
import os
import json

names = [
    "Atreus", "Athena", "Ares", "Aphrodite", "Apollo", "Artemis", "Achilles", "Ariadne", "Aeneas", "Aether",
    "Ban", "Bai", "Bao", "Bing", "Bo", "Cai", "Cao", "Chang", "Chao", "Chen", "Cheng", "Chin", "Chou", "Chu",
    "Delilah", "Dorothy", "Daphne", "Diana", "Doris", "Fiona", "Faye", "Faith", "Felicity", "Fern", "Flora",
    "John", "Jane", "Jack", "Jill", "James", "Jenny", "Jade", "Jasper", "Jasmine", "Jared", "Jocelyn", "Jude",
    "Emma", "Ethan", "Emily", "Elijah", "Elizabeth", "Evan", "Eva", "Eliana", "Ezra", "Elena", "Elias", "Eleanor",
    "Griamore", "Gowther", "Gilthunder", "Gustaf", "Gannon", "Gareth", "Gavin", "Gawain", "Galahad", "Galahalt",
    "Hannah", "Haley", "Hazel", "Heather", "Helen", "Holly", "Hope", "Harmony", "Haven", "Honor", "Hermione",
    "Indra", "Iris", "Ivy", "Isabella", "Isaac", "Ian", "Irene", "Iris", "Ivy", "Isabella", "Isaac", "Ian", "Irene",
]

surnames = [
    "Kane", "Kang", "Kao", "Kato", "Kawaguchi", "Kawamoto", "Kawamura", "Kawano", "Kawasaki", "Kawashima",
    "Loyd", "Matthew", "Morgan", "Morrison", "Moss", "Mullins", "Munoz", "Murphy", "Murray", "Myers", "Nash",
    "Nelson", "Newman", "Newton", "Nguyen", "Nichols", "Nicholson", "Nielsen", "Nieves", "Nixon", "Noble",
    "Ochoa", "Oconnor", "Odom", "Oliver", "Olsen", "Olson", "Oneal", "Oneill", "Orr", "Ortega", "Ortiz", "Osborn",
    "Owen", "Owens", "Pace", "Pacheco", "Padilla", "Page", "Palmer", "Park", "Parker", "Parks", "Parrish", "Parsons",
    "Quinn", "Ramirez", "Ramos", "Ramsey", "Randall", "Randolph", "Rasmussen", "Ratliff", "Ray", "Raymond", "Reed",
    "Santana", "Santiago", "Santos", "Sargent", "Saunders", "Savage", "Sawyer", "Schmidt", "Schneider", "Schroeder",
    "Tanner", "Taylor", "Terrell", "Terry", "Thomas", "Thompson", "Thornton", "Tillman", "Todd", "Torres", "Townsend",
    "Underwood", "Valdez", "Valencia", "Valentine", "Valenzuela", "Vance", 
]

bookNames = [
    "To Kill a Mockingbird",
    "1984",
    "The Great Gatsby",
    "One Hundred Years of Solitude",
    "Brave New World",
    "The Catcher in the Rye",
    "Fahrenheit 451",
    "The Lord of the Rings",
    "Pride and Prejudice",
    "The Hobbit",
    "Moby-Dick",
    "War and Peace",
    "The Odyssey",
    "Crime and Punishment",
    "The Grapes of Wrath",
    "The Old Man and the Sea",
    "The Brothers Karamazov",
    "The Count of Monte Cristo",
    "Frankenstein",
    "Wuthering Heights",
    "Dracula",
    "Alice's Adventures in Wonderland",
    "The Picture of Dorian Gray",
    "The Adventures of Sherlock Holmes",
    "Anna Karenina",
    "Les Misérables",
    "The Sun Also Rises",
    "The Scarlet Letter",
    "A Tale of Two Cities",
    "Moby-Dick",
    "The Canterbury Tales",
    "Hamlet",
    "The Divine Comedy",
    "Ulysses",
    "The Wind in the Willows",
    "Don Quixote",
    "The Iliad",
    "The Name of the Wind",
    "The Road",
    "The Shining",
    "The Book Thief",
    "The Girl with the Dragon Tattoo",
    "The Alchemist",
    "The Help",
    "The Kite Runner",
    "A Game of Thrones",
    "The Da Vinci Code",
    "The Pillars of the Earth",
    "The Hunger Games",
    "The Color Purple",
    "The Handmaid's Tale",
    "The Stand",
    "The Outsiders",
    "The Fault in Our Stars",
    "The Giver",
    "The Secret Garden",
    "The Little Prince",
    "The Lord of the Flies",
    "The Road",
    "The Silence of the Lambs",
    "The Martian",
    "The Goldfinch",
    "The Nightingale",
    "The Chronicles of Narnia",
    "The Time Traveler's Wife",
    "The Help",
    "The Joy Luck Club",
    "The Glass Castle",
    "The Immortal Life of Henrietta Lacks",
    "The Girl on the Train",
    "The Thirteenth Tale",
    "The Lovely Bones",
    "The Book Thief",
    "The Light Between Oceans",
    "The Night Circus",
    "The Great Alone",
    "The Silent Patient",
    "The Water Dancer",
    "The Dutch House",
    "The Vanishing Half",
    "The Push",
    "The Four Winds",
    "The Giver of Stars",
    "The Midnight Library",
    "The Paper Palace",
    "The Sanatorium",
    "The Last House on Needless Street",
    "The Burning Girls",
    "The Push",
    "The Sanatorium",
    "The Last House on Needless Street",
    "A tale of two cities",
    "Why you dream code",
]


PHONE = 2341234567890


def create_user(pos: int) -> dict:
    """ Creates a user dict for upload """
    user_data ={
        "first_name": names[pos],
        "last_name": surnames[pos],
        "email": f"{names[pos]}{surnames[pos]}@gmail.com",
        "password": f"{names[pos]}{surnames[pos]}",
        "gender": "male" if pos % 2 == 0 else "female",
        "date_of_birth": "2000-02-17T22:46:38.883037",
        "display_name": f"{names[pos]}{pos}",
        "phone": f"+{PHONE + pos}"
    }
    return user_data


def create_book(pos: int, user_folder: str) -> dict:
    """ creates the book's Dict for upload """
    book_data = {
        "name": bookNames[pos],
        "author": f"{surnames[pos]}",
        "public": True,
        "user_folder": user_folder,
        "description": f"This is a description for {bookNames[pos]} uploaded by {names[pos]}{pos}",
    }
    return book_data


def post_user(pos: int = 0, session: requests.Session = None):
    """ creates a user through the post request """
    user_data = create_user(pos)
    # data = {"data": json.dumps(user_data)}
    response = session.post("http://127.0.0.1:5000/api/users", data=user_data)
    if response.status_code == 409:
        response = session.post("http://127.0.0.1:5000/auth/login", data=user_data)

    return response.json()


def post_book(pos: int = 0, user_folder: str = "", session: requests.Session = None):
    """ creates a book through the post request """
    book_data = create_book(pos, user_folder)
    book = "Bird.pdf" if (pos + 2) % 2 == 0 else "1984.pdf"
    file_path = os.path.join(os.getcwd(), book)

    
    with open(file_path, "rb") as book_file:
        files = {"book_file": (book, book_file)}
        response = session.post(f"http://127.0.0.1:5000/api/books", data=book_data, files=files)

    return response.json()


def populate():
    """ Populates the database """
    num = int(input("How many users do you want to create? "))
    resp = requests.get("http://127.0.0.1:5000/api/status")
    print(resp.json())
    resp = requests.get("http://127.0.0.1:5000/api/stats")
    print(resp.json())
    for pos in range(0, num):
        with requests.Session() as session:
            user_data = post_user(pos, session)
            book_data = post_book(pos, user_data["folder"], session)
            print(f"{user_data['display_name']} successfully posted {book_data['name']}")

    resp = requests.get("http://127.0.0.1:5000/api/stats")
    print(resp.json())


populate()

# # create user
# user_data = {
#     "first_name": "John",
#     "last_name": "Doe",
#     "email": "johnDdoe@gmail.com",
#     "password": "password",
#     "gender": "male",
#     "date_of_birth": "2000-02-17T22:46:38.883037",
#     "display_name": "BigJohn"
# }

# data = {"data": json.dumps(user_data)}

# response = requests.post("http://127.0.0.1:5000/api/users", data=user_data)
# try:
#     user_folder = response.json()["folder"]
# except Exception:
#     pass

# # upload book
# book_data = {
#     "name": "A new Book",
#     "author": "John Doe",
#     "public": True,
#     "user_folder": user_folder
# }

# data = {"data": json.dumps(book_data)}

# file_path = os.path.join(os.getcwd(), "ANewBook.pdf")

# with open(file_path, "rb") as book_file:
#     files = {"book_file": ("ANewBook.pdf", book_file)}
#     response = requests.post(f"http://127.0.0.1:5000/api/books", data=book_data, files=files)

# if response.status_code == 201:
#     print("Book created successfully.")
#     print("Response data:", response.json())
# else:
#     print("Failed to create the book. Status code:", response.status_code)
#     print("Response content:", response.text)
