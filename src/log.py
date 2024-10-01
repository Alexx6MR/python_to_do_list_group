import datetime;

class FileLogger:
	def __init__(self, log_file):
		self.log_file = log_file
		self.log_handle = open(self.log_file, 'a')

	def log(self, message):
		date = datetime.datetime.now()
		self.log_handle.write(f'[{date}] INFO | {message}\n')

	def log_error(self, message):
		date = datetime.datetime.now()
		self.log_handle.write(f'[{date}] ERROR | {message}\n')
	
	def log_db_query(self, query):
		date = datetime.datetime.now()
		self.log_handle.write(f'[{date}] DB_QUERY | {query}\n')

	def log_db_query_data(self, query, dataTuple):
		date = datetime.datetime.now()
		self.log_handle.write(f'[{date}] DB_QUERY | {query} | Data: {dataTuple}\n')