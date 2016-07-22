import line_bot 
import factory

class UserFactory(factory.DjangoModelFactory):
	class Meta:
		model = line_bot.models.UserModel
		
	username = "shazbot"
	line_id = "00379732a4nzy543"
		
class RequestFactory(factory.DjangoModelFactory):
	class Meta:
		model = line_bot.models.Request
		
	itemrequest = 'default'
	url = 'default'
	size = 'default'
	itemcolor = 'default'
		
	user = factory.SubFactory(UserFactory)