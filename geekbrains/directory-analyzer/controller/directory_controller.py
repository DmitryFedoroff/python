from model.directory_model import DirectoryModel
from view.directory_view import DirectoryView


class DirectoryController:
    def __init__(self, directory: str) -> None:
        self.model = DirectoryModel(directory)
        self.view = DirectoryView()
