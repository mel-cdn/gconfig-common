import json


with open("updates.json") as f:
    update_list = json.load(f)
    


updates_strings = []
for ver, updates in update_list.items():
    updates_strings.append(ver)
    updates_strings.extend(updates)
    
print("|".join(updates_strings) + "GEND")


updates=[v2.15.1]|*NEW* Chaos Arena Macro (Private) - Dash to Portal Entrance - Private D|*ADJUST* Window Client Rename - NO VIP Required|*ADJUST* Baldus Macro (Private) - Add More Dungeon Settings|*ADJUST* ARH (Official) - Add More Dungeon Settings|*ADJUST* Train Macro (Official) - Adjust Entrance Location|[v2.15.0]|*NEW DUNGEON* Awakened Hazardous Valley (AHV) (Official Servers)|*ADJUST* Retarget Delay to milliseconds (ms)|[v2.14.1]|*NEW DUNGEON* Awakened Steamer Crazy - Train (Private & Official)|*NEW SETTINGS* Manual input of Change Target Delay|*ADJUST UI* Pause & Resume|[v2.13.0]|*NEW* Chaos Arena - Setup Level Runs for CA 1,2,3,4,5,6 & 7|*NEW* Dungeon Common Settings|[v2.12.0]|*NEW MACRO* Dungeon - Eternal Chaos Arena (ECA) (Official Servers)|*ADJUST* Re-channel for CABAL PH (Mercury & Cygnus)|*NEW* Re-channel up to 25 channels for CABAL NA & EU|[v2.11.3]|*FIX* Rechannel for Resolution 1280x720|*ADJUST* Train Macro Steaky & Door|[v2.11.2]|*NEW* PAUSE Macro Function|*ADJUST* Re-channel Capella Spot B|*ADJUST* Re-channel for CABAL PH|*ADJUST* Dungeon ARH: Maga & Bigcrup Routine|[v2.11.1]|*NEW MACRO* Dungeon - Radiant Hall Aprocrypha (ARH)|*NEW* Save Config for Rechannel, ARH, Train, CI, CA & Baldus|*FIX* Additional support for Windows 7 & 8|*UI ONLY* Step Highlights on Steamer (Train) Macro|[v2.11.0]|*NEW* Client version checker|*ADJUST* Chaos Infinity (CI): Private C - Server Entrance|[v2.10.8]|*NEW MACRO* Chaos Infinity (CI) (Private)|[v2.10.5]|*NEW MACRO* Steamer Crazy (Train) Macro (Private & Official)GEND