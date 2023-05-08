from source.database.index import connectToDataBase

def searchRecords(id):
    connection = connectToDataBase()
    record = connection.findById()