#!/usr/bin/env python3

'''
a Python function that lists all documents in a collection
'''


def list_all(mongo_collection):
    '''returns documents in a collection'''
    documents = []

    cursor = mongo_collection.find()
    for document in cursor:
        if document is None:
            return []
        else:
            documents.append(document)
            return documents
