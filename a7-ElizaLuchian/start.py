from src.repository import Repository, TextFileRepository, BinaryRepository, MemoryRepository, JsonRepository
from src.services import Services
from src.ui import Ui
from jproperties import Properties


def start():

    config = Properties()

    with open("settings.properties", "rb") as config_file:
        config.load(config_file)

    _repo = Repository()

    if config.get("repo_type").data == "memory":
        _repo = MemoryRepository()

    elif config.get("repo_type").data == "textfile":
        _repo = TextFileRepository(config.get("text_file_name").data)


    elif config.get("repo_type").data == "binary":
        _repo = BinaryRepository(config.get("binary_name").data)

    elif config.get("repo_type").data == "json":
        _repo = JsonRepository(config.get("json_name").data)

    _services = Services(_repo)
    _ui = Ui(_services)
    _ui.start()


start()