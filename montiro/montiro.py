import argparse
from pathlib import Path
from .helpers import compute_hash, load_hashes, save_hashes


def check_file_integrity(file_path, recursive=False):
    """Compute the SHA-256 hash(es) of the file(s) and check integrity."""
    path = Path(file_path)

    # Load stored hashes
    hashes = load_hashes()

    # Compute hash for a single file
    if path.is_file():
        current_hash = compute_hash(path)
        check_file_in_hashes(path, current_hash, hashes)
    
    # Compute hash for files in a directory recursively
    elif path.is_dir() and recursive:
        count = 0
        for entry in path.rglob('*'):  # Recursive search
            if entry.is_file():
                count += 1
                current_hash = compute_hash(entry)
                check_file_in_hashes(entry, current_hash, hashes)
        print(f"\n{count} files found")
    
    # Compute hash for files skipping subdirectories
    elif path.is_dir():
        count = 0
        for entry in path.iterdir():
            if entry.is_file():
                count += 1
                current_hash = compute_hash(entry)
                check_file_in_hashes(entry, current_hash, hashes)
            else:
                print(f"Skipping subdirectory: {entry.name}")
        print(f"\n{count} files found")

    else:
        print(f"{file_path}: No such file or directory.")
        return


def check_file_in_hashes(path, current_hash, hashes):
    """Helper function to check and update file integrity in hashes."""
    abs_path = str(path.resolve())  # Use absolute paths for uniqueness
    if abs_path in hashes:
        stored_hash = hashes[abs_path]
        if stored_hash == current_hash:
            print(f"The file '{path}' has not been modified.")
        else:
            print(f"Warning: The file '{path}' has been modified!")
    else:
        print(f"This is the first check for '{path}'.")
        hashes[abs_path] = current_hash
        save_hashes(hashes)
        print(f"Hash recorded: {current_hash}")


def main():
    parser = argparse.ArgumentParser(description='Montiro - File Integrity Monitoring Tool')
    parser.add_argument("path", help="Path to file or directory")
    parser.add_argument("--recursive", "-r", action="store_true", help="Recursively generate hash for files in subdirectories")

    args = parser.parse_args()

    # Pass the recursive argument directly to the function
    check_file_integrity(args.path, recursive=args.recursive)


if __name__ == '__main__':
    main()
