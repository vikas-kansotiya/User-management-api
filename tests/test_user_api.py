import unittest
import json
from tests.base import BaseTestCase
from app import db, User


class TestUserAPI(BaseTestCase):
    def test_create_user(self):
        response = self.client.post(
            "/api/user",
            data=json.dumps(
                {
                    "first_name": "Vikas",
                    "last_name": "Kansotiya",
                    "email": "vikaskansotiyasujangarh@gmail.com",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("Users created successfully", response.get_json()["message"])

    def test_get_users(self):
        with self.app.app_context():
            user = User(
                first_name="Vikas", 
                last_name="Kansotiya", 
                email="vikaskansotiyasujangarh@gmail.com"
            )
            db.session.add(user)
            db.session.commit()

        response = self.client.get("/api/users")
        self.assertEqual(response.status_code, 200)
        users = response.get_json()["users"]

        # Check if the user's data is in the response
        self.assertTrue(any(u["first_name"] == "Vikas" and u["last_name"] == "Kansotiya" for u in users))


if __name__ == "__main__":
    unittest.main()
