from flask import url_for
from flask_testing import TestCase
from service2.app import weapon
from service4.app import app, effects, longswords, spears , daggers, crossbows, bows, scythes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_weapon(self):

        for i in weapon:
            for j in range(60):

                content = {'weapon':i, 'damage':j}
                response = self.client.post(url_for('post_status'), json=content)

                self.assert200(response)

                if j <= 10:
                    self.assertIn("Beginner", response.data.decode())
                elif j <= 20:
                    self.assertIn("Adept", response.data.decode())
                elif j <= 30:
                    self.assertIn("Journeyman", response.data.decode())
                elif j <= 40:
                    self.assertIn("Master", response.data.decode())
                elif j <= 50:
                    self.assertIn("Hero", response.data.decode())
                else:
                    self.assertIn("Legend", response.data.decode())