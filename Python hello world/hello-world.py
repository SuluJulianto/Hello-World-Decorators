import random

# List of decorative symbols and languages
decor_symbols = ["=", "^", ":", "~", "*", "+", "_", "<", ">", "'"]
languages = ["English", "Indonesian", "Japanese", "French", "Portuguese", "Dutch", "Filipino", "Malay", "Korean",
             "Italian", "Latin", "Arabic", "Armenian", "Danish", "Finnish", "German", "Hindi", "Spanish", "Latvian",
             "Irish", "Zulu", "Greek", "Russian", "Serbian", "Turkish", "Kannada", "Thai", "Swahili", "Chinese"]

# List of greetings in different languages
greetings = [
    "Hello World", "Halo Dunia", "Ohayō Sekai", "Bonjour le Monde", "Olá Mundo", "Hallo Wereld", "Kumusta Mundo",
    "Hai Dunia", "Annyeong Sesang", "Ciao Mondo", "Salve Mundi", "Marhabaan Bialealam", "Barev Ashkharh",
    "Hej Verden", "Hei Maailma", "Hallo Welt", "Namaste Duniya", "Hola Mundo", "Sveika pasaule", "Dia Duit Domhan",
    "Sawubona Mhlaba", "Gei sou Kōsme", "Privet Mir", "Zdravo Svete", "Merhaba Dunya", "Namaste Prapancha",
    "Sawasdee Chow Lok", "Salamu, Dunia", "Nihao Shijie"
]


def random_number(limit):
    return random.randint(0, limit - 1)


def decorate(func, lang, index, index2, spacing):
    def wrapper():
        print(" " * spacing + decor_symbols[index] * 5 + " " + lang + " " + decor_symbols[index] * 5)
        func(spacing, index2)
        print(" " * spacing + decor_symbols[index] * (10 + len(lang)) + "\n")

    return wrapper


def display_text(spaces, idx):
    print(" " * spaces + greetings[idx])


# Loop through languages to display greetings with decorations
for i in range(len(languages)):
    symbol_index = random_number(len(decor_symbols))
    space = 20 if i % 2 == 0 else 1
    decorated_greeting = decorate(display_text, languages[i], symbol_index, i, space)
    decorated_greeting()
