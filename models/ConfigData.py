from models import ApiConfig


class ConfigData:

	def __init__(self):
		super().__init__()
		self.__target_dest__ = None
		self.__api_metadata__ = None

	def get_api_metadata(self):
		return self.__api_metadata__

	def set_api_metadata(self, api_metadata: ApiConfig):
		self.__api_metadata__ = api_metadata

	def get_target_dest(self) -> str:
		return self.__target_dest__

	def set_target_dest(self, target_dest: str):
		self.__target_dest__ = target_dest
