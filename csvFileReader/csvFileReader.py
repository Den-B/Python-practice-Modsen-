import csv
from os import path

class CsvFileReader:

    def __init__(self, fileName):
        self.filName = path.abspath(fileName)

    def readAll(self):
        result = {}
        result['rows'] = []
        file = open(self.filName, encoding='utf-8')
        fileReader = csv.reader(file, delimiter = ",")
        for row in fileReader:
            if "headers" not in result:
                result["headers"] = row
            else:
                result['rows'].append(row)
        return result

    
