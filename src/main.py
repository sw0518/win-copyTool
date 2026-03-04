import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import logging
from copier import copy_files

class FileCopierApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Copier")
        self.geometry("800x600")

        # --- UI Components ---
        # Frame for inputs
        input_frame = tk.Frame(self, padx=10, pady=10)
        input_frame.pack(fill="x")

        # Source Directory
        tk.Label(input_frame, text="Source Directory:").grid(row=0, column=0, sticky="w", pady=2)
        self.source_dir_entry = tk.Entry(input_frame, width=80)
        self.source_dir_entry.grid(row=0, column=1, sticky="ew")
        tk.Button(input_frame, text="Browse...", command=self.browse_source).grid(row=0, column=2, padx=5)

        # Destination Directory
        tk.Label(input_frame, text="Destination Directory:").grid(row=1, column=0, sticky="w", pady=2)
        self.dest_dir_entry = tk.Entry(input_frame, width=80)
        self.dest_dir_entry.grid(row=1, column=1, sticky="ew")
        tk.Button(input_frame, text="Browse...", command=self.browse_dest).grid(row=1, column=2, padx=5)

        # Excluded Directories
        tk.Label(input_frame, text="Excluded Dirs (comma-separated):").grid(row=2, column=0, sticky="w", pady=2)
        self.excluded_dirs_entry = tk.Entry(input_frame, width=80)
        self.excluded_dirs_entry.insert(0, ".git, __pycache__, node_modules, venv")
        self.excluded_dirs_entry.grid(row=2, column=1, sticky="ew")

        # Excluded Extensions
        tk.Label(input_frame, text="Excluded Exts (comma-separated):").grid(row=3, column=0, sticky="w", pady=2)
        self.excluded_exts_entry = tk.Entry(input_frame, width=80)
        self.excluded_exts_entry.insert(0, ".log, .tmp, .bak")
        self.excluded_exts_entry.grid(row=3, column=1, sticky="ew")

        input_frame.columnconfigure(1, weight=1)

        # --- Action Button ---
        tk.Button(self, text="Start Copy", command=self.start_copy_thread, font=("Helvetica", 12, "bold"), bg="lightblue").pack(pady=10)

        # --- Log Viewer ---
        log_frame = tk.Frame(self, padx=10, pady=10)
        log_frame.pack(fill="both", expand=True)
        self.log_text = tk.Text(log_frame, state='disabled', wrap='word', height=20)
        scrollbar = tk.Scrollbar(log_frame, command=self.log_text.yview)
        self.log_text.config(yscrollcommand=scrollbar.set)
        self.log_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Configure logging to redirect to the GUI
        self.log_handler = GuiLogger(self.log_text)
        logging.getLogger().setLevel(logging.INFO)
        logging.getLogger().addHandler(self.log_handler)

    def browse_source(self):
        directory = filedialog.askdirectory()
        if directory:
            self.source_dir_entry.delete(0, tk.END)
            self.source_dir_entry.insert(0, directory)

    def browse_dest(self):
        directory = filedialog.askdirectory()
        if directory:
            self.dest_dir_entry.delete(0, tk.END)
            self.dest_dir_entry.insert(0, directory)

    def start_copy_thread(self):
        source_dir = self.source_dir_entry.get()
        dest_dir = self.dest_dir_entry.get()
        
        if not source_dir or not dest_dir:
            messagebox.showerror("Error", "Source and Destination directories must be specified.")
            return

        excluded_dirs = [d.strip() for d in self.excluded_dirs_entry.get().split(',') if d.strip()]
        excluded_exts = [e.strip() for e in self.excluded_exts_entry.get().split(',') if e.strip()]

        # Run the copy operation in a separate thread to keep the GUI responsive
        thread = threading.Thread(target=self.run_copy, args=(source_dir, dest_dir, excluded_dirs, excluded_exts))
        thread.daemon = True
        thread.start()

    def run_copy(self, source_dir, dest_dir, excluded_dirs, excluded_exts):
        try:
            logging.info("File copy process started...")
            copy_files(source_dir, dest_dir, excluded_dirs, excluded_exts)
            logging.info("File copy process completed successfully.")
            messagebox.showinfo("Success", "Files copied successfully!")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            messagebox.showerror("Error", f"An error occurred during the copy process:\n{e}")

class GuiLogger(logging.Handler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text_widget.config(state='normal')
            self.text_widget.insert(tk.END, msg + '\n')
            self.text_widget.config(state='disabled')
            self.text_widget.see(tk.END)
        self.text_widget.after(0, append)

if __name__ == "__main__":
    app = FileCopierApp()
    app.mainloop()
