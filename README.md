# File Copier

This is a user-friendly Windows application for copying files from a source directory to a destination directory while maintaining the original folder structure. It provides a graphical user interface (GUI) to easily configure and run the copy process.

## Features

*   **Graphical User Interface**: An intuitive interface for easy operation.
*   **Directory Selection**: "Browse" buttons to easily select source and destination folders.
*   **Flexible Exclusions**: Specify lists of directories and file extensions to exclude from the copy.
*   **Real-Time Logging**: A log viewer within the application shows the status of the copy process in real-time.
*   **Standalone Executable**: Runs as a single `.exe` file on Windows with no installation or dependencies required.

## How to Use

1.  **Run the Application**:
    *   Navigate to the `dist` folder.
    *   Double-click `FileCopier.exe` to launch the application.

2.  **Configure the Copy**:
    *   **Source Directory**: Use the "Browse..." button to select the folder you want to copy files from.
    *   **Destination Directory**: Use the "Browse..." button to select the folder where you want to copy files to.
    *   **Excluded Dirs**: Enter a comma-separated list of folder names to exclude (e.g., `.git, node_modules`).
    *   **Excluded Exts**: Enter a comma-separated list of file extensions to exclude (e.g., `.log, .tmp`).

3.  **Start the Process**:
    *   Click the "Start Copy" button.

4.  **Monitor Progress**:
    *   Watch the log area at the bottom of the window to see which files are being copied and which are being skipped.
    *   A message box will appear to confirm when the process is complete.

## Project Structure

```
file_copier/
├── src/
│   ├── copier.py       # Core file copying logic
│   └── main.py         # GUI application code
├── dist/
│   └── FileCopier.exe  # The standalone executable
└── README.md           # This documentation
```
