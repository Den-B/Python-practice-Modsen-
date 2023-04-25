from mongoDatabase import MongoDatabase

database = MongoDatabase("mongodb://127.0.0.1:27066","Modsen")
database.readCsvFile("../data/posts.csv", "Documents")

        





