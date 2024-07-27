import unittest
from app import db, User
from tests.base import BaseTestCase


class TestUserModel(BaseTestCase):
    def test_create_user(self):
        with self.app.app_context():
            user = User(
                first_name="Vikas", last_name="Kansotiya", email="vikaskansotiyasujangarh@gmail.com"
            )
            db.session.add(user)
            db.session.commit()
            self.assertEqual(user.id, 1)
            self.assertEqual(user.first_name, "Vikas")
            self.assertEqual(user.last_name, "Kansotiya")
            self.assertEqual(user.email, "vikaskansotiyasujangarh@gmail.com")


if __name__ == "__main__":
    unittest.main()
