# RV Shotgun plugin build tool
[RV](https://www.shotgunsoftware.com/rv) is an image, audio and video review software 
owned by Shotgun.

This is a script to assist with RV's package development in order to iterate and deploy easily.


### How it works
It searches inside the `plugin` folder and adds the contents to a zip _.rvpkg_ file.  
It can then install and add the file to the RV home area. In order to do 
this it uses the `rvpkg` application that comes with RV.  
It can start/restart RV to pick up the latest changes.

This allows a developer to make changes on their development environment and use the 
script to deploy and restart to see those reflected on RV.

##### Requirements

* RV-2021.0.0
* A `PACKAGE` yaml file following the RV convention inside the 'plugin' folder

### Installation

1. Clone repo
2. Copy or write your plugin code inside the `plugin` folder, include a `PACKAGE` yaml 
file and at least one `mu` or `python` file.
3. This step will bundle the files and create the `rvpkg` file inside a 'build' folder
    If you have python 3 as a default in your environment:
    ```bash
    python build-tool.py
   ```
   Otherwise:
   ```bash
   python3 build-tool.py
  ```
4. To install your plugin on RV:
    ```bash
    python build-tool.py --install
   ```
5. Build, install and restart all current RV sessions. You can do this after changing 
   the plugin files to pick up latest changes.
    ```bash
    python build-tool.py --install --restart
   ```


#### Tools used and compatible versions

* Written in Python 3
* Tested with RV-2021.0.0
* Aims to be completely cross-platform, however it has not been tested in MacOS.  
  
  

----------------------------------------------------------------------------
_Copyright 2020 Benteveo Ltd._  
_Licensed under the GNU General Public License v3.0_
