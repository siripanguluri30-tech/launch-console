def main():
    print("Welcome to the Launch Console!")

    user_name = input("Please enter your name: ")
    print(f"\nHello, {user_name}! Great to have you here.\n")

    while True:
        print("--- MENU ---")
        print("1. About Me")
        print("2. My Goals")
        print("3. Favorite Project")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            print(
                f"\nAbout Me: Hi my name is Sowmya and i'm excited to start the Fall C2C Coursework!!"
            )
        elif choice == "2":
            print(
                f"\nMy Goals: Graduate highschool, learn to crochet and become an activist!"
            )
        elif choice == "3":
            print(
                f"\nFavorite Project: Building interactive CLI consoles like this one!"
            )
        elif choice == "4":
            print(f"\nGoodbye, {user_name}! Thanks for viewing my page!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

        print("\n" + "=" * 30 + "\n")


if __name__ == "__main__":
    main()