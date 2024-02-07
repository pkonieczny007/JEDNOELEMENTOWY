import pandas as pd
import os
import shutil
import glob

# Funkcja do tworzenia folderów, jeśli nie istnieją
def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Wczytaj dane z pliku Excel
excel_file = 'nazwa_pliku.xlsx'
df = pd.read_excel(excel_file)

# Folder bazowy dla obrazów jpg
base_images_folder = os.path.join(os.getcwd(), 'Rysunki_jpg')

# Lista do przechowywania brakujących rysunków
missing_drawings = []

# Przejdź przez każdy wiersz danych Excel
for index, row in df.iterrows():
    rysunek_base = str(row['Rysunek'])
    folder1 = row['FOLDER1']
    folder2 = row['FOLDER2']
    folder3 = row['FOLDER3']

    # Szukaj pasujących plików z uwzględnieniem wszelkich dodatkowych oznaczeń przed "_+opracowanie.jpg"
    pattern = os.path.join(base_images_folder, rysunek_base + '*_+opracowanie.jpg')
    matches = glob.glob(pattern)

    # Sprawdź, czy znaleziono jakiekolwiek dopasowania
    if matches:
        # Jeśli tak, użyj pierwszego znalezionego dopasowania
        file_path = matches[0]
        # Kontynuuj kopiowanie do wskazanych folderów
        for folder in [folder1, folder2, folder3]:
            if pd.notna(folder):
                target_folder_path = os.path.join(base_images_folder, folder)
                create_folder_if_not_exists(target_folder_path)
                shutil.copy(file_path, target_folder_path)
    else:
        # Jeśli nie, dodaj do listy brakujących rysunków
        missing_drawings.append(rysunek_base)

# Zapisz brakujące rysunki do pliku, jeśli takie istnieją
if missing_drawings:
    missing_drawings_file = os.path.join(base_images_folder, 'brak_rysunku_do_pr.txt')
    with open(missing_drawings_file, 'w') as f:
        for drawing in missing_drawings:
            f.write(f"{drawing}\n")
    print(f"Zapisano listę brakujących rysunków do pliku '{missing_drawings_file}'.")

print("Operacja zakończona sukcesem.")
