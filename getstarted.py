import openvector

client = openvector.Client()
collection = client.create_collection('quotes')

docs = ["This is document1", "This is document2"]
collection.add(docs)

results = collection.query(["This is a query document"])
print(results.documents)
