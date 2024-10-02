import csv
import os

from models.ApiConfig import ApiConfig
from utils import logUtils
from models import ApiConfig, ConfigData


__config_file_home__ = os.getenv('AUTO_WORKSPACE_SETUP_CONFIG_HOME')
__path_to_api_config_file__ = f'{__config_file_home__}\\auto_workspace_setup_api_configs.csv'
__path_to_target_dest_config_file__ = f'{__config_file_home__}\\auto_workspace_setup_dest_config.csv'
__config__ = ConfigData.ConfigData()


def collect(api_name):
	api_configs = __read_csv_for_api_cfg__(api_name)
	if api_configs is None:
		logUtils.log("INFO", f"No configuration found for API %s", api_name)
		return None

	cloned_repo_target_dest = __read_csv_for_api_clone_dest__(api_configs.get_api_tool_type())
	if cloned_repo_target_dest is None:
		logUtils.log("INFO", f"No target destination found to clone API %s", api_name)
		return None

	__config__.set_api_metadata(api_configs)
	__config__.set_target_dest(cloned_repo_target_dest)

	return __config__


# Read csv file and get the required configs for project
def __read_csv_for_api_cfg__(api_name) -> ApiConfig.ApiConfig | None:
	try:
		with open(__path_to_api_config_file__, mode = 'r', newline = '', encoding = 'utf-8') as file:
			reader = csv.reader(file)
			for row in reader:
				if row[0].strip() == api_name:
					api_config = ApiConfig.ApiConfig()
					api_config.set_api_name(row[0].strip())
					api_config.set_api_tool_type(row[1].strip())
					api_config.set_api_repo_url(row[2].strip())
					return api_config
			return None
	except FileNotFoundError as exception:
		logUtils.log("ERROR", "Error occurred :: %s", exception)
		logUtils.log(
			"ERROR",
			"Unable to locate configs files at location %s",
			__path_to_api_config_file__)


# Read csv file and get the required destination path for project cloning
def __read_csv_for_api_clone_dest__(tool_name) -> str | None:
	try:
		with open(__path_to_target_dest_config_file__, mode = 'r', newline = '', encoding = 'utf-8') as file:
			reader = csv.reader(file)
			for row in reader:
				if row[0].strip() == tool_name and len(row[1].strip()) > 0:
					return row[1].strip()
		return None
	except FileNotFoundError as exception:
		logUtils.log("ERROR", "Error occurred :: %s", exception)
		logUtils.log(
			"ERROR",
			"Unable to locate configs files at location %s",
			__path_to_target_dest_config_file__)
