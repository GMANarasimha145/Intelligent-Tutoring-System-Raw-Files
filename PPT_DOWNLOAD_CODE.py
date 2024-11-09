import os
import tkinter as tk
from tkinter import filedialog
from shutil import copyfile

def download_ppt():
    # Path to the existing PowerPoint presentation
    source_path = r"C:\Practical Freaks\content_chunks.pptx"

    # Choose the destination directory for saving the downloaded ppt
    destination_dir = filedialog.askdirectory()

    if destination_dir:
        # Destination path for the downloaded PowerPoint presentation
        destination_path = os.path.join(destination_dir, "downloaded_presentation.pptx")

        # Copy the PowerPoint presentation to the destination directory
        copyfile(source_path, destination_path)

        # Show a message box indicating successful download
        tk.messagebox.showinfo("Download Complete", "The PowerPoint presentation has been downloaded successfully.")

# Create a Tkinter window
root = tk.Tk()
root.title("PPT Downloader")

# Create a button to download the PowerPoint presentation
download_button = tk.Button(root, text="Download Content PPT", command=download_ppt)
download_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()