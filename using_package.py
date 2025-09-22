## TODO: Make a package that can be used to find the best recipe for a person called "recipe_matcher"

from recipe_matcher import people, recipes, find_best_recipe # this package doesnt exist yet. You need to make it :)

for person in people:
    print(f"Hello, {person.name}.\n I am a huge fan of your music, and I'm so excited to help you find the best recipe for your next meal! 😁😋")
    print(find_best_recipe(person, recipes))