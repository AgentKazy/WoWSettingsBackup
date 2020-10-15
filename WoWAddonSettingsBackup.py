import os
import pathlib
from pathlib import Path
import configparser
import tkinter as tk
from tkinter import filedialog
import time
from datetime import datetime
import re
from re import search
import shutil
import glob

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
        input('Press ENTER to exit.')

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
        Config.write(cfg_settings) # Write settings to 'config_file'.
        cfg_settings.close() # Close file.
        #print('Configuration file created.') # Print file successfuly created.
    except IOError:
        print('Unable to create file. Check your permissions.')
        input('Press ENTER to exit.')

# > CHOOSE FOLDERS
root = tk.Tk()
root.withdraw()
new_settings = open(config_file,'r+', encoding='utf-8') # Open file in 'write' mode, UTF-8 encoding.
Config.read(config_file) # Read file settings.
addon_settings_flag = Config.get('Folders', 'settings_flag') # Get settings flag.
backup_destination_flag = Config.get('Folders', 'destination_flag') # Get destination flag.

if addon_settings_flag == 'False': # If flag is 'False':
    settings_folder_path = filedialog.askdirectory(title='Choose settings folder') # Prompt directory.
    if settings_folder_path == '': # If no folder is selected.
        pass
    else:
        Config.set('Folders','settings_flag','True') # Set flag to 'True'.
        Config.set('Folders','settings_path',str('"' + settings_folder_path + '"')) # Set settings path.
else:
    pass

if backup_destination_flag == 'False': # If flag is 'False':
    destination_folder_path = filedialog.askdirectory(title='Choose destination folder') # Prompt directory.
    if destination_folder_path == '': # If no folder is selected.
        pass
    else:
        Config.set('Folders','destination_flag','True') # Set flag to 'True'.
        Config.set('Folders','destination_path',str('"' + destination_folder_path + '"')) # Set destination path.
else:
    pass

try:
    Config.write(new_settings) # Write new settings to file.
    new_settings.close() # Close file.
except IOError:
    print('Unable to write to file. Check your permissions.')
    input('Press ENTER to exit.')

# > MAIN SETTINGS
current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S") # Current time in specific format.
Config.read(config_file) # Read settings file.
source_path = Config.get('Folders', 'settings_path') # Get path from settings file.
backup_folder_path = Config.get('Folders', 'destination_path') # Get path from settings file.
final_source_path = Path(re.sub('"', '', source_path)) # Create path object.
final_dest_path = Path(re.sub('"', '', backup_folder_path)) # Create path object.
file_name = Path('Settings Backup ' + current_time)

# > REMOVE OLD BACKUPS (KEEP 7)
files = final_dest_path.glob('Settings Backup*.zip')
file_list = []
for file in files:
    file_list.append(file)
file_list.sort()
for x in file_list[:-4]:
    Path.unlink(x)

# > BACKUP SETTINGS
if (source_path != '') and (backup_folder_path != ''): # and search('World of Warcraft', final_source_path):
    try:
        print('Settings path: ' + source_path) # Print source.
        print('Backup path: ' + backup_folder_path) # Print destination.
        shutil.make_archive(final_dest_path / file_name, 'zip', final_source_path.parent, final_source_path.name) # Backup process.
        print('') # Empty line.
        print('> Backup complete!') # Success!
        time.sleep(3) # Wait 3 seconds.
    except IOError:
        print('Unable to create backup folder at destination. Check your permissions.')
        input('Press ENTER to exit.')
else:
    print("Paths are empty and/or didn't save properly.")
    input('Press ENTER to exit.')
