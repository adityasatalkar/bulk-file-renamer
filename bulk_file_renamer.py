import os
import re


class FileRenamer:
    def __init__(self, directory_path, include_subfolders=False):
        self.directory_path = directory_path
        self.include_subfolders = include_subfolders

    def _rename_files_in_directory(self, directory, renaming_function):
        for filename in os.listdir(directory):
            renaming_function(directory, filename)

    def start(self):
        self._rename_files_in_directory(self.directory_path, self._rename_files_downloaded_from_whatsapp)
        self._rename_files_in_directory(self.directory_path, self._rename_to_lowercase_and_dashes)

        if self.include_subfolders:
            for root, dirs, files in os.walk(self.directory_path):
                for dir in dirs:
                    directory = os.path.join(root, dir)
                    self._rename_files_in_directory(directory, self._rename_files_downloaded_from_whatsapp)
                    self._rename_files_in_directory(directory, self._rename_to_lowercase_and_dashes)

    def _rename_files_downloaded_from_whatsapp(self, directory, filename):
        pattern = r"WhatsApp Image (\d{4}-\d{2}-\d{2}) at (\d{2}\.\d{2}\.\d{2})\.jpeg"
        regex = re.compile(pattern)
        match = regex.match(filename)
        if match:
            date_str = match.group(1)
            time_str = match.group(2)
            time_str = time_str.replace('.', '-')
            new_filename = f"PHOTO-{date_str}-{time_str}.jpg"
            self._rename_file(directory, filename, new_filename)

    def _rename_to_lowercase_and_dashes(self, directory, filename):
        name, ext = os.path.splitext(filename)
        new_name = name.lower().replace(" ", "-")
        new_name = re.sub('-+', '-', new_name)
        new_name = new_name.strip('-')
        new_filename = f"{new_name}{ext}"
        self._rename_file(directory, filename, new_filename)

    def _rename_file(self, directory, old_filename, new_filename):
        old_filepath = os.path.join(directory, old_filename)
        new_filepath = os.path.join(directory, new_filename)
        os.rename(old_filepath, new_filepath)
        print(f"Renamed {old_filename} to {new_filename}")


if __name__ == "__main__":
    folder_path = input("Enter the directory path: ")
    include_subfolders = input("Include subfolders? (y/n): ").lower() == 'y'
    renamer = FileRenamer(folder_path, include_subfolders)

    renamer.start()
