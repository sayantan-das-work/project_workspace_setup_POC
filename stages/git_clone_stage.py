import subprocess
from utils import logUtils


def start_clone(repository_url: str, clone_dest_path: str):
	logUtils.log("INFO", "Cloning Git Repo stage started...")
	repo_url = repository_url.strip() if (repository_url is not None) else ""
	if len(repo_url) == 0:
		logUtils.log("ERROR", "Invalid/Empty Git repository URL provided")

	logUtils.log("INFO", "Git repository URL : %s", repo_url)

	git_clone_cmd = f"git clone {repo_url} {clone_dest_path}"

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

	logUtils.log(
		"INFO",
		"Cloning Git Repo stage ended :: Repo Cloned Successfully :: Path to cloned repo --> %s",
		clone_dest_path
	)
	return 0
