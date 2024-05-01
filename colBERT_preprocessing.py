from icecream import ic
import json
import tools

docs = tools.get_docs()
queries = tools.get_queries()

ColBERTqueries = {}
for i, query in enumerate(queries):
    ColBERTqueries[str(i)] = query.strip().upper()

colBERTdocs = {}
for i, doc in enumerate(docs):
    colBERTdocs[doc[0]] = doc[1]


with open("colBERT_input/colBERT_docs", "w") as filename:
    json.dump(colBERTdocs, filename)
    filename.close()

with open("colBERT_input/colBERT_queries", "w") as filename:
    json.dump(ColBERTqueries, filename)
    filename.close()