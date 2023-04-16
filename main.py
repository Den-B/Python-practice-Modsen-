from csvFileReader.csvFileReader import CsvFileReader

reader = CsvFileReader("./data/posts.csv")
result = reader.readAll()
print(result['headers'])
print(result['rows'][0])