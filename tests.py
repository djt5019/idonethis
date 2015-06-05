import os
import unittest

import betamax
import idonethis
import requests

try:
    from unittest import mock
except ImportError:
    import mock


# No requests should come from Travis
RECORD_MODE = 'never' if bool(os.environ.get('TRAVIS')) else 'once'
AUTH_TOKEN = 'Token ' + os.environ.get('IDONETHIS_TOKEN', 'x' * 20)


class BetamaxMixn(object):

    @classmethod
    def setUpClass(cls):
        super(BetamaxMixn, cls).setUpClass()
        cls.session = requests.Session()
        cls.session.headers = {'Authorization': AUTH_TOKEN}
        cls.vcr = betamax.Betamax(cls.session)

        with betamax.Betamax.configure() as config:
            config.cassette_library_dir = 'fixtures'
            config.default_cassette_options['record_mode'] = RECORD_MODE
            config.define_cassette_placeholder('Token <AUTH_TOKEN>',
                                               AUTH_TOKEN)


class TestSubmitDone(BetamaxMixn, unittest.TestCase):

    def test_invalid_auth_token(self):
        self.session.headers['Authorization'] = 'Token hunter2'

        with self.assertRaises(ValueError):
            with self.vcr.use_cassette('bad_auth_token'):
                idonethis.submit_done(self.session, 'team', 'done')

        self.session.headers['Authorization'] = AUTH_TOKEN

    def test_using_the_wrong_team(self):
        with self.assertRaises(ValueError):
            with self.vcr.use_cassette('bad_team'):
                idonethis.submit_done(self.session, 'team', 'done')

    def test_a_good_request(self):
        with self.vcr.use_cassette('good_post_request'):
            idonethis.submit_done(self.session, 'aweber-be-bof', 'I did it!')


class TestGrabText(unittest.TestCase):

    @mock.patch('sys.stdin')
    def test_stdin_available(self, stdin):
        stdin.isatty.return_value = False
        stdin.read.return_value = 'testing'
        self.assertEqual('testing', idonethis.get_done_text())

    @mock.patch('idonethis.subprocess.call')
    def test_bringing_up_an_editor(self, subprocess_call):
        self.assertEqual('Today I did... ', idonethis.get_done_text())


class TestMainFunction(BetamaxMixn, unittest.TestCase):

    @mock.patch('sys.exit')
    @mock.patch('sys.stdin')
    @mock.patch('idonethis.parser')
    @mock.patch('idonethis.requests')
    def test_no_done_text_provided_in_cli(self, requests, parser, stdin, exit_):
        requests.Session.return_value = self.session
        parser.parse_args.return_value = mock.Mock(
            message=None,
            team='aweber-be-bof',
            token=os.environ.get('IDONETHIS_TOKEN', 'x' * 20))

        stdin.isatty.return_value = False
        stdin.read.return_value = 'testing'

        with self.vcr.use_cassette('good_post_request'):
            idonethis.main()

        self.assertFalse(exit_.called)

    @mock.patch('idonethis.requests')
    @mock.patch('idonethis.parser')
    @mock.patch('idonethis.get_done_text')
    def test_done_text_provided_in_cli(self, get_done_text, parser, requests):
        requests.Session.return_value = self.session
        parser.parse_args.return_value = mock.Mock(
            message='I did it!',
            team='aweber-be-bof',
            token=os.environ.get('IDONETHIS_TOKEN', 'x' * 20))

        with self.vcr.use_cassette('good_post_request'):
            idonethis.main()

        self.assertFalse(get_done_text.called)

    @mock.patch('sys.exit')
    @mock.patch('idonethis.parser')
    @mock.patch('idonethis.requests')
    def test_unhandled_exception_occurs(self, requests, parser, exit_):
        requests.Session.return_value = self.session
        parser.parse_args.return_value = mock.Mock()

        with self.vcr.use_cassette('good_post_request'):
            idonethis.main()

        self.assertTrue(exit_.called)
