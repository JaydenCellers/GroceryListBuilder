from recipe_manager import add_recipe, list_recipes

def main():
    while True:
        print("\nRecipe Manager")
        print("1. Add Recipe")
        print("2. List Recipes")
        print("3. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            add_recipe()
        elif choice == '2':
            list_recipes()
        elif choice == '3':
            print("Exiting the Recipe Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()