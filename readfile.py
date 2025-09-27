def modify_file(input_file, output_file):
    """Reads content from input_file, modifies it, and writes to output_file."""
    try:
        with open(input_file, "r") as f:
            content = f.read()
        
        # Example modification: make all text uppercase
        modified_content = content.upper()
        
        with open(output_file, "w") as f:
            f.write(modified_content)
        
        print(f"\n✅ Modified content written to '{output_file}'")
    except FileNotFoundError:
        print(f"\n❌ Error: '{input_file}' not found.")
    except Exception as e:
        print(f"\n⚠️ An error occurred: {e}")


def read_file(filename):
    """Reads and prints the content of a file with error handling."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n📄 File content:\n")
            print(content)
    except FileNotFoundError:
        print(f"\n❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"\n❌ Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"\n⚠️ An unexpected error occurred: {e}")


# Main menu
while True:
    print("\n=== File Read & Write Program ===")
    print("1. Read a file")
    print("2. Modify a file and save as new")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        filename = input("Enter the filename to read: ")
        read_file(filename)
    elif choice == "2":
        input_file = input("Enter the input filename: ")
        output_file = input("Enter the output filename: ")
        modify_file(input_file, output_file)
    elif choice == "3":
        print("👋 Exiting program. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
