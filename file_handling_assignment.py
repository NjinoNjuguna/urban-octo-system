# File Creation
with open("my_file.txt", "w") as file:
    file.write("Hello, this is line 1.\n")
    file.write("12345\n")
    file.write("This is line 3 with some special characters: !@#$%^&*\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("Contents of my_file.txt:")
        print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File reading complete.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is line 4 appended to the existing content.\n")
        file.write("Appended line 5.\n")
        file.write("Another appended line 6.\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File appending complete.")
