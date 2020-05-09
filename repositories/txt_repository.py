class TxtRepository:
    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as reader:
            return reader.read().splitlines()
