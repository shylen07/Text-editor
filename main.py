import os

def edit_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print(f"Current content of the file '{file_path}':")
        print(content)
        
        new_content = input("Enter new content (press Enter to keep existing content): ")
        
        with open(file_path, 'w') as file:
            file.write(new_content)
        print("File updated successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def create_file(file_path):
    try:
        with open(file_path, 'w') as file:
            print("File created successfully.")
    except FileExistsError:
        print(f"File '{file_path}' already exists.")
    except FileNotFoundError:
        print("Invalid file path.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def list_files_and_directories(directory_path):
    try:
        items = os.listdir(directory_path)
        print(f"Contents of directory '{directory_path}':")
        for item in items:
            print(item)
    except FileNotFoundError:
        print("Directory not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def create_directory(directory_path):
    try:
        os.mkdir(directory_path)
        print(f"Directory '{directory_path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_path}' already exists.")
    except FileNotFoundError:
        print("Parent directory not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def rename_file(old_file_path, new_file_name):
    try:
        os.rename(old_file_path, new_file_name)
        print(f"File renamed to '{new_file_name}' successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    while True:
        print("\nMenu:")
        print("1. Edit File")
        print("2. Create File")
        print("3. List Files and Directories")
        print("4. Create Directory")
        print("5. Delete File")
        print("6. Rename File")
        print("7. Quit")

        choice = input("Enter your choice (1-7):")
        
        if choice == '1':
            file_path = input("Enter the file path: ")
            edit_file(file_path)
        elif choice == '2':
            file_path = input("Enter File Name to create: ")
            create_file(file_path)
        elif choice == '3':
            directory_path = input("Enter the directory path: ")
            list_files_and_directories(directory_path)
        elif choice == '4':
            directory_path = input("Enter the directory path to create: ")
            create_directory(directory_path)
        elif choice == '5':
            file_path = input("Enter the file path to delete: ")
            delete_file(file_path)
        elif choice == '6':
            old_file_path = input("Enter the old file path: ")
            new_file_name = input("Enter the new file name: ")
            rename_file(old_file_path, new_file_name)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-7).")

if __name__ == "__main__":
    main()
