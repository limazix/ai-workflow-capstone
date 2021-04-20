# -*- coding: utf-8 -*-

from unittest import TestCase
from starlette.testclient import TestClient

from app.main import app


class TestAppMain(TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_ping(self):
        """
        it should answer pong
        """
        response = self.client.get("/ping")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"ping": "pong"})
