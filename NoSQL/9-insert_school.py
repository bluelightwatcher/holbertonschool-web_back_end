#!/usr/bin/env python3
"""function that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """inserts new document and return new id"""
    done = mongo_collection.insert_one(kwargs)
    return done.inserted_id
