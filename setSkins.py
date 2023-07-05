from config import skin_id, mmc, cape_id
import psutil
import os
import shutil
from ahk import AHK
ahk = AHK()

path = os.path.dirname(os.path.realpath(__file__))
reset_file = os.path.abspath(os.path.realpath(os.path.join(path, 'reset.ahk')))
hold_file = os.path.abspath(os.path.realpath(os.path.join(path, 'hold.tmp')))
pids_file = os.path.abspath(os.path.realpath(os.path.join(path, 'PIDs.txt')))

PIDs = []
for proc in psutil.process_iter():
    if "javaw" in proc.name():
        PIDs.append(proc.pid)

for i in range(len(PIDs)):
    if len(skin_id) > 0:
        skin_folder = f"{mmc}\\assets\skins\{skin_id[:2]}"
        # Remove file
        if os.path.exists(skin_folder + f"\{skin_id}"):
            os.remove(skin_folder + f"\{skin_id}")
        # Copy over skin
        skin_path = os.path.abspath(os.path.realpath(os.path.join(path, "skins", f"{i+1}.png")))
        shutil.copyfile(skin_path, skin_folder + f"\\{skin_id}")
    if len(cape_id) > 0:
        cape_folder = f"{mmc}\\assets\skins\{cape_id[:2]}"
        # Remove file
        if os.path.exists(cape_folder + f"\{cape_id}"):
            os.remove(cape_folder + f"\{cape_id}")
        # Copy over skin
        cape_path = os.path.abspath(os.path.realpath(os.path.join(path, "capes", f"{i+1}.png")))
        shutil.copyfile(cape_path, cape_folder + f"\\{cape_id}")
    # Run reset.ahk
    open(hold_file, 'a').close()
    script_str = f'pid := {PIDs[i]}\n'
    with open(reset_file, "r") as ahk_script:
        script_str += ahk_script.read()
    ahk.run_script(script_str)
    # Wait for file to exist
    while os.path.exists(hold_file):
        print("resetting")

if os.path.exists(pids_file):
    os.remove(pids_file)

# Reset defaults

default_skin_file = os.path.abspath(os.path.realpath(os.path.join(path, 'skins', 'main.png')))
default_cape_file = os.path.abspath(os.path.realpath(os.path.join(path, 'capes', 'main.png')))

if len(skin_id) > 0 and os.path.exists(default_skin_file):
    shutil.copyfile(default_skin_file, skin_folder + f"\\{skin_id}")
if len(cape_id) > 0 and os.path.exists(default_cape_file):
    shutil.copyfile(default_cape_file, cape_folder + f"\\{cape_id}")
