#DfB Explorer Testing of a client sending requests to the server

import re
import unittest
from flask import url_for
from app import create_app, db
from app.models import User, Role

class FlaskClientTestCase(unittest.TestCase):

def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)

    def test_register_and_login(self):
        # register a new account
        response = self.client.post(url_for('auth.register'), data={
                                'email': 'chad@notarealdomain.com',
                                'username': 'chad',
                                'password': 'pass',
                                'password2': 'pass'
                                })
        self.assertTrue(response.status_code == 302)


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


        # login with the new account
        response = self.client.post(url_for('auth.login'), data={
            'email': 'jessica@weston.com',
            'password': 'harry'
        }, follow_redirects=True)
        self.assertTrue(re.search(b'Hello,\s+jessica!', response.data))
        self.assertTrue(
            b'You have not confirmed your account yet' in response.data)

        # send a confirmation token
        user = User.query.filter_by(email='jessica.weston@gmail.com').first()
        token = user.generate_confirmation_token()
        response = self.client.get(url_for('auth.confirm', token=token),
                                   follow_redirects=True)
        self.assertTrue(
            b'You have confirmed your account' in response.data)

        # log out
        response = self.client.get(url_for('auth.logout'), follow_redirects=True)
        self.assertTrue(b'You have been logged out' in response.data)
