# -*- coding: utf-8 -*-
version_info = (1, 0, 0)
__version__ = '.'.join(str(v) for v in version_info[:3])

import json
import os
import subprocess
import sys
import tempfile

import argparse
import requests


ROOT_URI = 'https://idonethis.com/api/v0.1/dones/'


class DoneApi(object):
    """Wrapper around some of the functionality provided by idonethis.

    :param str token: Your authorization token for the API
    :param str team: Name of the team to the user did something on.

    """

    def __init__(self, token, team):
        self.team = team
        self.session = requests.Session()
        self.session.headers['Authorization'] = 'Token {}'.format(token)

    def submit_done(self, done):
        """Submit the users done and bask in the glory of productivity.

        :param str done: Description of what was accomplished.

        """
        post_data = {'raw_text': done, 'team': self.team}
        response = self.session.post(ROOT_URI, json=post_data)

        if response.ok:
            return

        if response.status_code not in (400, 401):
            response.raise_for_status()

        payload = response.json()

        if 'errors' in payload and 'team' in payload['errors']:
            raise ValueError("You aren't a part of the '{}' team".format(self.team))
        else:
            raise ValueError(payload['detail'])



def get_done_text():
    """Grab input from either the users editor of choice or stdin."""
    if not sys.stdin.isatty():
        return sys.stdin.read()

    EDITOR = os.environ.get('EDITOR', 'vim')

    with tempfile.NamedTemporaryFile(suffix='.tmp', delete=False) as temp:
        filename = temp.name
        temp.write(b'Today I did... ')
        temp.flush()
        subprocess.call([EDITOR, temp.name])

    with open(filename) as updated_temp:
        data = updated_temp.read()

    os.unlink(filename)
    return data


def main():
    """The main entry point for the application."""
def read_config(path):
    """Read and return the config or an empty dictionary if something breaks

    :param str pathlib.Path: The pathlib object for your config file.

    """
    try:
        with path.open() as config:
            config = json.load(config)
            return {'team': config['team'], 'token': config['token']}
    except Exception:
        return {}


def build_parser():
    """Build and return an ArgumentParser."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--message', help='Content of your done')
    parser.add_argument('--team', required=True, help='Your team')
    parser.add_argument('--token', required=True,
                        help=('Your authorization token: '
                            'see https://idonethis.com/api/token/'))
    parser.add_argument('-c', '--config', help=(
        'Config file to load, default is your home directory'))
    parser.add_argument('--team', help='Your team')
    parser.add_argument('--token', help=(
        'Your authorization token: see https://idonethis.com/api/token/'))
    return parser


def read_cli(parser):
    """Read the CLI arguments from the parser and return a dictionary."""
    args = parser.parse_args()
    token = args.token
    team = args.team
    done_text = args.message

    done = DoneApi(token, team)
    config_path = args.config
    if not config_path:
        home_dir = os.path.expanduser('~')
        config_path = os.path.join(home_dir, '.idonethis.json')

    return {'team': args.team, 'token': args.token,
            'config': config_path, 'message': args.message}


    if not done_text:
        done_text = get_done_text()

    try:
        done.submit_done(done_text)
    except Exception as exception:
        sys.exit("Failed to record what you've done: {}".format(exception))

    print("Recorded what you've done, keep up the good work!")


if __name__ == '__main__':  # pragma: nocover
    main()
