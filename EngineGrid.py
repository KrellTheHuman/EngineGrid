#######################################################################################################################
#
# EngineGrid
# by Krell
# krellgames.com
#
#######################################################################################################################

import maya.cmds as cmds
import sys
import maya.mel as mel


# builds window UI and buttons
def EngineGrid():
    version = " v1.1"
    title = "EngineGrid"

    # colors
    frameBGC = [0.17, 0.30, 0.30]
    unityBGC = [0.25, 0.25, 0.35]
    udkBGC = [0.35, 0.25, 0.25]
    cryengineBGC = [0.25, 0.35, 0.25]
    mayaBGC = [0.33, 0.33, 0.33]

    # kills open instance of window
    if cmds.window("EngineGrid", exists=True):
        cmds.deleteUI("EngineGrid")

    # creates window and assigns title
    cmds.window("EngineGrid", title=title + version, iconName=title + version, menuBar=False, minimizeButton=False, maximizeButton=False, sizeable=False)

    # overall parent frame that holds all children
    cmds.columnLayout("gridSettingsColumn", columnWidth=261)
    cmds.separator(style="in")

    # frame around all buttons with instruction to set grid. is collapsible in Maya 2013 despite flag set to false
    cmds.frameLayout('gridButtonsColumn', label="select your grid", collapsable=False, backgroundColor=frameBGC, collapse=False, borderStyle="etchedIn", width=261, marginHeight=1, parent="gridSettingsColumn")

    # grid selection buttons
    cmds.rowColumnLayout(numberOfColumns=4, columnWidth=[(1, 64), (2, 64), (3, 64), (4, 64)], parent="gridButtonsColumn")
    # changeGridSettings(set, size, spacing, divisions, nearClipPlane, farClipPlane, gridAxisColor, gridHighlightColor, gridColor, trans)
    cmds.button(h=64, label="Unity", bgc=unityBGC, c=lambda z: changeGridSettings("unity", 150, 10, 1, 0.1, 100000.0, 1, 3, 2, 10000.0))
    cmds.button(h=64, label="UDK", bgc=udkBGC, c=lambda z: changeGridSettings("udk", 512, 16, 1, 0.1, 100000.0, 1, 3, 2, 10000.0))
    cmds.button(h=64, label="CryEngine", bgc=cryengineBGC, c=lambda z: changeGridSettings("cryengine", 150, 10, 1, 0.1, 100000.0, 1, 3, 2, 10000.0))
    cmds.button(h=64, label="Maya", bgc=mayaBGC, c=lambda z: changeGridSettings("maya", 12, 5, 5, 0.1, 10000.0, 1, 3, 3, 100.1))

    # grid square division text
    cmds.rowColumnLayout('unityDivUnits', visible=False, numberOfColumns=3, columnWidth=[(1, 125), (2, 28), (3, 60)], parent="gridButtonsColumn")
    cmds.text(align="left", label="                 1 grid square is ")
    cmds.intField('unityMultiplier', min=0, value=100)
    cmds.text(label=" centimeters")

    cmds.rowColumnLayout('udkDivUnits', visible=False, numberOfColumns=3, columnWidth=[(1, 140), (2, 20), (3, 30)], parent="gridButtonsColumn")
    cmds.text(align="left", label="                      1 grid square is ")
    cmds.intField('udkMultiplier', min=0, value=16)
    cmds.text(label=" units")

    cmds.rowColumnLayout('cryengineDivUnits', visible=False, numberOfColumns=3, columnWidth=[(1, 125), (2, 28), (3, 60)], parent="gridButtonsColumn")
    cmds.text(align="left", label="                 1 grid square is ")
    cmds.intField('cryengineMultiplier', min=0, value=100)
    cmds.text(label=" centimeters")

    # grid division buttons
    cmds.rowColumnLayout('unityDivButtons', visible=False, numberOfColumns=5, columnWidth=[(1, 51), (2, 51), (3, 52), (4, 51), (5, 51)], parent="gridButtonsColumn")
    cmds.button(h=32, label="1cm", bgc=unityBGC, command=lambda z: setGridDivisions(100, 1))
    cmds.button(h=32, label="10cm", bgc=unityBGC, command=lambda z: setGridDivisions(10, 10))
    cmds.button(h=32, label="25cm", bgc=unityBGC, command=lambda z: setGridDivisions(4, 25))
    cmds.button(h=32, label="50cm", bgc=unityBGC, command=lambda z: setGridDivisions(2, 50))
    cmds.button(h=32, label="100cm", bgc=unityBGC, command=lambda z: setGridDivisions(1, 100))

    cmds.rowColumnLayout('udkDivButtons', visible=False, numberOfColumns=5, columnWidth=[(1, 51), (2, 51), (3, 52), (4, 51), (5, 51)], parent="gridButtonsColumn")
    cmds.button(h=32, label="1", bgc=udkBGC, command=lambda z: setGridDivisions(16, 1))
    cmds.button(h=32, label="2", bgc=udkBGC, command=lambda z: setGridDivisions(8, 2))
    cmds.button(h=32, label="4", bgc=udkBGC, command=lambda z: setGridDivisions(4, 4))
    cmds.button(h=32, label="8", bgc=udkBGC, command=lambda z: setGridDivisions(2, 8))
    cmds.button(h=32, label="16", bgc=udkBGC, command=lambda z: setGridDivisions(1, 16))

    cmds.rowColumnLayout('cryengineDivButtons', visible=False, numberOfColumns=5, columnWidth=[(1, 51), (2, 51), (3, 52), (4, 51), (5, 51)], parent="gridButtonsColumn")
    cmds.button(h=32, label="1cm", bgc=cryengineBGC, command=lambda z: setGridDivisions(100, 1))
    cmds.button(h=32, label="10cm", bgc=cryengineBGC, command=lambda z: setGridDivisions(10, 10))
    cmds.button(h=32, label="25cm", bgc=cryengineBGC, command=lambda z: setGridDivisions(4, 25))
    cmds.button(h=32, label="50cm", bgc=cryengineBGC, command=lambda z: setGridDivisions(2, 50))
    cmds.button(h=32, label="100cm", bgc=cryengineBGC, command=lambda z: setGridDivisions(1, 100))

    # grid grow/shrink and "about" buttons
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, 85), (2, 86), (3, 85)], p="gridButtonsColumn")
    cmds.button(h=20, label="grow", bgc=frameBGC, command=lambda z: gridSizeChange("up", 50))
    cmds.button(h=20, label="shrink", bgc=frameBGC, command=lambda z: gridSizeChange("down", 50))
    cmds.button(h=20, label="about", bgc=frameBGC, command=lambda z: cmds.showHelp('http://krellgames.com/tools.html', absolute=True))

    # prints version and author info to the command line
    consolePrint((title + version), " by Krell of krellgames.com")

    # draws the main window
    cmds.showWindow()
    cmds.window("EngineGrid", e=True, resizeToFitChildren=True, sizeable=True, height=190, width=261)
    cmds.frameLayout('gridButtonsColumn', edit=True, cc=lambda *args: editWinSize('EngineGrid', 'gridButtonsColumn'))


# resize window to fit children
def editWinSize(winName, flName):
    windowHeight = cmds.window(winName, q=True, height=True)
    frameHeight = cmds.frameLayout(flName, q=True, height=True)
    height = windowHeight - frameHeight

    if height > 0:
        cmds.window(winName, e=True, height=height)
    else:
        return None


# prints to command line
def consolePrint(message, num):
    sys.stdout.write(message + str(num) + '\n')


# display number of units in text box, as well as print to the command line
def setGridDivisions(which, units):
    cmds.grid(divisions=which)
    cmds.intField('unityMultiplier', edit=True, value=units)
    cmds.intField('udkMultiplier', edit=True, value=units)
    cmds.intField('cryengineMultiplier', edit=True, value=units)
    consolePrint("Grid square size changed to ", units)


# grow or shrink grid and print to command line
def gridSizeChange(direction, amount):
    currentGridSize = cmds.grid(query=True, size=True)
    if direction == 'up':
        cmds.grid(size=(currentGridSize + amount))
        consolePrint("Grid has grown", "")
    elif direction == 'down':
        cmds.grid(size=(currentGridSize - amount))
        consolePrint("Grid has shrunk", "")


# changes grid settings. shows/hides division text and buttons based on grid button set selection
# changeGridSettings(set, size, spacing, divisions, nearClipPlane, farClipPlane, gridAxisColor, gridHighligtColor, gridColor, trans)
def changeGridSettings(set, s, sp, div, ncp, fcp, gac, ghc, gc, trans):
    cmds.displayColor('gridAxis', gac, c=True, dormant=True)
    cmds.displayColor('gridHighlight', ghc, c=True, dormant=True)
    cmds.displayColor('grid', gc, c=True, dormant=True)
    cmds.setAttr('perspShape.farClipPlane', fcp)
    cmds.setAttr('perspShape.nearClipPlane', ncp)
    cmds.setAttr('topShape.farClipPlane', fcp)
    cmds.setAttr('topShape.nearClipPlane', ncp)
    cmds.setAttr('sideShape.farClipPlane', fcp)
    cmds.setAttr('sideShape.nearClipPlane', ncp)
    cmds.setAttr('frontShape.farClipPlane', fcp)
    cmds.setAttr('frontShape.nearClipPlane', ncp)
    cmds.setAttr('top.translateY', trans)
    cmds.setAttr('front.translateZ', trans)
    cmds.setAttr('side.translateX', trans)

    # sets Unity grid settings
    if set == "unity":
        # shows unity division text and buttons, hides others
        cmds.rowColumnLayout('unityDivUnits', edit=True, visible=True)
        cmds.rowColumnLayout('udkDivUnits', edit=True, visible=False)
        cmds.rowColumnLayout('cryengineDivUnits', edit=True, visible=False)
        cmds.rowColumnLayout('unityDivButtons', edit=True, visible=True)
        cmds.rowColumnLayout('udkDivButtons', edit=True, visible=False)
        cmds.rowColumnLayout('cryengineDivButtons', edit=True, visible=False)
        # sets division text default
        cmds.intField('unityMultiplier', edit=True, value=100)
        # sets grid, prints to console, sets camera, and sets Maya units to centimeters
        cmds.grid(size=s, spacing=sp, divisions=div)
        consolePrint("Unity grid activated", "")
        mel.eval("viewSet -animate `optionVar -query animateRollViewCompass` -home;")
        mel.eval('currentUnit -linear "cm";')

    #sets UDK grid settings
    elif set == "udk":
        # shows udk division text and buttons, hides others
        cmds.rowColumnLayout('unityDivUnits', edit=True, visible=False)
        cmds.rowColumnLayout('udkDivUnits', edit=True, visible=True)
        cmds.rowColumnLayout('cryengineDivUnits', edit=True, visible=False)
        cmds.rowColumnLayout('unityDivButtons', edit=True, visible=False)
        cmds.rowColumnLayout('udkDivButtons', edit=True, visible=True)
        cmds.rowColumnLayout('cryengineDivButtons', edit=True, visible=False)
        # sets division text default
        cmds.intField('udkMultiplier', edit=True, value=16)
        # sets grid, prints to console, sets camera, and sets Maya units to centimeters
        cmds.grid(size=s, spacing=sp, divisions=div)
        consolePrint("UDK grid activated", "")
        mel.eval("viewSet -animate `optionVar -query animateRollViewCompass` -home;")
        mel.eval('currentUnit -linear "cm";')

    #sets CryEngine grid settings
    elif set == "cryengine":
        # shows cryengine division text and buttons, hides others
        cmds.rowColumnLayout('unityDivUnits', edit=True, visible=False)
        cmds.rowColumnLayout('udkDivUnits', edit=True, visible=False)
        cmds.rowColumnLayout('cryengineDivUnits', edit=True, visible=True)
        cmds.rowColumnLayout('unityDivButtons', edit=True, visible=False)
        cmds.rowColumnLayout('udkDivButtons', edit=True, visible=False)
        cmds.rowColumnLayout('cryengineDivButtons', edit=True, visible=True)
        # sets division text default
        cmds.intField('cryengineMultiplier', edit=True, value=100)
        # sets grid, prints to console, sets camera, and sets Maya units to centimeters
        cmds.grid(size=s, spacing=sp, divisions=div)
        consolePrint("CryEngine grid activated", "")
        mel.eval("viewSet -animate `optionVar -query animateRollViewCompass` -home;")
        mel.eval('currentUnit -linear "cm";')

    #restores Maya grid settings
    elif set == "maya":
        # hides all division text and buttons
        cmds.rowColumnLayout('unityDivUnits', edit=True, visible=False)
        cmds.rowColumnLayout('udkDivUnits', edit=True, visible=False)
        cmds.rowColumnLayout('cryengineDivUnits', edit=True, visible=False)
        cmds.rowColumnLayout('unityDivButtons', edit=True, visible=False)
        cmds.rowColumnLayout('udkDivButtons', edit=True, visible=False)
        cmds.rowColumnLayout('cryengineDivButtons', edit=True, visible=False)
        # sets grid, prints to console, sets camera, and sets Maya units to centimeters
        cmds.grid(size=s, spacing=sp, divisions=div)
        consolePrint("Maya grid restored", "")
        mel.eval("viewSet -animate `optionVar -query animateRollViewCompass` -home;")
        mel.eval('currentUnit -linear "cm";')