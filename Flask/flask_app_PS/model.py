import json


def load_db():
    with open("flashcards_db.json") as fhnad:
        return json.load(fhnad)


def save_db():
    with open("flashcards_db.json", "w") as fhand:
        return json.dump(db, fhand)


db = load_db()
