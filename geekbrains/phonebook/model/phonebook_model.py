from utils import file_handler


class PhonebookModel:
    def __init__(self):
        self.data = []

    def add_contact(self, contact):
        self.data.append(contact)

    def get_all_contacts(self):
        return self.data

    def load_data(self, file_name, format_type):
        try:
            if format_type == 'CSV':
                self.data = file_handler.read_csv(file_name)
            elif format_type == 'JSON':
                self.data = file_handler.read_json(file_name)
            return True, "Data imported successfully"
        except Exception as e:
            return False, f"Error occurred while loading data: {e}"

    def save_data(self, file_name, format_type):
        try:
            if format_type == 'CSV':
                file_handler.write_csv(self.data, file_name)
            elif format_type == 'JSON':
                file_handler.write_json(self.data, file_name)
            return True, "Data exported successfully"
        except Exception as e:
            return False, f"Error occurred while saving data: {e}"
