class Recipe:
    def __init__(self, name, ingredients, instructions, time):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.time = time

    def __str__(self):
        return f"{self.name}: {self.ingredients} -> {self.instructions}"

recipes = [
    Recipe("Spaghetti Carbonara", ["spaghetti", "egg", "parmesan", "bacon"], "Boil the spaghetti. Fry the bacon. Mix the egg and parmesan. Mix the spaghetti and bacon. Add the egg and parmesan.", 30),
    Recipe("Chicken Curry", ["chicken", "curry powder", "coconut milk", "onion", "carrots"], "Fry the onion. Add the chicken and curry powder. Add the coconut milk. Simmer for 45 minutes.", 45),
    Recipe("Beef Stew", ["beef", "carrots", "potatoes", "onion"], "Fry the onion. Add the beef and carrots. Add the potatoes. Simmer for 2 hours.", 120),
    Recipe("Salad", ["lettuce", "tomato", "cucumber", "olive"], "Mix the lettuce, tomato, cucumber, and olive. Add salt and pepper to taste.", 15),
    Recipe("Pizza", ["dough", "tomato sauce", "cheese", "pepperoni"], "Roll the dough. Add the tomato sauce and cheese. Add the pepperoni. Bake for 15 minutes.", 15),
    Recipe("Soup", ["chicken", "vegetables", "noodles"], "Boil the chicken and vegetables. Add the noodles. Simmer for 60 minutes.", 60),
    Recipe("Sirniki", ["eggs", "flour", "milk", "sugar"], "Mix the eggs, flour, milk, and sugar. Bake for 5 minutes.", 5),
    Recipe("Pancakes", ["flour", "eggs", "milk", "sugar"], "Mix the flour, eggs, milk, and sugar. Bake for 5 minutes.", 5),
    Recipe("disaster😈", ["evil intentions", "chaotic energy", "destructive force", "2 teaspoons of sugar"], "Mix the evil intentions, chaotic energy, and destructive force. Bake for 666 minutes (sign of the apocalypse). Sprinkle with the sugar.", 666),
    Recipe("Waffles", ["flour", "eggs", "milk", "sugar"], "Mix the flour, eggs, milk, and sugar. Bake for 8 minutes.", 8),
    Recipe("French Toast", ["bread", "eggs", "milk", "sugar"], "Mix the bread, eggs, milk, and sugar. Bake for 6 minutes.", 6),
    Recipe("Omelette", ["eggs", "milk", "salt", "pepper"], "Beat the eggs. Add the milk, salt, and pepper. Fry the eggs. Add the milk, salt, and pepper. Fry the eggs. Add the milk, salt, and pepper. Fry the eggs.", 10),
]

class Person:
    def __init__(self, name, ingredients, time_preference):
        self.name = name
        self.ingredients = ingredients # the ingredients the person has
        self.time_preference = time_preference


    def __str__(self):
        return f"{self.name}: {self.recipes}"

people = [ # band members from the incredibly awesome band "Nervy" 😎
    Person("Zhenya Milkovskiy", ["eggs", "flour", "milk", "sugar"], 30),
    Person("Dima Dudka", ["chicken", "curry powder", "coconut milk", "onion"], 60),
    Person("Anton Nizhenko", ["beef", "carrots"], 60),
    Person("Vlad Zaychenko", ["lettuce", "tomato"], 15),
    Person("🦹🏻‍♂️ PROFESSOR X 🦹🏻‍♂️", ["evil intentions", "chaotic energy", "DESIRE TO DESTROY", "ABILITY TO CONTROL TIME"], 666),
]
def find_best_recipe(person, recipes):
    best_recipe = None
    best_score = 0
    for recipe in recipes:
        score = 0
        for ingredient in person.ingredients:
            if ingredient in recipe.ingredients and recipe.time <= person.time_preference:
                score += 1
        if score > best_score:
            best_score = score
            best_recipe = recipe
    return f"your best recipe is {best_recipe.name} with a score of {best_score}"


