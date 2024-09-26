import logging

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger()


def log(log_type: str, msg: str, *msg_args):
	log_type = log_type.upper()
	if log_type == "INFO":
		if len(msg_args) > 0:
			logger.info(msg, msg_args)
		else:
			logger.info(msg)
	elif log_type == "ERROR":
		if len(msg_args) == 1:
			logger.error(msg, msg_args[0])
		else:
			err_msgs = ""
			for m in msg_args:
				err_msgs += f"-\t{m}\n"
				logger.error(msg, err_msgs)
	else:
		logger.error("Unknown logging type provided [%s]..!!", log_type)
