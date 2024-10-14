import zipfile

def crack_zip(zip_file, dictionary):
    with open(dictionary, 'r') as f:
        for line in f:
            password = line.strip()  # Remove newline and any trailing spaces
            try:
                zip_file.extractall(pwd=password.encode())  # Attempt to extract with the current password
                print(f"Password found: {password}")  # Print the found password
                return password  # Return the found password
            except (RuntimeError, zipfile.BadZipFile):
                # RuntimeError: incorrect password; BadZipFile: corrupt zip file (you can handle this if needed)
                continue
    print("Password not found.")  # Print when no password was found

# Use the function to attempt cracking the ZIP file


zip_file_path = input('Enter your zip file name: ')
dictionary_file_path = input('Enter your password file: ')


try:
    zip_file = zipfile.ZipFile(zip_file_path)
    crack_zip(zip_file, dictionary_file_path)
except FileNotFoundError:
    print(f"The file {zip_file_path} or {dictionary_file_path} does not exist.")
