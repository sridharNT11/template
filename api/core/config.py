class Config(object):
	DEBUG = False
	TESTING = False
	DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
	DATABASE_URI = 'mysql://root:@127.0.0.1/registration'
	
class DevelopmentConfig(Config):
	DEBUG = True
	