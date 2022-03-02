from config import *
import os
import shutil
from ahk import AHK
ahk = AHK()

if os.path.exists("PIDs.txt"):
    os.remove("PIDs.txt")
if os.path.exists("hold.tmp"):
    os.remove("hold.tmp")

# Run ahk to get PIDs.txt
with open("getPIDs.ahk", "r") as ahk_script:
    script_str = ahk_script.read()
ahk.run_script(script_str)

while not os.path.exists("PIDs.txt"):
    print("getting PIDs")

with open("PIDs.txt", "r") as fp:
    PIDs = fp.read().strip()[:-1].split(",")

for i in range(len(PIDs)):
    if len(skin_id) > 0:
        skin_folder = f"{mmc}\\assets\skins\{skin_id[:2]}"
        # Remove file
        if os.path.exists(skin_folder + f"\{skin_id}"):
            os.remove(skin_folder + f"\{skin_id}")
        # Copy over skin
        shutil.copyfile(f"skins\{i+1}.png", skin_folder + f"\\{skin_id}")
    if len(cape_id) > 0:
        cape_folder = f"{mmc}\\assets\skins\{cape_id[:2]}"
        # Remove file
        if os.path.exists(cape_folder + f"\{cape_id}"):
            os.remove(cape_folder + f"\{cape_id}")
        # Copy over skin
        shutil.copyfile(f"capes\{i+1}.png", cape_folder + f"\\{cape_id}")
    # Run reset.ahk
    open("hold.tmp", 'a').close()
    script_str = f"pid := {PIDs[i]}\n"
    with open("reset.ahk", "r") as ahk_script:
        script_str += ahk_script.read()
    ahk.run_script(script_str)
    # Wait for file to exist
    while os.path.exists("hold.tmp"):
        print("resetting")
