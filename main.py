import inverted_index as ii
import vector_space_model as vsm
import preprocessing as prep
import evaluation_metrics as metrics

def main_app():
    doc_collection = prep.preprocess_collection()   # stripped_docs
    queries = prep.preprocess_queries()     # stripped_queries

    inverted_index = ii.create_inverted_index(doc_collection)
    results1, results2 = vsm.run_vsm(doc_collection, queries, inverted_index)

    metrics.run_metrics(results1, results2)


if __name__ == '__main__':
    main_app()
