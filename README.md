# Name
- Package Remover Interface for Android Debug Bridge (PRI for ADB)

## Motivation
- When using Android Debug Bridge(ADB) to remove packages, you have to type the command "adb shell pm uninstall --user 0 _package_" for each package you want to remove.

## Description
- Now, with the space bar, you can select as many packages as you want, and remove them simultaneously. You can also search for a specific package.
- ADB's _pm uninstall_ is useful to remove those applications that come preinstalled on your smartphone by your provider or one of the FAANGs :vampire:

## Disclaimer
- You can absolutely break your smartphone by removing packages that the system relies upon. Please do your research on the packages you want to remove. If you break your smartphone, a factory data reset should be performed to go back to a useful state but everything will, of course, be lost.
- As alternatives to using a real smartphone or tablet you can create an emulator in Android Studio:
	- https://developer.android.com/studio  ...AND/OR...	- https://developer.android.com/studio/run/emulator
- I'm not associated with Android in any way. They are not associated with PRI nor are responsible for anything you do with it. PRI is not intended to replace ADB.
- Android is not economically responsible for your phone or tablet if you break it.

## Requirements
- Linux (Kernel 5.10/Debian)
- Python 3.9.2
- Android Debug Bridge (ADB) (Contained in the Android SDK Platform-Tools package) https://developer.android.com/studio/releases/platform-tools (Linux version)
- Or you can install ADB directly from the command line:	
	- sudo apt-get install android-tools-adb  ...OR...
	- sudo apt-get install adb

## Dependencies
- Inquirer 2.7.0 -- Inquirer is used so we can apply the checkbox functionality to select multiple packages.

## Features
- Option 1: List all packages and select for removal
	- You can remove packages as with ADB but many at once.
- Option 2: Search packages by keyword
    - You can also search for a specific package and all instances will be shown and removable.
- Option 3: Spawn ADB shell
    - In case you need an ADB shell in the same window.
- Option 4: Exit

## Smartphone Setup
1. Your smartphone has to be in developer mode. Generally in Settings > About Phone > Software Info and tap on Build Number around 7 times until you are a developer.
2. USB Debugging must be enabled in, the now available, Developer Options.
3. The first time you connect your smartphone to the computer (after USB Debugging), you will be prompted to accept an RSA key fingerprint, to confirm that USB Debugging is allowed.

## How to install / run
1. Clone or download package
2. pip install inquirer
3. python pack_remover.py
- *Note*: On first run, the program will create a _package_list.txt_ file in your home folder (Linux) with the list of packages. You don't have to (and should not) modify this file directly.
<img src="images/pri_0th.png" width="375" height="100">

## How to use
### Option 1: List all packages and select for removal
- Navigate up and down the list with the arrow keys.
- With the space bar, select the package(s) you want to remove.
- Press Enter to remove the package(s).
- Confirm with "y" or cancel with "n".
<img src="images/pri_1st.png" width="350" height="250">

### Option 2: Search packages by keyword
- When selected, you are prompted to input a search term. You can search any part of a Java package hierarchy which takes the form of: _com.example.mypackage_. Some of these packages have the name of the app or the company in them, you can use that as a search term.
- After that, you proceed with instructions for option 1.
<img src="images/pri_2nd.png" width="350" height="175">

### Option 3: Spawn ADB shell
- You can spawn an ADB shell in case you quickly need other functionality from ADB.
<img src="images/pri_3rd.png" width="325">

### Option 4: Exit
- Option 4 makes coffee.

## Next version
- It would be awesome if this could be adapted for the web. Maybe in a while.
