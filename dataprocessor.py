class DataProcessor:
    """Class DataProcessor"""
    def __init__(self, data=[]):
        self.data = data
        self.processed_data_ = []
    def process(self):
        """Process method"""
        if not self.data:
            return
        average = sum(self.data) / len(self.data)
        self.processed_data_ = [x - average for x in self.data]
    def save_to_file(self, filename):
        """Save to file method"""
        if not self.processed_data_:
            return
        with open(filename, 'w') as file:
            for value in self.processed_data_:
                file.write(str(value) + '\n')
                