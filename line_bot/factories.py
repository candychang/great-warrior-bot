from line_bot.models import *
import factory

class UserFactory(factory.Factory):
	class Meta:
		model = line_bot.UserModel
		
		username = ""