# cryoID_GUI

## TLDR, to run the GUI: 
```
python3 main_cryoID_developmental.py
```


## what files are what?
- **main_cryoID_developmental.py** is what you actually run (or main_cryoID.py, whatever the current name is)
- **.ui** files are for Designer (QtDesigner). Only need them for making changes to the GUI's skin, don't need them to run the GUI.
- **.py** files with the same name are python code generated from the .ui files using pyuic5 (like so: ```pyuic5 placeholder.ui -o placeholder.py```)
    - _optionally in the imports, you could skip using the .py file and just use the .ui file (there's a python package that does that)_
- **svg assets** is a folder for any button icons, other images, etc.
    - currently only has a file upload icon svg
    - **file_upload.qrc** is just something generated in Designer to add the svg in
- **chimerax_launcher.py** is imported as a module into main, but also works as a standalone script.

## notes about editing the GUI
- To change buttons and other visual stuff about the GUI, edit the .ui file, and generate new python code with pyuic5.
- Then make any necessary changes in main_cryoID_developmental.py (such as updating button names if you changed them in Designer, attaching functions to buttons, etc.)
- **DON'T directly edit the .py files generated from pyuic5**
    - well actually you can if you want, but your changes will get overwritten if you run pyuic5 again with the **same** output file name
    - also if you change the name of the output file (the generated python file), make sure to update it in the import statement in the main python file. <br>
    ```line 11: from cryoID_v2_exp_FINALPRESVERSION import Ui_cryoID``` <-- this line <br>
    cryoID_v2_exp_FINALPRESVERSION refers to cryoID_v2_exp_FINALPRESVERSION.py, so if you save the pyuic5 output file as a different name, change this. <br>
    Ui_cryoID comes from the object name of the QMainWindow (or whatever template/form you built your GUI on). If you change the name of this in Designer, also update it here.
- **TLDR: edit the .ui file in Designer and then generate the .py file again with pyuic5**
    - *Alternatively, you could hand code the whole GUI and you wouldn't need Designer at all.*


## TODOs for myself
- maybe rename the files
    - change main_cryoID.py to main_cryoID_gui.py
- clean up imports in main
- displaying file tree in sidebar (only got it working in a separate file, still working on integrating it)
    - replace the checkboxes in the sidebar with the file tree. some functionality might change but should be pretty quick modifications


note to self: All my other developmental code is in C:\Users\noelu\Python Projects\PyQt GUI practice\QtDesigner_practice\draftGUI. There's a bunch of examples and other junk in there. Copy what's needed to here and make the final touches here. And then maybe copy it back over to that clusterfuck folder (just make a new folder under backups with the date as the name).