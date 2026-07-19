import json
import random


def main():
    with open("./recipes.json", "r") as fh:
        recipe_books = json.load(fh)

    weights = None

    book = random.choices(list(recipe_books.keys()))[0]
    recipe = random.choices(recipe_books[book])[0]

    print(book)
    print(f"Page {recipe}")


if __name__ == "__main__":
    main()
