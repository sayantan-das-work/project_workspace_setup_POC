import logging

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger()


def log(log_type: str, msg: str, *msg_args):
	log_type = log_type.upper()
	if log_type == "INFO":
		if len(msg_args) > 0:
			logger.info(msg, prepare_msg_args(msg_args))
		else:
			logger.info(msg)
	elif log_type == "ERROR":
		if len(msg_args) > 0:
			logger.error(msg, prepare_msg_args(msg_args))
		else:
			logger.error(msg)
	else:
		logger.error("Unknown logging type provided [%s]..!!", log_type)


def prepare_msg_args(msg_args: tuple):
	if len(msg_args) == 1:
		return msg_args[0]
	elif len(msg_args) > 1:
		msg_to_ret = ""
		for m in msg_args:
			msg_to_ret += f"-\t{m}\n"
		return msg_to_ret
	return tuple("")
