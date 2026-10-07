word_dict = {}

while True:
    print("\n--- Dictionary Menu ---")
    print("1. Add a Word")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        word = input("Enter word: ").strip().lower()
        if not word:
            print("Word cannot be empty.")
        elif word in word_dict:
            print(f"'{word}' already exists. Use update option to change its meaning.")
        else:
            meaning = input("Enter meaning: ").strip()
            word_dict[word] = meaning
            print(f"'{word}' added successfully.")

    elif choice == "2":
        word = input("Enter word to search: ").strip().lower()
        if word in word_dict:
            print(f"Meaning of '{word}': {word_dict[word]}")
        else:
            print(f"'{word}' not found in the dictionary.")

    elif choice == "3":
        if not word_dict:
            print("Dictionary is empty.")
        else:
            print("\nStored Words and Meanings:")
            for word, meaning in word_dict.items():
                print(f"• {word.capitalize()}: {meaning}")

    elif choice == "4":
        word = input("Enter word to update: ").strip().lower()
        if word in word_dict:
            new_meaning = input("Enter new meaning: ").strip()
            word_dict[word] = new_meaning
            print(f"Updated successfully! '{word}': {word_dict[word]}")
        else:
            print(f"Error: '{word}' does not exist in the dictionary.")

    elif choice == "5":
        word = input("Enter word to delete: ").strip().lower()
        if word in word_dict:
            confirm = input(f"Are you sure you want to delete '{word}'? (y/n): ").strip().lower()
            if confirm == "y":
                del word_dict[word]
                print(f"'{word}' has been deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print(f"Error: '{word}' not found in the dictionary.")

    elif choice == "6":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")


#      output:--- Dictionary Menu ---
# 1. Add a Word
# 2. Search for Meaning
# 3. Display All Words
# 4. Update Meaning
# 5. Delete Word
# 6. Exit
# Enter your choice (1-6): 1
# Enter word: algorithm
# Enter meaning: A step-by-step procedure for solving a problem.
# 'algorithm' added successfully.

# --- Dictionary Menu ---
# 1. Add a Word
# 2. Search for Meaning
# 3. Display All Words
# 4. Update Meaning
# 5. Delete Word
# 6. Exit
# Enter your choice (1-6): 1
# Enter word: variable
# Enter meaning: A named storage location in memory.
# 'variable' added successfully.

# --- Dictionary Menu ---
# 1. Add a Word
# 2. Search for Meaning
# 3. Display All Words
# 4. Update Meaning
# 5. Delete Word
# 6. Exit
# Enter your choice (1-6): 2
# Enter word to search: algorithm
# Meaning of 'algorithm': A step-by-step procedure for solving a problem.

# --- Dictionary Menu ---
# 1. Add a Word
# 2. Search for Meaning
# 3. Display All Words
# 4. Update Meaning
# 5. Delete Word
# 6. Exit
# Enter your choice (1-6): 4
# Enter word to update: variable
# Enter new meaning: A reserved memory location to store values.
# Updated successfully! 'variable': A reserved memory location to store values.

# --- Dictionary Menu ---
# 1. Add a Word
# 2. Search for Meaning
# 3. Display All Words
# 4. Update Meaning
# 5. Delete Word
# 6. Exit
# Enter your choice (1-6): 3

# Stored Words and Meanings:
# • Algorithm: A step-by-step procedure for solving a problem.
# • Variable: A reserved memory location to store values.

# --- Dictionary Menu ---
# 1. Add a Word
# 2. Search for Meaning
# 3. Display All Words
# 4. Update Meaning
# 5. Delete Word
# 6. Exit
# Enter your choice (1-6): 5
# Enter word to delete: algorithm
# Are you sure you want to delete 'algorithm'? (y/n): y
# 'algorithm' has been deleted.

# --- Dictionary Menu ---
# 1. Add a Word
# 2. Search for Meaning
# 3. Display All Words
# 4. Update Meaning
# 5. Delete Word
# 6. Exit
# Enter your choice (1-6): 6
# Exiting program. Goodbye!