# project_workspace_setup_POC
This script will perform the basic workspace setup for any spring-boot project present on github.

It will clone the project int a specified folder on the local system as specified in the config file, then will run `mvn clean install` to install the maven dependencies

Environment variables to set:
- GITHUB_PAT => the personal access token generated on github
- AUTO_WORKSPACE_SETUP_CONFIG_HOME => the base path to the directory where you will be keeping the config files

To build the system specific executable file, run the following command on terminal in the project folder:

`pyinstaller --onefile --add-data "utils;utils" --add-data "models;models" --add-data "stages;stages" main.py`

After creating the executable file you can directly run it

Store the csv config files under the same directory