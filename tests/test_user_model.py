import unittest
from app import db, User
from tests.base import BaseTestCase


class TestUserModel(BaseTestCase):
    def test_create_user(self):
        with self.app.app_context():
            user = User(
                first_name="John", last_name="Doe", email="john.doe@example.com"
            )
            db.session.add(user)
            db.session.commit()
            self.assertEqual(user.id, 1)
            self.assertEqual(user.first_name, "John")
            self.assertEqual(user.last_name, "Doe")
            self.assertEqual(user.email, "john.doe@example.com")


if __name__ == "__main__":
    unittest.main()
