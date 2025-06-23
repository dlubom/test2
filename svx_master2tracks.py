#python 3.4
import os, subprocess
from pathlib import Path

def get_script_dir():
    script_dir = Path(__file__).parent
    print("Script Directory:", script_dir)
    return script_dir

def master_svx_file_list(directory):
    file_list = [f for f in Path(directory).glob('**/*-master.svx') if f.is_file()]
    return file_list

def main():
    script_dir = get_script_dir()
    print(script_dir)
    
    try:
        file_list = master_svx_file_list(script_dir)
    except (IndexError):
        print("Index Error")
    except (NameError):
        print("Name Error")
    except (TypeError):
        print("Type Error")
    except:
        print("Other error")
        
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
        print('current_cave_dir: ', current_cave_dir)
        os.chdir(current_cave_dir)
        # print(os.getcwd())
        print(Path. cwd())

        subprocess.run(['cavern', '-qq', file_path])
        
        file_3d = file_path.stem + '.3d'
        print('file_3d', file_3d)
        subprocess.run(["c:\Program Files (x86)\Survex\survexport.exe", '--plan', '--legs', '--gpx', file_3d])
        subprocess.run(["c:\Program Files (x86)\Survex\survexport.exe", '--plan', '--legs', '--kml', file_3d])

if __name__ == "__main__":
    main()