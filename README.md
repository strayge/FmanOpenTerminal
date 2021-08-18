# FmanOpenTerminal

## Overview

Fman Plugin to open [iTerm2](https://iterm2.com/) / [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab) at the current directory (instead of opening default Terminal.app / cmd.exe).  
When `iTerm2` / `Windows Terminal` is not installed, the regular command line apps opens.

This plugin overrides the default `open_terminal` command, so F9 or any custom binding (if it was changed) still works as before.

In addion it is also possible to open the terminal using the context menu.  
Both file & folder context menus have new `Open Terminal` (and `Open Directory` for connsistency) entries.

## Installation
[Ctrl+Shift+P -> Install Plugins -> FmanOpenTerminal](https://fman.io/docs/installing-plugins)

## Usage
- Click F9
- Open context menu and click at "New Terminal"
- Ctrl+Shift+p -> Open Terminal

## Screenshots
### "New Terminal" entry in the folder context menu
!["New Terminal" entry in the folder context menu](https://user-images.githubusercontent.com/1760091/129905850-aa3c36c7-cea2-4946-baba-fdc748eb983e.jpg)  

### "New Terminal" entry in the file context menu
!["New Terminal" entry in the file context menu](https://user-images.githubusercontent.com/1760091/129906039-850b46de-739b-44f2-a9f4-6657a4eb4fc2.jpg)  

### Showing the plugin in action
![Showing the plugin in action](https://user-images.githubusercontent.com/1760091/129906094-94e3154b-6e2b-4912-8381-b162ed8879f5.jpg)  

## Disclaimer
The theme in the last screenshot was changed using [Fman Alternative Colors](https://github.com/strayge/FmanAlternativeColors) plugin  
The bottom menu was created using [Fman Action Bar](https://github.com/strayge/FmanActionBar) plugin  
The two dots (..) are presented using [Fman Dot Entries](https://github.com/strayge/FmanDotEntries) plugin  
