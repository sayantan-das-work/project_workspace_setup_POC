import subprocess
from utils import logUtils

# URL of the GitHub repository you want to clone
repo_url_base = 'https://github.com/Sayantan500'


def start_clone(api_name_to_clone: str, clone_dest_path: str):
	logUtils.log("INFO", "Cloning Git Repo stage started...")
	repo_url = f'{repo_url_base}/{api_name_to_clone}.git'
	logUtils.log("INFO", "Git repository URL : %s", repo_url)

	git_clone_cmd = f"git clone {repo_url} {clone_dest_path}"
	print(f">> git clone cmd arr : {git_clone_cmd.strip().split(sep = " ")}")

	git_clone_stage_cmd = subprocess.run(
		git_clone_cmd.strip().split(sep = " "),
		shell = True,
		capture_output = True,
		text = True)

	if git_clone_stage_cmd.returncode != 0:
		errors = ""
		for error in git_clone_stage_cmd.stderr.split("\n"):
			errors += f"\t{error}\n"
		logUtils.log("ERROR", "Error occurred when cloning git repo : \n%s", errors)

	logUtils.log("INFO", "Cloning Git Repo stage ended :: Repo Cloned Successfully :: Path to cloned repo --> %s")
	return 0
