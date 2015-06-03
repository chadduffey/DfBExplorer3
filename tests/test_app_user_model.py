#DfB Explorer User Model Tests

import unittest
import time
from datetime import datetime
from app import create_app, db
from app.models import User, AnonymousUser, Role, Permission, Follow


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('test123')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        u = User(password='password')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='password')
        with self.assertRaises(AttributeError):
            u.password

    def test_valid_confirmation_token(self):
        u = User(password='password')
        db.session.add(u)
        db.session.commit()
        token = u.generate_confirmation_token()
        self.assertTrue(u.confirm(token))

    def test_password_verification(self):
        u = User(password='password')
        self.assertTrue(u.verify_password('password'))
        self.assertFalse(u.verify_password('something'))

    def test_password_salts_are_random(self):
        u = User(password='password')
        u2 = User(password='password')
        self.assertTrue(u.password_hash != u2.password_hash)

    def test_invalid_confirmation_token(self):
        u1 = User(password='password')
        u2 = User(password='something')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        token = u1.generate_confirmation_token()
        self.assertFalse(u2.confirm(token))

    def test_valid_reset_token(self):
        u = User(password='password')
        db.session.add(u)
        db.session.commit()
        token = u.generate_reset_token()
        self.assertTrue(u.reset_password(token, 'newpass'))
        self.assertTrue(u.verify_password('newpass'))

    def test_valid_email_change_token(self):
        u = User(email='jessica@weston.com', password='password')
        db.session.add(u)
        db.session.commit()
        token = u.generate_email_change_token('chad@test.com')
        self.assertTrue(u.change_email(token))
        self.assertTrue(u.email == 'chad@test.com')

