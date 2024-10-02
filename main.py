import logging

from utils.logUtils import log
from stages import stage_orchestator

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger()

# Directory where the repository will be cloned
clone_dir_base = 'D:\\python_cloned_git_repo'

if __name__ == '__main__':
	# input from user
	api_name = input("Enter Repository Name : ").strip()
	ret_code = stage_orchestator.start_setup_flow(api_name)
	if ret_code < 0:
		log("Error", "Script ended with errors :: %s", ret_code)

	log("INFO", "Press ~ to exit")
	while input().strip() != '~':
		log("INFO", "Press ~ to exit")
