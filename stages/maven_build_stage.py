import os.path
import subprocess
from utils import logUtils


def mvn_clean_install(dest_to_pom_folder: str):
	path_to_pom = f"{dest_to_pom_folder}\\pom.xml"
	logUtils.log("INFO", "Maven Build stage Started...")
	if os.path.isfile(path_to_pom):
		# os.chdir("D:")
		os.chdir(dest_to_pom_folder)
		logUtils.log("INFO", "Path to pom : %s", path_to_pom)
		logUtils.log("INFO", "Running mvn clean install")
		mvn_clean_install_cmd = "mvn clean install"
		stage = subprocess.run(
			mvn_clean_install_cmd.strip().split(" "),
			shell = True,
			text = True)
		if stage.returncode != 0:
			errors = []
			for error in stage.stderr.split("\n"):
				errors.append(f"\t{error}\n")
			errors.append(stage.stdout)
			logUtils.log("ERROR", "Error occurred during maven build :: ", errors)
			return stage.returncode
	else:
		logUtils.log("Error", "pom.xml Not Found at path %s", path_to_pom)

	logUtils.log("INFO", "Maven Build stage Ended Successfully...")
	return 0
