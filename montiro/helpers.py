import hashlib
import json
from pathlib import Path

# Path to store hashes
HASH_STORE = 'hashes.json'

def compute_hash(path):
    """Helper function to compute the SHA-256 of a file."""
    hash_obj = hashlib.new('sha256')

    # Open file in binary mode and read it in chunks
    with open(path, 'rb') as file:
        while chunks := file.read(8192):
            hash_obj.update(chunks)

    return hash_obj.hexdigest()


def load_hashes():
    """Load the existing hashes from file."""
    if Path.exists(Path(HASH_STORE)):
        with open(HASH_STORE, 'r') as f:
            return json.load(f)
    return {}


def save_hashes(hashes):
    """Saves the hashes to the file."""
    with open(HASH_STORE, 'w') as f:
        json.dump(hashes, f, indent=4)
