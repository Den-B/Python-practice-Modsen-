from source.database.mongoDatabase import MongoDatabase
from ast import literal_eval

def currectionFunction(document):
    document["rubrics"] = literal_eval(document["rubrics"])
    return document

database = MongoDatabase("mongodb://127.0.0.1:27066","Modsen")
database.readCsvFile("./data/posts.csv", "Documents",currectionFunction)
