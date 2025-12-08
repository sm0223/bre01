import dill
from pathlib import Path

import pyDMNrules


def get_all_files(folder_path):
    """Finds all .xlsx files in a given directory."""
    print(f"Searching for .xlsx files in: {folder_path}")
    files = list(folder_path.rglob('*.xlsx'))
    print(f"Found {len(files)} files.")
    return files


def get_output_file_path(input_path, cache_dir):
    """Constructs the output path for the pickle file in the cache directory."""
    # Ensure the cache directory exists
    cache_dir.mkdir(parents=True, exist_ok=True)
    # Create the output filename by changing the extension to .pkl
    return cache_dir / input_path.with_suffix('.pkl').name


def add_to_pkl(file_path, dmn_object, cache_dir):
    """Saves the DMN object to a pickle file."""
    output_filepath = get_output_file_path(file_path, cache_dir)
    try:
        with open(output_filepath, 'wb') as f:
            dill.dump(dmn_object, f)
        print(f"Successfully created pickle file: {output_filepath}")
    except Exception as ex:
        print(f"Error saving pickle file for {file_path}: {ex}")
        raise


def get_dmn_from_pkl(file_path):
    """Loads a pyDMNrules.DMN object from a pickle file."""
    try:
        with open(file_path, 'rb') as f:
            dmn_object = dill.load(f)
        print(f"Successfully loaded DMN object from: {file_path}")
        return dmn_object
    except Exception as ex:
        print(f"Error loading pickle file {file_path}: {ex}")
        raise


def main():
    """
    Main function to load all DMN tables from Excel files and save them as pickles.
    """
    print("Starting DMN table processing...")
    base_path = Path('/rules/bre01/policy_rules/decision_tables/')
    raw_folder_path = base_path / 'raw'
    cache_folder_path = base_path / 'cache'

    file_paths = get_all_files(raw_folder_path)

    if not file_paths:
        print("No Excel files found to process.")
        return

    try:
        for file_path in file_paths:
            print(f"Processing: {file_path.name}")
            # Create a new DMN object for each file to prevent recursion errors
            dmn = pyDMNrules.DMN()
            status = dmn.load(file_path)

            if 'error' in status:
                print(f"ERROR loading {file_path.name}: {status['error']}")
                print("Stopping process due to error.")
                break
            else:
                add_to_pkl(file_path, dmn, cache_folder_path)
        
        print("All files processed successfully.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Process ended with an exception.")

if __name__ == '__main__':
    main()
