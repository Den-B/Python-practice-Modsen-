from source.database.mongoDatabase import MongoDatabase
from ast import literal_eval


def connectToDataBase():
    database = MongoDatabase("mongodb://127.0.0.1:27066","Modsen")
    return database
    
def writeRecordsFromCsvFile():

    def currectionFunction(document):
        document["rubrics"] = literal_eval(document["rubrics"])
        return document

    database = connectToDataBase()
    database.readCsvFile("../data/posts.csv", "Documents",currectionFunction)


        





