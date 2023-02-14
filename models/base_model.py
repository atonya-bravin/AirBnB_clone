#!/usr/bin/python3

import uuid
import datetime

time_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        time_dict = self.__dict__.copy()
        time_dict["__class__"] = self.__class__.__name__
        if "created_at" in time_dict:
            time_dict["created_at"] = time_dict["created_at"].strftime(time_format)
        if "updated_at" in time_dict:
            time_dict["updated_at"] = time_dict["updated_at"].strftime(time_format)
        return (time_dict)
