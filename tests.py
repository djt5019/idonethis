import os
import unittest

import betamax
import idoneit
import requests

try:
    from unittest import mock
    from io import StringIO
except ImportError:
    import mock
    from cStringIO import StringIO


# No requests should come from Travis
RECORD_MODE = 'never' if os.environ.get('TRAVIS_GH3') else 'once'
AUTH_TOKEN = 'Token ' + os.environ.get('IDONEIT_TOKEN', 'x' * 20)


class TestSubmitDone(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.session = requests.Session()
        cls.session.headers = {'Authorization': AUTH_TOKEN}
        cls.vcr = betamax.Betamax(cls.session)

        with betamax.Betamax.configure() as config:
            config.cassette_library_dir = 'fixtures'
            config.default_cassette_options['record_mode'] = RECORD_MODE
            config.define_cassette_placeholder('Token <AUTH_TOKEN>', AUTH_TOKEN)

    def test_invalid_auth_token(self):
        self.session.headers['Authorization'] = 'Token hunter2'

        with self.assertRaises(ValueError):
            with self.vcr.use_cassette('bad_auth_token'):
                idoneit.submit_done(self.session, 'team', 'done')

        self.session.headers['Authorization'] = AUTH_TOKEN

    def test_using_the_wrong_team(self):
        with self.assertRaises(ValueError):
            with self.vcr.use_cassette('bad_team'):
                idoneit.submit_done(self.session, 'team', 'done')

    def test_a_good_request(self):
        with self.vcr.use_cassette('good_post_request'):
            idoneit.submit_done(self.session, 'aweber-be-bof', 'I did it!')


class TestGrabText(unittest.TestCase):

    @mock.patch('sys.stdin')
    def test_stdin_available(self, stdin):
        stdin.isatty.return_value = False
        stdin.read.return_value = 'testing'
        self.assertEqual('testing', idoneit.get_done_text())

    @mock.patch('idoneit.subprocess.call')
    def test_bringing_up_an_editor(self, subprocess_call):
        self.assertEqual('Today I did...', idoneit.get_done_text())
