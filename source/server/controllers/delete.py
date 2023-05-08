from source.database.index import connectToDataBase
from source.elasticSearch.index import connectToES
import json

def deleterRecord(id):
    connection = connectToDataBase()
    elasticeSearch = connectToES()
    record = connection.findOneById("Documents", id)
    record["_id"]=id
    connection.deleteRecord("Documents", id)
    elasticeSearch.delete("posts", id)
    return json.dumps({ "deletedRecord": record})
