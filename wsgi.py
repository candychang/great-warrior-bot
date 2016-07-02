import os, sys    
sys.path.append(' /dev/great_warrior_bot/great_warrior_bot')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "great_warrior_bot.settings.default")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
