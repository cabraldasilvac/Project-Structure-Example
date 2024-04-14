import os

def create_project_structure(root_folder, folders, file_contents):
    try:
        # Create the project's root folder.
        os.makedirs(root_folder, exist_ok=True)

        # Create folders and files in each subfolder.
        for folder in folders:
            folder_path = os.path.join(root_folder, folder)
            os.makedirs(folder_path, exist_ok=True)

            # Create files in each subfolder.
            for file_name, content in file_contents.items():
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'w') as f:
                    f.write(content)

        print("Project structure successfully created!")
    except Exception as e:
        print("An error occurred while creating the project structure:", e)

# Define the structure of the project.
root_folder = "MyProject/src"
folders = [
    "Components/Component1",
    "Components/Components2",
    "Components/pages/Home",
    "Components/pages/About",
    "public"
    ]
file_contents = {
    "index.tsx": "// file content index.tsx",
    "styles.css":"* { padding:0; margin:0; vertical-align:baseline; list-style:none; border:0}"
}
# Call the function to create the project structure.
create_project_structure(root_folder, folders, file_contents)
