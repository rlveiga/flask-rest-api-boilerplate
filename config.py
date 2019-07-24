import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to figure out long ass string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True

	# Should set environment variables for database uri in the future

	SQLALCHEMY_DATABASE_URI = 'postgresql://@USERNAME:@localhost/DATABASE_NAME'

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'postgresql://@USERNAME:@localhost/DATABASE_NAME'

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'postgresql://@USERNAME:@localhost/DATABASE_NAME'

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,

	'default': DevelopmentConfig
}
