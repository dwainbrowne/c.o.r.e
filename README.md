
# C.O.R.E Folder Structure Generation Script

### Description
This Python script automates the creation of a complex, cross-platform compatible folder structure designed for organizing company and personal resources. The structure is based on the C.O.R.E. system, categorizing various aspects of companies, personal obligations, resources, and records into a hierarchical folder format. The script also includes a section where you can specify company names, which will be automatically sanitized and converted to lowercase to ensure compatibility across different operating systems.

### Features
- **Cross-Platform Compatibility**: The script sanitizes folder names to ensure they are compatible with various operating systems (Windows, macOS, Linux).
- **Customizable Company List**: Easily add your own company names to generate specific folders for each one.
- **Hierarchical Structure**: Creates a deep folder hierarchy for organized storage of various documents and resources.
- **Configurable Root Path**: Specify the root directory where the entire folder structure should be created.

### Folder Structure Overview

The generated structure includes:

- **C.O.R.E.**
  - **Companies**
    - Company-specific folders (e.g., "snapsuite", "PhD solutions")
      - **Planning**
      - **Sales**
      - **Marketing**
      - **Operations**
      - **Human Resources**
      - **Finance**
      - **Legal**
      - **IT Infrastructure**
  - **Obligations**
    - **Personal**
      - **Health**
      - **Finance**
      - **Identity**
      - **Family**
      - **Legal**
      - **Employment**
      - **Planning**
      - **Travel**
      - **Photos Videos**
      - **Miscellaneous**
    - **People**
      - **Friends**
      - **Colleagues**
      - **Acquaintances**
  - **Resources**
    - **Audio Notes**
    - **Brainstorming**
    - **Bookmarks**
    - **Books**
    - **Design Notes**
    - **Miscellaneous Ideas**
  - **Records**
    - **Family**
    - **Business**
    - **Old Records**

### Usage Instructions

#### Prerequisites
- Python 3.x installed on your system.

#### How to Run the Script
1. **Download/Clone the Script**: Ensure the script file is available on your system.
2. **Modify the Script (Optional)**: If you wish to add more companies, edit the `companies` list in the script.
3. **Set the Root Path**: Modify the `root_path` variable in the script to specify where the "C.O.R.E." folder should be created.
4. **Run the Script**:
   ```bash
   python folder_structure_generator.py
   ```
   The script will create the entire folder structure at the specified location.

### Customization

- **Adding Companies**: You can add more company names to the `companies` list in the script. Ensure that the names are in quotes, separated by commas.
- **Changing the Root Path**: Update the `root_path` variable in the script to set a different location for the "C.O.R.E." folder.

### License

This script is open-source and available for personal or commercial use. Feel free to modify and distribute it as needed.

---

### Short Description

This Python script automates the creation of a hierarchical, cross-platform compatible folder structure for organizing company and personal resources. It allows you to specify company names, which are sanitized and converted to lowercase, and to choose the root directory for generating the folder structure. Ideal for maintaining a structured organization system using the C.O.R.E. framework.
