class ApiConfig:

	def __init__(self):
		super().__init__()
		self.__api_name__ = None
		self.__api_tool_type__ = None
		self.__api_repo_url__ = None

	def get_api_name(self) -> str:
		return self.__api_name__

	def set_api_name(self, api_name):
		self.__api_name__ = api_name

	def get_api_tool_type(self):
		return self.__api_tool_type__

	def set_api_tool_type(self, api_tool_type):
		self.__api_tool_type__ = api_tool_type

	def get_api_repo_url(self):
		return self.__api_repo_url__

	def set_api_repo_url(self, api_repo_url):
		self.__api_repo_url__ = api_repo_url
