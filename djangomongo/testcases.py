import mongoengine
from django.test import TestCase
from django.conf import settings


class MongoTestCase(TestCase):
    """
        TestCase class that clear the collection between the tests
    """
    def setUp(self):
        mongoengine.connection.disconnect()
        mongoengine.connect(
            host=settings.MONGO['host'],
            port=settings.MONGO['port'],
            db=settings.MONGO['db'],
            username=settings.MONGO['username'],
            password=settings.MONGO['password']
            )
        super().setUpClass()

    def tearDown(self):
        from mongoengine.connection import get_connection, disconnect
        connection = get_connection()
        connection.drop_database(settings.MONGO['db'])
        disconnect()
        super().tearDownClass()
