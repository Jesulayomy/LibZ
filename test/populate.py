""" This module uploads some models to the database """
import os
import requests

names = [
    "Atreus", "Athena", "Ares", "Aphrodite", "Apollo", "Artemis",
    "Achilles", "Ariadne", "Aeneas", "Aether",
    "Ban", "Bai", "Bao", "Bing", "Bo", "Cai", "Cao",
    "Chang", "Chao", "Chen", "Cheng", "Chin", "Chou", "Chu",
    "Delilah", "Dorothy", "Daphne", "Diana", "Doris", "Fiona",
    "Faye", "Faith", "Felicity", "Fern", "Flora",
    "John", "Jane", "Jack", "Jill", "James", "Jenny", "Jade",
    "Jasper", "Jasmine", "Jared", "Jocelyn", "Jude",
    "Emma", "Ethan", "Emily", "Elijah", "Elizabeth", "Evan",
    "Eva", "Eliana", "Ezra", "Elena", "Elias", "Eleanor",
    "Griamore", "Gowther", "Gilthunder", "Gustaf", "Gannon",
    "Gareth", "Gavin", "Gawain", "Galahad", "Galahalt",
    "Hannah", "Haley", "Hazel", "Heather", "Helen", "Holly",
    "Hope", "Harmony", "Haven", "Honor", "Hermione",
    "Indra", "Iris", "Ivy", "Isabella", "Isaac", "Ian",
    "Irene", "Iris", "Ivy", "Isabella", "Isaac", "Ian", "Irene",
]

surnames = [
    "Kane", "Kang", "Kao", "Kato", "Kawaguchi", "Kawamoto",
    "Kawamura", "Kawano", "Kawasaki", "Kawashima",
    "Loyd", "Matthew", "Morgan", "Morrison", "Moss",
    "Mullins", "Munoz", "Murphy", "Murray", "Myers", "Nash",
    "Nelson", "Newman", "Newton", "Nguyen", "Nichols",
    "Nicholson", "Nielsen", "Nieves", "Nixon", "Noble",
    "Ochoa", "Oconnor", "Odom", "Oliver", "Olsen", "Olson",
    "Oneal", "Oneill", "Orr", "Ortega", "Ortiz", "Osborn",
    "Owen", "Owens", "Pace", "Pacheco", "Padilla", "Page",
    "Palmer", "Park", "Parker", "Parks", "Parrish", "Parsons",
    "Quinn", "Ramirez", "Ramos", "Ramsey", "Randall", "Randolph",
    "Rasmussen", "Ratliff", "Ray", "Raymond", "Reed",
    "Santana", "Santiago", "Santos", "Sargent", "Saunders",
    "Savage", "Sawyer", "Schmidt", "Schneider", "Schroeder",
    "Tanner", "Taylor", "Terrell", "Terry", "Thomas",
    "Thompson", "Thornton", "Tillman", "Todd", "Torres", "Townsend",
    "Underwood", "Valdez", "Valencia", "Valentine",
    "Valenzuela", "Vance",
]

book_names = [
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
    user_data = {
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


def create_book(pos: int, user_pos: int, user_folder: str) -> dict:
    """ creates the book's Dict for upload """
    book_data = {
        "name": book_names[pos],
        "author": f"{surnames[user_pos]}",
        "public": True,
        "user_folder": user_folder,
        "description": f"This is a description for {book_names[pos]} uploaded by {names[user_pos]}{user_pos}",
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


def post_book(
        book_pos: int = 0,
        user_pos: int = 0,
        user_folder: str = "",
        session: requests.Session = None):
    """ creates a book through the post request """
    book_data = create_book(book_pos, user_pos, user_folder)
    book = "Bird.pdf" if (book_pos + 2) % 2 == 0 else "StreetFest.pdf"
    file_path = os.path.join(os.getcwd(), book)
    book_name = book_names[book_pos].replace(" ", "")

    with open(file_path, "rb") as book_file:
        files = {"book_file": (book_name + ".pdf", book_file)}
        response = session.post("http://127.0.0.1:5000/api/books", data=book_data, files=files)

    return response.json()


def populate():
    """ Populates the database """
    usrs = int(input("How many users do you want to create? "))
    bks = int(input("How many books do you want to create for each user? "))
    resp = requests.get("http://127.0.0.1:5000/api/status", timeout=60)
    print(resp.json())
    resp = requests.get("http://127.0.0.1:5000/api/stats", timeout=60)
    print(resp.json())
    for user_pos in range(0, usrs):
        with requests.Session() as session:
            user_data = post_user(user_pos, session)
            for idx in range(user_pos * bks, (user_pos + 1) * bks):
                book_data = post_book(idx, user_pos, user_data["folder"], session)
                print(f"{user_data['display_name']} successfully posted {book_data['name']}")

    resp = requests.get("http://127.0.0.1:5000/api/stats", timeout=60)
    print(resp.json())


populate()
