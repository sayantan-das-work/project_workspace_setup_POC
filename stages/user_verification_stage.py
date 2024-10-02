import requests

from utils import logUtils

__url__ = "https://api.github.com/octocat"
__headers__ = {
	"X-GitHub-Api-Version": "2022-11-28",
	"Content-Type": "application/json"
}


def verify_git_user(github_pat: str):
	if github_pat is None or len(github_pat) == 0:
		logUtils.log("ERROR", "Github personal access token is not found or empty")
		return False

	bearer_auth: str = f"Bearer {github_pat}"
	__headers__['Authorization'] = bearer_auth
	response = requests.get(__url__, headers = __headers__)

	# Check the response status and content
	return response.status_code == 200
