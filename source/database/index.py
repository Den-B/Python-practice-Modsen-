from source.database.mongoDatabase import MongoDatabase
from ast import literal_eval
from constants import mongoCollection
from constants import mongoDatabase
from constants import mongoUrl

def connectToDataBase():
    database = MongoDatabase(mongoUrl,mongoDatabase)
    return database
    
def writeRecordsFromCsvFile():

    def currectionFunction(document):
        document["rubrics"] = literal_eval(document["rubrics"])
        return document

    database = connectToDataBase()
    database.readCsvFile("../data/posts.csv", mongoCollection,currectionFunction)


        





