# Bulk File Renamer

### Description

A Python script for bulk renaming files and folders. The script supports custom naming formats and recursive renaming in subdirectories. It also includes a specialized function for renaming files downloaded from WhatsApp.

### Features

* Bulk renaming of files in a directory.
* Option to rename files in subdirectories recursively.
* Custom naming formats.
* Specialized function for renaming files downloaded from WhatsApp.

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/bulk-file-renamer.git
```

Navigate into the project directory:

```bash
cd bulk-file-renamer
```

### Usage

Run the script by executing:

```
python bulk_file_renamer.py
```

The script will prompt for the directory path where you wish to perform the renaming operations and whether to include subdirectories.

### Functions

```
_rename_files_downloaded_from_whatsapp
```

Rename files downloaded from WhatsApp that follow the pattern "WhatsApp Image YYYY-MM-DD at HH.MM.SS.jpeg" to "PHOTO-YYYY-MM-DD-HH-MM-SS.jpg".

```
_rename_to_lowercase_and_dashes
```

Renames all files in a directory to lowercase, replaces spaces with dashes, and condenses multiple consecutive dashes into a single dash.

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License

This project is licensed under the MIT License.