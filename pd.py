def write_name_to_file(filename, name):
    try:
        with open(filename, 'a') as file:
            file.write(name + '\n')
        print("Tavs vārds tika pierakstīts failam.")
    except PermissionError:
        print(f"Tev nav atļauja te rakstīt '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
name = input("Ievadi savu vārdu : ")
filename = "user_names.txt"
write_name_to_file(filename, name)

