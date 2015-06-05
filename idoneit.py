# -*- coding: utf-8 -*-
version_info = (1, 0, 0)
__version__ = '.'.join(str(v) for v in version_info[:3])

import os
import subprocess
import sys
import tempfile

import requests


ROOT_URI = 'https://idonethis.com/api/v0.1/dones/'


def get_done_text():
    """Grab input from either the users editor of choice or stdin."""
    if not sys.stdin.isatty():
        return sys.stdin.read()

    EDITOR = os.environ.get('EDITOR', 'vim')

    with tempfile.NamedTemporaryFile(suffix='.tmp', delete=False) as temp:
        filename = temp.name
        temp.write('Today I did... ')
        temp.flush()
        subprocess.call([EDITOR, temp.name])

    with open(filename) as updated_temp:
        data = updated_temp.read()

    temp.unlink(filename)
    return data


def submit_done(session, team, done):
    """Submit the users done and bask in the glory of productivity.

    :param Session session: A `requests_` session object.
    :param str team: Name of the team to the user did something on.
    :param str done: Description of what was accomplished.

    """
    post_data = {'raw_text': done, 'team': team}
    response = session.post(ROOT_URI, json=post_data)

    if response.ok:
        return

    if response.status_code not in (400, 401):
        response.raise_for_status()

    payload = response.json()

    if 'errors' in payload and 'team' in payload['errors']:
        raise ValueError("You aren't a part of the '{}' team".format(team))
    else:
        raise ValueError(payload['detail'])
