import os


def create_project_structure(root_folder, folders, file_name):
    try:
        # Create the project's root folder.
        os.makedirs(root_folder)

        # Create folders and files in each subfolder.
        for folder in folders:
            folder_path = os.path.join(root_folder, folder)
            os.makedirs(folder_path)

            # Create the index.tsx file in each subfolder.
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'w') as f:
                f.write('// file content ' + file_name)

        print("Project structure successfully created!")
    except Exception as e:
        print("An error occurred while creating the project structure:", e)


# Define the structure of the project.
root_folder = "MyProject"
folders = ["folder1", "Folder2", "folder3"]
file_name = "index.tsx"

# Call the function to create the project structure.
create_project_structure(root_folder, folders, file_name)
