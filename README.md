# Montiro - File Integrity Monitoring Tool

Montiro is a simple, command-line tool for monitoring file integrity using SHA-256 hashing. It helps you track changes to files or directories, alerting you when a file has been modified.

## Features
- **File Integrity Monitoring:** Detect changes in files or directories.
- **Recursive Hashing:** Option to check subdirectories.
- **SHA-256 Hashing:** Secure hashing for file verification.
- **Hash History:** Stores and compares file hashes for future integrity checks.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/montiro.git
   cd montiro
   ```
2. Install the package:
   ```bash
   pip install .
   ```

3. Run the program
   ```bash
   montiro --help
   ```

## Usage

### Check for a Single File
```bash
montiro /path/to/your/file.txt
```
### Monitor a directory
Without recursion
```bash
montiro /path/to/your/directory
```

With recursion
```bash
montiro /path/to/your/directory --recursive
```

### Example Output
```bash
montiro /home/user/documents --recursive

File: report.docx, SHA-256: abc123...
2 files found

This is the first check for '/home/user/documents/report.docx'.
Hash recorded: abc123...
```

## LICENSE
Licensed under the MIT License. See LICENSE for details.