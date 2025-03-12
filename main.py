import pyjokes

def tell_joke(lang="en", joke_type="neutral"):
    print(pyjokes.get_joke(language=lang, category=joke_type))

if __name__ == "__main__":
    lang = input("Choisissez une langue (en, de, es, it, gl): ")
    joke_type = input("Choisissez une catégorie de blague (neutral, chuck, all): ")
    tell_joke(lang, joke_type)


print("Bienvenue sur le générateur de blagues !")
lang = input("Sélectionnez une langue : ")
category = input("Sélectionnez une catégorie : ")
print(pyjokes.get_joke(language=lang, category=category))