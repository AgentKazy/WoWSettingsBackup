import os
import pathlib
from pathlib import Path
import configparser
import tkinter as tk
from tkinter import filedialog
import subprocess
import time
from datetime import datetime

cls = lambda: os.system('cls')
cls()
# --------------------------------------------------------------------------- #
#                  WoW Addon Settings Backup by /u/AgentKazy                  #
# --------------------------------------------------------------------------- #
# > CONFIGURATION FILE
config_folder = pathlib.Path.home() / 'KazyWoWBackup' # Path to configuration file.
if not config_folder.is_dir(): # If folder doesn't exist:
    try:
        config_folder.mkdir(parents=True, exist_ok=True) # Create folder.
    except IOError:
        print('Unable to create folder. Check your permissions.')
        time.sleep(5)
        quit()

config_file = pathlib.Path(config_folder) / 'AddonSettingsBackup.ini' # Path to configuration file.
Config = configparser.ConfigParser() # Determine parser.

if not config_file.is_file(): # If configuration file doesn't exist:
    try:
        open(config_file, 'x', encoding='utf-8') # Create file, UTF-8 encoding.
        cfg_settings = open(config_file,'r+', encoding='utf-8') # Open file in 'read+' mode, UTF-8 encoding.
        Config.add_section('Folders') # Create section 'Folders'.
        Config.set('Folders','settings_flag','False') # Create sub-section and value.
        Config.set('Folders','settings_path','') # Create sub-section and value.
        Config.set('Folders','destination_flag','False') # Create sub-section and value.
        Config.set('Folders','destination_path','') # Create sub-section and value.
        Config.set('Folders','exe7z_flag','False') # Create sub-section and value.
        Config.set('Folders','exe7z_path','') # Create sub-section and value.
        Config.write(cfg_settings) # Write settings to 'config_file'.
        cfg_settings.close() # Close file.
        #print('Configuration file created.') # Print file successfuly created.
    except IOError:
        print('Unable to create file. Check your permissions.')
        time.sleep(5)
        quit()

# > CHOOSE FOLDERS

root = tk.Tk()
root.withdraw()
new_settings = open(config_file,'r+', encoding='utf-8') # Open file in 'write' mode, UTF-8 encoding.
Config.read(config_file) # Read file settings.
addon_flag = Config.get('Folders', 'settings_flag') # Get settings flag.
backup_flag = Config.get('Folders', 'destination_flag') # Get destination flag.
exe_flag = Config.get('Folders', 'exe7z_flag') # Get exe flag.

if addon_flag == 'False': # If flag is 'False':
    settings_folder_path = filedialog.askdirectory(title='Choose settings folder') # Prompt directory.
    if settings_folder_path == '': # If no folder is selected.
        pass
    else:
        Config.set('Folders','settings_flag','True') # Set flag to 'True'.
        Config.set('Folders','settings_path',str('"' + settings_folder_path + '"')) # Set settings path.
else:
    pass

if backup_flag == 'False': # If flag is 'False':
    destination_folder_path = filedialog.askdirectory(title='Choose destination folder') # Prompt directory.
    if destination_folder_path == '': # If no folder is selected.
        pass
    else:
        Config.set('Folders','destination_flag','True') # Set flag to 'True'.
        Config.set('Folders','destination_path',str('"' + destination_folder_path + '"')) # Set destination path.
else:
    pass

if exe_flag == 'False': # If flag is 'False':
    exe7z_folder_path = filedialog.askopenfilename(title='Open 7za.exe file') # Prompt directory.
    if exe7z_folder_path == '': # If no folder is selected.
        pass
    else:
        Config.set('Folders','exe7z_flag','True') # Set flag to 'True'.
        Config.set('Folders','exe7z_path',str('"' + exe7z_folder_path + '"')) # Set destination path.
else:
    pass

try:
    Config.write(new_settings) # Write new settings to file.
    new_settings.close() # Close file.
except IOError:
    print('Unable to write to file. Check your permissions.')
    time.sleep(5)
    quit()

# > MAIN FUNCTION

current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S") # Current time in specific format.

Config.read(config_file) # Read settings file.

source_path = Config.get('Folders', 'settings_path') # Get path from settings file.
backup_folder_path = Config.get('Folders', 'destination_path') # Get path from settings file.

file_name = str('"Settings Backup ' + current_time + '.7z"') # Create file name using current time.
backup_path = pathlib.Path(backup_folder_path) / file_name # Build target file path.

exe_path = Config.get('Folders', 'exe7z_path') # Get path from settings file.

cmd7zip = exe_path + ' a -t7z ' + str(backup_path) + ' ' + source_path + ' -mx=7' # Command line code. (Using compression level 7)
if (source_path != '') and (backup_path != '') and (exe_path != ''):
    try:
        subprocess.call(cmd7zip) # Backup process.
        quit()
    except IOError:
        print('Unable to backup folder. Check your permissions.')
        time.sleep(5)
        quit()

config_file = pathlib.Path(config_folder) / 'AddonSettingsBackup.ini' # Path to configuration file.
Config = configparser.ConfigParser() # Determine parser.

if not config_file.is_file(): # If configuration file doesn't exist:
    try:
        open(config_file, 'x', encoding='utf-8') # Create file, UTF-8 encoding.
        cfg_settings = open(config_file,'r+', encoding='utf-8') # Open file in 'read+' mode, UTF-8 encoding.
        Config.add_section('Folders') # Create section 'Folders'.
        Config.set('Folders','settings_flag','False') # Create sub-section and value.
        Config.set('Folders','settings_path','') # Create sub-section and value.
        Config.set('Folders','destination_flag','False') # Create sub-section and value.
        Config.set('Folders','destination_path','') # Create sub-section and value.
        Config.set('Folders','exe7z_flag','False') # Create sub-section and value.
        Config.set('Folders','exe7z_path','') # Create sub-section and value.
        Config.write(cfg_settings) # Write settings to 'config_file'.
        cfg_settings.close() # Close file.
        #print('Configuration file created.') # Print file successfuly created.
    except IOError:
        print('Unable to create file. Check your permissions.')
        time.sleep(5)
        quit()

# > CHOOSE FOLDERS

root = tk.Tk()
root.withdraw()
new_settings = open(config_file,'r+', encoding='utf-8') # Open file in 'write' mode, UTF-8 encoding.
Config.read(config_file) # Read file settings.
addon_flag = Config.get('Folders', 'settings_flag') # Get settings flag.
backup_flag = Config.get('Folders', 'destination_flag') # Get destination flag.
exe_flag = Config.get('Folders', 'exe7z_flag') # Get exe flag.

if addon_flag == 'False': # If flag is 'False':
    settings_folder_path = filedialog.askdirectory(title='Choose settings folder') # Prompt directory.
    if settings_folder_path == '': # If no folder is selected.
        pass
    else:
        Config.set('Folders','settings_flag','True') # Set flag to 'True'.
        Config.set('Folders','settings_path',str('"' + settings_folder_path + '"')) # Set settings path.
else:
    pass

if backup_flag == 'False': # If flag is 'False':
    destination_folder_path = filedialog.askdirectory(title='Choose destination folder') # Prompt directory.
    if destination_folder_path == '': # If no folder is selected.
        pass
    else:
        Config.set('Folders','destination_flag','True') # Set flag to 'True'.
        Config.set('Folders','destination_path',str('"' + destination_folder_path + '"')) # Set destination path.
else:
    pass

if exe_flag == 'False': # If flag is 'False':
    exe7z_folder_path = filedialog.askopenfilename(title='Open 7za.exe file') # Prompt directory.
    if exe7z_folder_path == '': # If no folder is selected.
        pass
    else:
        Config.set('Folders','exe7z_flag','True') # Set flag to 'True'.
        Config.set('Folders','exe7z_path',str('"' + exe7z_folder_path + '"')) # Set destination path.
else:
    pass

try:
    Config.write(new_settings) # Write new settings to file.
    new_settings.close() # Close file.
except IOError:
    print('Unable to write to file. Check your permissions.')
    time.sleep(5)
    quit()

# > MAIN FUNCTION

current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S") # Current time in specific format.

Config.read(config_file) # Read settings file.

source_path = Config.get('Folders', 'settings_path') # Get path from settings file.
backup_folder_path = Config.get('Folders', 'destination_path') # Get path from settings file.

file_name = str('"Settings Backup ' + current_time + '.7z"') # Create file name using current time.
backup_path = pathlib.Path(backup_folder_path) / file_name # Build target file path.

exe_path = Config.get('Folders', 'exe7z_path') # Get path from settings file.

cmd7zip = exe_path + ' a -t7z ' + str(backup_path) + ' ' + source_path + ' -mx=7' # Command line code. (Using compression level 7)
if (source_path != '') and (backup_path != '') and (exe_path != ''):
    subprocess.call(cmd7zip) # Backup process.
    time.sleep(5)
    quit()

# > MAIN FUNCTION

current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S") # Current time in specific format.

Config.read(config_file) # Read settings file.

source_path = Config.get('Folders', 'settings_path') # Get path from settings file.
backup_folder_path = Config.get('Folders', 'destination_path') # Get path from settings file.

file_name = str('"Settings Backup ' + current_time + '.7z"') # Create file name using current time.
backup_path = pathlib.Path(backup_folder_path) / file_name # Build target file path.

exe_path = Config.get('Folders', 'exe7z_path') # Get path from settings file.

cmd7zip = exe_path + ' a -t7z ' + str(backup_path) + ' ' + source_path + ' -mx=7' # Command line code. (Using compression level 7)
if (source_path != '') and (backup_path != '') and (exe_path != ''):
    subprocess.call(cmd7zip) # Backup process.
