import unittest

from src.domain.client import Client
from src.repository.clientrepo import ClientRepo, NotUniqueClientIdError, NotFoundError


class TestClientRepo(unittest.TestCase):

    def setUp(self):
        self.client_repo = ClientRepo()

    def test_add_client(self):
        # Test adding a new client
        client = Client(client_id=1, name="John Doe")
        self.client_repo.add_client(client)
        self.assertIn(client, self.client_repo.get_all_clients())

    def test_get_all_clients(self):
        # Test getting all clients from an empty repository
        self.assertEqual(self.client_repo.get_all_clients(), [])

        # Test getting all clients after adding some clients
        clients = [
            Client(client_id=1, name="John Doe"),
            Client(client_id=2, name="Jane Doe"),
            Client(client_id=3, name="Bob Smith")
        ]
        for client in clients:
            self.client_repo.add_client(client)
        self.assertEqual(self.client_repo.get_all_clients(), clients)

    def test_update(self):
        # Test updating the name of an existing client
        client = Client(client_id=1, name="John Doe")
        self.client_repo.add_client(client)
        new_name = "John Updated"
        self.client_repo.update(client.client_id, new_name)
        self.assertEqual(client.name, new_name)

    def test_remove(self):
        # Test removing an existing client
        client = Client(client_id=1, name="John Doe")
        self.client_repo.add_client(client)
        self.client_repo.remove(client.client_id)
        self.assertNotIn(client, self.client_repo.get_all_clients())



if __name__ == '__main__':
    unittest.main()
