# -*- coding: utf-8 -*-
version_info = (1, 0, 0)
__version__ = '.'.join(str(v) for v in version_info[:3])

import requests


ROOT_URI = 'https://idonethis.com/api/v0.1/dones/'


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
