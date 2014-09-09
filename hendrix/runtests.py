from unittest import expectedFailure
import unittest

from django.core.handlers.wsgi import WSGIHandler
import mock
from twisted.application import service

from hendrix.deploy import HendrixDeploy
from tests import wsgi

from twisted.application.service import Service

from twisted.test.proto_helpers import MemoryReactor

FAKE_RUN_MESSAGE = "Look at me! I ran!"

class FakeReactor(MemoryReactor):

    def run(self):
        return FAKE_RUN_MESSAGE

class ServiceTests(unittest.TestCase):

    options = {'http_port': 2000,
               'nocache': True,
               'fd': None}

    reactor = FakeReactor()

    def test_hendrix_service_maker_makes_hendrix_server(self):
        deploy_object = HendrixDeploy(
                                      wsgi_application=WSGIHandler(),
                                      options=self.options,
                                      reactor=self.reactor)
        result = deploy_object.run()
        self.assertEqual(result, FAKE_RUN_MESSAGE)


    def test_no_settings_and_no_wsgi_raises_error(self):
        self.assertRaises(ValueError, HendrixDeploy,
                          wsgi_application=None,
                          options=self.options,
                          reactor=self.reactor)

    '''
     Logging Tests

     The following link is a helpful blog post on examining logging buffer.
     http://plumberjack.blogspot.com/2010/09/unit-testing-and-logging.html
     '''
    @expectedFailure
    def test_no_logging_setting_causes_default_logger(self):
        options = {'port': "2000", 'settings': "test", "wsgi": WSGI_FILE}
        server = self.service_maker.makeService(options)
        self.fail()

    @expectedFailure
    def test_no_logging_setting_causes_warning(self):
       options = {'port': "2000", "settings": "i_didnt_ask_for_santana_abraxas", "wsgi": WSGI_FILE}
       #If the setting module has no LOGGING, we warn them and question of the action they are about to take.
       self.fail()

if __name__ == '__main__':
    unittest.main()
