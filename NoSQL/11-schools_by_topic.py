#!/usr/bin/env python3
"""function that returns the list of school having a given topic"""


def schools_by_topic(mongo_collection, topic):
    """return the list of schools with a specific topic"""
    done = mongo_collection.find({"topics": topic})
    return done
