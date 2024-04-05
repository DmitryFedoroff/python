from model.directory_model import DirectoryModel
from view.directory_view import DirectoryView


class DirectoryController:
    def __init__(self, directory: str) -> None:
        self.model = DirectoryModel(directory)
        self.view = DirectoryView()

    def analyze_and_save(self, output_dir: str) -> None:
        data = self.model.analyze_directory()
        self._write_to_json(data, output_dir, 'directory_analysis')
        self._write_to_csv(data, output_dir, 'directory_analysis')
        self._write_to_pickle(data, output_dir, 'directory_analysis')
        self.view.display_message("Analysis completed and data saved.")
