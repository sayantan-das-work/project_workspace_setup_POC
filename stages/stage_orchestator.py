import os
import platform

from stages import collect_configs_stage, user_verification_stage, git_clone_stage, maven_build_stage
from utils import logUtils

__github_pa_sys_env_name__ = "GITHUB_PAT"


def start_setup_flow(api_name: str):
	api_name = api_name.strip()

	# stage 1: Getting setup configs
	configs = collect_configs_stage.collect(api_name)
	os_name = platform.system()
	github_personal_access_token = os.getenv(__github_pa_sys_env_name__)

	if configs is None:
		logUtils.log("ERROR", "Some configurations are missing for the given api..!!")
		return -1

	clone_dir_base = configs.get_target_dest()
	repo_url = configs.get_api_metadata().get_api_repo_url()

	logUtils.log("INFO", "Running Script on %s", os_name)
	logUtils.log("INFO", "Destination folder : %s", clone_dir_base)
	logUtils.log("INFO", "Repository URL : %s", repo_url)

	# stage 2: User verification on GitHub
	is_verified = user_verification_stage.verify_git_user(github_personal_access_token)
	if is_verified is False:
		logUtils.log(
			"INFO",
			"User verification failed...please check the github Personal Access Token"
		)
		return -401
	# stage 3: Clone project from GitHub into a specified folder
	logUtils.log("INFO", "Checking if folder already cloned")
	destination_path = f"{clone_dir_base}\\{api_name}"
	if os.path.isdir(destination_path):
		logUtils.log("INFO", "The repository has been already cloned :: path to repo --> %s", destination_path)
		return 0

	# repo_url = f"{repo_url}/{api_name}.git"
	if git_clone_stage.start_clone(repo_url, destination_path) != 0:
		logUtils.log("ERROR", "Clone of git repository failed")
		return -1

	# stage 4: Run 'mvn clean install' for the newly cloned project
	if maven_build_stage.mvn_clean_install(destination_path) != 0:
		logUtils.log("ERROR", "Maven build failed")
		return -2

	logUtils.log(
		"INFO",
		"Path to cloned Repository --> %s\n",
		destination_path
	)
	return 0
# stage 5: Show the modifications required to make in the project to run on local machine
# stage 6: [Optional: based on user choice] Setup minimum IDE configs and if possible open the ide
