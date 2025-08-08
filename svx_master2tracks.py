#python 3.4
import time
import zipfile
import os
import subprocess
import pathlib
#from pathlib import Path

def get_script_dir():
    # script_dir = Path(__file__).parent
    script_dir = pathlib.Path(__file__).parent
    print("Script Directory:", script_dir)
    return script_dir

def master_svx_file_list(directory):
    file_list = [f for f in pathlib.Path(directory).glob('**/*-master.svx') if f.is_file()]
    return file_list

def mask_file_list(directory, file_mask):
    file_list = [f for f in pathlib.Path(directory).glob(file_mask) if f.is_file()]
    return file_list

def zipuj_pliki(sciezka_do_zip, pliki_gpx_do_spakowania, nazwa_archiwum):
    """
    Pakuje podane pliki i foldery do archiwum zip.

    Args:
        sciezka_do_zip (str): Ścieżka do folderu, w którym ma zostać utworzone archiwum.
        pliki_gpx_do_spakowania (list): Lista ścieżek do plików i folderów do spakowania.
        nazwa_archiwum (str): Nazwa archiwum zip (bez rozszerzenia .zip).
    """
    try:
        with zipfile.ZipFile(os.path.join(sciezka_do_zip, nazwa_archiwum + ".zip"), "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zip_plik:
            for element in pliki_gpx_do_spakowania:
                if os.path.isfile(element):
                    zip_plik.write(element, os.path.basename(element))
                elif os.path.isdir(element):
                    for folder_element, _, pliki in os.walk(element):
                        for plik in pliki:
                            sciezka_do_pliku = os.path.join(folder_element, plik)
                            relatywna_sciezka = os.path.relpath(sciezka_do_pliku, element)
                            zip_plik.write(sciezka_do_pliku, os.path.join(os.path.basename(element), relatywna_sciezka))
    except Exception as e:
        print(f"Wystąpił błąd podczas tworzenia archiwum zip: {e}")

def usun_pliki_pathlib(lista_plikow):
    for sciezka_pliku in lista_plikow:
        plik = pathlib.Path(sciezka_pliku)
        try:
            if plik.exists():
                plik.unlink()
                print(f"Plik {sciezka_pliku} został usunięty.")
            else:
                print(f"Plik {sciezka_pliku} nie istnieje.")
        except OSError as e:
             print(f"Błąd podczas usuwania pliku {sciezka_pliku}: {e}")

def main():
    nazwa_archiwum_gpx = "cave-tracks-gpx"
    nazwa_archiwum_kml = "cave-tracks-kml"

    script_dir = get_script_dir()
    print(script_dir)

    # usuń pliki zip zawierające ciągi pomiarowe jaskiń w formatach gpx i kml
    path_archiwum_gpx = str(script_dir) + '\\' + nazwa_archiwum_gpx + '.zip'
    path_archiwum_kml = str(script_dir) + '\\' + nazwa_archiwum_kml + '.zip'
    lista_plikow_do_usuniecia = [path_archiwum_gpx, path_archiwum_kml]
    print("lista_plikow_do_usuniecia: ", lista_plikow_do_usuniecia)
    usun_pliki_pathlib(lista_plikow_do_usuniecia)
    
    try:
        # file_list = master_svx_file_list(script_dir)
        file_list = mask_file_list(script_dir, '**/*-master.svx')
        # print("file_list: ", file_list)
    except (IndexError) as e:
        print("Index Error: {e}")
    except (NameError) as e:
        print("Name Error: {e}")
    except (TypeError) as e:
        print("Type Error: {e}")
    except (Exception) as e:
        print("An error occurred: {e}")
        
    try:
        file_list[0]
        print('quantity of  *-master.svx files =', len(file_list))
    except (IndexError):
        print('Not found *-master.svx files in current directory and subdirectories')
        quit()
    
    print('run cavern.exe to generate *-master.3d files')
    for file_path in file_list:
        print(file_path)
        current_cave_dir = file_path.parent
        # print('current_cave_dir: ', current_cave_dir)
        os.chdir(current_cave_dir)
        # print(os.getcwd())
        # print(pathlib.Path.cwd())

        subprocess.run(['cavern', '--log', file_path])
        
        file_3d = file_path.stem + '.3d'
        # print('file_3d', file_3d)
        subprocess.run(["c:\\Program Files (x86)\\Survex\\survexport.exe", '--plan', '--legs', '--gpx', file_3d])
        subprocess.run(["c:\\Program Files (x86)\\Survex\\survexport.exe", '--plan', '--legs', '--kml', file_3d])

    print('Sleep for 1 second')
    time.sleep(1)  # Wstrzymuje program na kilka sekund, aby wszystkie pliki *.gpx o *.kml zostały utworzone i zwolnione

    # pliki_gpx_do_spakowania = [f for f in pathlib.Path(script_dir).glob('**/*-master.gpx') if f.is_file()]
    pliki_gpx_do_spakowania = file_list = mask_file_list(script_dir, '**/*-master.gpx')
    # pliki_kml_do_spakowania = [f for f in pathlib.Path(script_dir).glob('**/*-master.kml') if f.is_file()]
    pliki_kml_do_spakowania = file_list = mask_file_list(script_dir, '**/*-master.kml')

    zipuj_pliki(script_dir, pliki_gpx_do_spakowania, nazwa_archiwum_gpx)
    print(f"Archiwum zip '{nazwa_archiwum_gpx}.zip' zostało utworzone w '{script_dir}'")
    zipuj_pliki(script_dir, pliki_kml_do_spakowania, nazwa_archiwum_kml)
    print(f"Archiwum zip '{nazwa_archiwum_kml}.zip' zostało utworzone w '{script_dir}'")

    print('Sleep for 2 seconds')
    time.sleep(2)  # Wstrzymuje program na kilka sekund, aby wszystkie pliki *.gpx o *.kml zostały spakowane i zwolnione

    # usuń pliki gpx i kml z folderów poszczególnych jaskiń
    lista_plikow_do_usuniecia = pliki_gpx_do_spakowania + pliki_kml_do_spakowania
    # print("lista_plikow_do_usuniecia: ", lista_plikow_do_usuniecia)
    usun_pliki_pathlib(lista_plikow_do_usuniecia)

if __name__ == "__main__":
    main()