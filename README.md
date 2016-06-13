        ______            _            ______     _     __
       / ____/___  ____ _(_)___  ___  / ____/____(_)___/ /
      / __/ / __ \/ __ `/ / __ \/ _ \/ / __/ ___/ / __  /
     / /___/ / / / /_/ / / / / /  __/ /_/ / /  / / /_/ /
    /_____/_/ /_/\__, /_/_/ /_/\___/\____/_/  /_/\__,_/
                /____/


Installation:

1. Place EngineGrid.pyc in your Maya scripts folder:
    Windows: C:\Users\<Username>\Documents\maya\scripts
    OSx:  Library/preferences/Autodesk/maya/scripts

2. Create Maya shelf button to call script:
    Click the "Custom" tab on your tool shelf to have it ready.
    Open the Script Editor: Window > General Editors > Script Editor.
    In the lower half, click the Python tab and paste in the following two lines:

>import EngineGrid
>
>EngineGrid.EngineGrid()

    Drag to highlight the pasted text, then click+drag to an empty spot on your shelf.
    When prompted, select Python as the script type.
    You can rename the new shelf item by right-clicking it, selecting edit, and on the
    Shelves tab, under Shelf Contents, there is a Rename field.


Use:

    Open EngineGrid by clicking its shelf icon.
    Select the grid button for your target engine.
    
    Unity: 100cm(1m) = 1 unit in Unity. You can subdivide the grid from 1cm to 100cm(1m)
    by clicking the division buttons. This is most useful with grid snapping ON.

    UDK: 1 foot = 16 units in UDK. You can subdivide the grid from 1 unit to 16 units(1ft)
    by clicking the division buttons. This is most useful with grid snapping ON.

    Unity: 100cm(1m) = 1 unit in Unity. You can subdivide the grid from 1cm to 100cm(1m)
    by clicking the division buttons. This is most useful with grid snapping ON.

    Maya: restores default maya grid and units.

    Grow: increases the size of the grid itself by adding squares to the edges.
    Shrink: reduces the size of the grid itself by removing squares from the edges.

    About: links to the Tools page of krellgames.com

Thanks for using EngineGrid!