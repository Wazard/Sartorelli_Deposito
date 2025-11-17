import random, base_classes

def generate_items():
    items = []

    # Generate 3 random Punto objects
    for _ in range(3):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        items.append(base_classes.Punto(x, y))

    # Sample book data
    titles = ["1984", "Brave New World", "Fahrenheit 451"]
    authors = ["George Orwell", "Aldous Huxley", "Ray Bradbury"]

    # Generate 3 random Libro objects
    for i in range(3):
        pages = random.randint(100, 500)
        items.append(base_classes.Libro(titles[i], authors[i], pages))

    return items

print(generate_items())