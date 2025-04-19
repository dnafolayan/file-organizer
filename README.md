# File Organizer

## Overview

The **File Organizer** is a Python script designed to help you organize files in a folder based on their extensions. It sorts files into predefined folders such as `TEXT`, `PDF`, `JSON`, or a generic `REMNANT` folder for unsupported file types. This script ensures that your workspace is neat and organized, making it easier to manage and access your files.

## Features

-   Organizes files based on their extensions (e.g., `.txt`, `.pdf`, `.json`).
-   Creates subfolders dynamically in the target directory if they don't already exist.
-   Moves files to their corresponding folders.
-   Handles common errors, such as permission issues or missing files.

## Requirements

-   Python 3.6 or higher
-   No external dependencies are required.

## Setup and Usage

1. **Clone or Download the Repository**:
   Clone the repository:

    ```bash
    git clone https://github.com/dnafolayan/file-organizer.git
    ```

2. **Run the Script**:
   Open a terminal or command prompt and navigate to the project folder.

    Run the Python script:

    ```bash
    python3 file_organizer.py
    ```

    You will be prompted to enter the full path of the folder you want to organize. For example:

    ```
    Please enter the full path to the folder to organize: /path/to/your/folder
    ```

    The script will:

    - Create folders like `TEXT`, `PDF`, `JSON`, and `REMNANT` if they don't already exist.
    - Move the files to the corresponding folders based on their extension.
    - Print messages indicating whether files were successfully moved or excluded.
