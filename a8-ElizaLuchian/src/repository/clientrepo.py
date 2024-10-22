import random

from src.domain.client import *
class NotUniqueClientIdError(Exception):
    def __init__(self, client_id):
        self.__client_id = client_id

    def __str__(self):
        return str(self.__client_id) + " is not an unique movie id "

class NotFoundError(Exception):
    def __init__(self, entity_id):
        self.__entity_id = entity_id
    def __str__(self):
        return str(self.__entity_id) + " this id is not found"

class ClientRepo:
    def __init__(self):
        self._clientlist=[]
    def add_client(self, client:Client):
        if self.already_exists_client(client) is False:
            raise NotUniqueClientIdError(client.client_id)
        self._clientlist.append(client)

    def get_all_clients(self):
        return self._clientlist
    def update(self, cl_id, new_name):
        found=0
        for client in self._clientlist:
            if cl_id==client.client_id:
                client.name = new_name
                found=1

        if found==0:
            raise NotFoundError(cl_id)
    def remove(self, cl_id):
        found=0
        for client in self._clientlist:
            if cl_id==client.client_id:
                found=1
                self._clientlist.remove(client)

        if found==0:
            raise NotFoundError(cl_id)

    def search(self, search_string: str):
        result = []
        search_string = search_string.lower()
        for el in self._clientlist:
            if search_string in el.name.lower() or search_string in str(el.client_id).lower():
                result.append(el)
        return result

    def get_client_by_id(self, id: int):
        found=0
        for client in self._clientlist:
            if client.client_id == id:
                found=1
                return client

        if found==0:
            raise NotFoundError(id)


    def already_exists_client(self, client: Client):


        for x in self._clientlist:

            if client.client_id == x.client_id:
                return False
        return True
