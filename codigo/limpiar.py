import os

# Specify the directory where the files are located
directory = "D:\\cositas\\NeoClean_Actualizator"

# List of files to be deleted
files_to_delete = ["lista_bacha.csv", "lista_vieja.csv"]

# Iterate over the files in the directory
for filename in os.listdir(directory):
    # Check if the file is in the list of files to be deleted
    if filename in files_to_delete:
        # If it is, delete the file
        os.remove(os.path.join(directory, filename))
        print(f"{filename} has been deleted.")