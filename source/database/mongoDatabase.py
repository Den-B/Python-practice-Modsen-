from source.csvFile.csvFileReader import CsvFileReader
from pymongo import MongoClient

class MongoDatabase:

    def __init__(self, connectionString, databaseName):
        self.connectionString = connectionString
        self.database = MongoClient(self.connectionString)[databaseName]

    def insertDocument(self, collectionName, document):
        collection = self.database[collectionName]
        collection.insert_one(document)

    def readCsvFile(self, fileName, collectionName, currectionFunction):
        collection = self.database[collectionName]
        reader = CsvFileReader(fileName)
        for document in reader.rowStreamGenerator():
            collection.insert_one(currectionFunction(document))
        

