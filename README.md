# project-management-tool
I'll guide you through the process of converting your Python script into a standalone executable (.exe) file that you can launch with a double-click. This will make it easy to use without needing to run Python commands.

# Creating an Executable (.exe) from Your Python Script

There are two excellent tools for this purpose: PyInstaller and Auto-py-to-exe (which is a GUI for PyInstaller). I'll show you both methods.

## Method 1: Using PyInstaller directly

1. **Install PyInstaller**:
   ```
   pip install pyinstaller
   ```

2. **Navigate to your script directory** in Command Prompt or PowerShell:
   ```
   cd C:\Users\DELL\Downloads\lat-long-to-row-main
   ```

3. **Create the executable** with this command:
   ```
   pyinstaller --onefile --windowed project_flow.py
   ```
   
   The options mean:
   - `--onefile`: Create a single executable file
   - `--windowed`: Don't show a console window when running the app

4. **Find your executable** in the `dist` folder that PyInstaller creates. You can copy this .exe file anywhere and run it with a double-click.

## Method 2: Using Auto-py-to-exe (Easier with GUI)

1. **Install Auto-py-to-exe**:
   ```
   pip install auto-py-to-exe
   ```

2. **Launch the GUI**:
   ```
   auto-py-to-exe
   ```

3. **In the GUI**:
   - Select your script file (`project_flow.py`)
   - Choose "One File" option
   - Choose "Window Based" option (hide the console)
   - Click "Convert .py to .exe"

4. **After conversion**, you'll find your .exe file in the output location (which you can specify in the GUI).

## Creating a Shortcut (Optional)

1. **Create a desktop shortcut** by right-clicking the .exe file
2. Select "Create shortcut"
3. Move the shortcut to your desktop or preferred location

## Additional Recommendations

1. **Include an icon**: To make your app look professional, add an icon with:
   ```
   pyinstaller --onefile --windowed --icon=your_icon.ico project_flow.py
   ```

2. **Create a named executable**: To give your app a better name:
   ```
   pyinstaller --onefile --windowed --name="Drone Inspection Tracker" project_flow.py
   ```

3. **If your app uses additional files** (images, data files), you might need to include them:
   ```
   pyinstaller --onefile --windowed --add-data "your_data_folder;your_data_folder" project_flow.py
   ```

## Troubleshooting Common Issues

1. **Missing dependencies**: If the .exe doesn't run, you might need to include additional hidden imports:
   ```
   pyinstaller --onefile --windowed --hidden-import=tkinter project_flow.py
   ```

2. **Antivirus detection**: Some antivirus software may flag PyInstaller executables. This is usually a false positive. You may need to add an exception in your antivirus software.

3. **Data file access**: If your app needs to access the JSON data file, make sure it uses relative paths that will work in an executable context.

