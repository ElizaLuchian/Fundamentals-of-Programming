from src.domain.client import *
from src.repository.clientrepo import *

class ClientService:
    def __init__(self, client_repo: ClientRepo):
        self.__repo = client_repo
       # self.get_all_generated_clients()



    def add_client(self, client):
        self.__repo.add_client(client)

    def get_all_clients(self):
        return self.__repo.get_all_clients()

    def remove(self, client_id:int):
        self.__repo.remove(client_id)

    def update(self, cl_id: int, new_name):
        self.__repo.update(cl_id, new_name)

    def search(self, search_string: str):
        return self.__repo.search(search_string)

    def get_client_by_id(self, id: int):
        return self.__repo.get_client_by_id(id)

    def get_all_generated_clients(self):
        list_of_clients=Client.generate_n_clients(20)
        for client in list_of_clients:
            self.add_client(client)
        return list_of_clients

