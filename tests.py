import os
import unittest

import betamax
import idoneit
import requests


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
