from hendrix.deploy import HendrixDeploy
from example_app.wsgi import application as WSGIApp

deploy = HendrixDeploy('start', {'settings': 'settings', 'loud': True})
deploy.run()