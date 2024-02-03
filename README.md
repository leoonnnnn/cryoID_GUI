# cryoID_GUI

## TLDR, to run the GUI: 
```
python3 main_cryoID.py
```
or
```
python3 main_cryoID_experimental.py
```

## what files are what?
- **.ui** are for Designer (QtDesigner). They're not necessary to run the actual program. <br>
- **.py** with the same name are generated from the .ui's using pyuic5 (like so: ```pyuic5 placeholder.ui -o placeholder.py```) <br>
- **main_cryoID.py** is what you actually run (or main_cryoID_experimental.py) <br>
- **search_pool** and **search_support** .py do the heavy lifting. 
    - They're from the original cryoID repo but translated into python3 by Qibo (literally just a few syntax things. run a diff if you're curious.) <br>
- **OG_cryoID.py** is also from the original cryoID repo and translated into python3 by Qibo. But it's entirely unneeded (we're essentially remaking this part). You can run this file to see how the old cryoID works. <br>
- **svg assets** is a folder for any button icons, other images, etc. <br>
    - currently only has a file upload icon svg <br>
    - **file_upload.qrc** is just something generated in Designer to add the svg in <br>

## notes about editing the GUI
- main_cryoID.py uses cryoID_v2.py <br>
- main_cryoID_experimental.py uses cryoID_v2_1.py &nbsp;&nbsp;&nbsp; (the naming sucks lol)<br>
<br>
- **DONT directly edit the .py files generated from pyuic5** (so cryoID_v2.py and cryoID_v2_1.py) <br>
    - well actually you can if you want, but your changes will get overwritten if you run pyuic5 again with the same output file name <br>
    - also you can name the pyuic5 output file whatever you want (say you want to save a dif version). BUT make sure to also change the name of the import in the main python file. <br>
    ```9: from cryoID_v2_1 import Ui_cryoID``` <br>
    cryoID_v2_1 refers to cryoID_v2_1.py, so if you save the pyuic5 output file as a different name, change this. <br>
    Ui_cryoID comes from the object name of the QMainWindow (or whatever template/form you built your GUI on). If you change the name of this in Designer, also update it here. <br>
- Better practice (since we're using Designer) is to instead edit the .ui files in Designer and then generate the .py files again with pyuic5 <br>
- *Alternatively, you could hand code the whole GUI and you wouldn't need Designer at all.* <br>

## self TODOs:
- low prio/cosmetic: finish adding all the tool tips (tool tips are the messages that pop up when you hover over a button or textbox). Just go to OG_cryoID.py and copy the toolTip messages and then go into Designer and right click on a button and click "Change toolTip".
- high prio: finish the error messages/status bar
- high prio: get the scripts to work with our GUI. It should work as is; test it by printing an error message to the status bar like how the original cryoID does. Need to download Phenix again to actually test full funcionality.
- medium prio: get the help page button working (could have it pop out as a dialog box/messagebox)
- medium prio: consider remaking the GUI in Designer with proper layouts because some of the textboxes overlap when you run the python file. But it might just be an issue on my end. Someone else should run the GUI too just to check.
- low prio/cosmetic: polish up the GUI and modernize the look, rounded buttons, button icons, etc. (found some tutorials with nice looking designs that I'll check out later)
- semi-high prio: figure out how to implement a "save" progress feature (Like say it's taking too long to run and you wanna pause it to free up resources to do something else). Use the pickle module? Would have to look at the actual ML code. <br>
edit: Qibo said he already implemented an autosave feature, so just figure out how to add that to the GUI.