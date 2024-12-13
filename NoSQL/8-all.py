#!/usr/bin/env python3
"""function that lists all documents in a collection"""


def list_all(mongo_collection):
    """list and return all documents in a collection"""
    return list(mongo_collection.find())
