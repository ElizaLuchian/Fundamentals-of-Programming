import random


class InvalidClientIdError(Exception):
    def __init__(self, client_id):
        self.__client_id = client_id

    def __str__(self):
        return str(self.__client_id) + " is and invalid id "


class InvalidClientNameError(Exception):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name + " is an invalid name "

class Client:
    def __init__(self, client_id:int, name:str):
        if client_id<0:
            raise InvalidClientIdError(client_id)

        self.__client_id = client_id

        if name.isnumeric()==True:
            raise InvalidClientNameError(self.__name)

        self.__name = name

    @property
    def client_id(self):
        return self.__client_id

    @property
    def name(self):
        return self.__name

    @client_id.setter
    def client_id(self, new_id):
        self.__client_id=new_id
    @name.setter
    def name(self, newname):
        self.__name=newname

    def __str__(self):
        return ("client id " + str(self.__client_id) + " | name "+ str(self.__name))

    __repr__ = __str__

    @staticmethod
    def generate_clients(idd:int):
        str1 = [
            "Alice Anderson",
            "Bob Brown",
            "Charlie Clark",
            "David Davis",
            "Emma Evans",
            "Frank Fisher",
            "Grace Garcia",
            "Henry Harrison",
            "Ivy Irwin",
            "Jack Johnson",
            "Katherine Khan",
            "Leo Lopez",
            "Mia Miller",
            "Nathan Nguyen",
            "Olivia Owens",
            "Peter Patel",
            "Quinn Quinn",
            "Rachel Reyes",
            "Samuel Smith",
            "Taylor Thompson"]



        id_ = idd
        name = random.choice(str1)

        return Client(id_, name)

    @staticmethod
    def generate_n_clients(n: int):
        arr = []
        for i in range(1,n+1):
            new = Client.generate_clients(i)
            arr.append(new)
        return arr



