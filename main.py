from recipe_manager import add_recipe, list_recipes, select_recipes, view_recipe_details, edit_recipe, delete_recipe

def main():
    while True:
        print("\nRecipe Manager")
        print("1. Add Recipe")
        print("2. List Recipes")
        print("3. Select Recipes for Shopping List")
        print("4. View Recipe Details")
        print("5. Edit Recipe")
        print("6. Delete Recipe")
        print("7. Exit")

        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            add_recipe()
        elif choice == '2':
            list_recipes()
        elif choice == '3':
            select_recipes()
        elif choice == '4':
            view_recipe_details()
        elif choice == '5':
            edit_recipe()
        elif choice == '6':
            delete_recipe()
        elif choice == '7':
            print("Exiting the Recipe Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()