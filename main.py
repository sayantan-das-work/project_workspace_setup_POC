import logging
import os
from stages import git_clone_stage, maven_build_stage

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger()

# Directory where the repository will be cloned
clone_dir_base = 'D:\\python_cloned_git_repo'

if __name__ == '__main__':
	api_name = "HTS-HandleTicketEventStreams"
	destination_path = f"{clone_dir_base}\\{api_name}"

	if os.path.isdir(destination_path):
		logger.info("The repository has been already cloned :: path to repo --> %s", destination_path)
		exit(0)

	if git_clone_stage.start_clone(api_name, destination_path) != 0:
		logger.error("Clone FAILED..!!")

	maven_build_stage.mvn_clean_install(destination_path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
