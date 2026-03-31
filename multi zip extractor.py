# ==================================================
# MULTI ZIP FILE EXTRACTOR
# User can select ANY number of ZIP files
# Each ZIP extracts into its own folder
# Press ENTER to exit
# ==================================================

import zipfile
import os
from tkinter import Tk, filedialog

print("\n======================================")
print(" MULTI ZIP FILE EXTRACTOR")
print("======================================\n")

# ---------------- TKINTER SETUP ----------------
root = Tk()
root.withdraw()            # Hide main window
root.attributes('-topmost', True)

# ---------------- SELECT ZIP FILES ----------------
zip_files = filedialog.askopenfilenames(
    title="Select ZIP files (CTRL or SHIFT for multiple)",
    filetypes=[("ZIP files", "*.zip")]
)

if not zip_files:
    print("❌ No ZIP files selected.")
    input("\nPress Enter to exit...")
    exit()

print(f"✅ {len(zip_files)} ZIP file(s) selected\n")

# ---------------- EXTRACT ZIP FILES ----------------
for zip_path in zip_files:
    try:
        zip_name = os.path.basename(zip_path)
        extract_folder = os.path.splitext(zip_path)[0]

        print(f"📦 Extracting: {zip_name}")

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)

        print(f"   ✔ Extracted to: {extract_folder}\n")

    except zipfile.BadZipFile:
        print(f"❌ Corrupted ZIP file: {zip_path}\n")

    except Exception as e:
        print(f"❌ Error extracting: {zip_path}")
        print(e, "\n")

print("======================================")
print(" 🎉 ALL ZIP FILES EXTRACTED SUCCESSFULLY")
print("======================================")

input("\nPress Enter to exit...")
