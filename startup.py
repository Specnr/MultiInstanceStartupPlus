from config import *
import os

for i in range(1, instance_count+1):
    print(f"Starting instance {instance_format}{i}")
    os.system(f"{mmc}\MultiMC.exe -l {instance_format}{i}")
