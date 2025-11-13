from typing import Union

from gym.project import Category
from gym.project import Topic
from gym.project import Document


class Storage:

    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        self.__edit_object__(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.__edit_object__(topic_id, self.topics, new_topic ,new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        self.__edit_object__(document_id, self.documents, new_file_name)

    def delete_category(self, category_id: int):
        self.__delete_object__(category_id, self.categories)

    def delete_topic(self, topic_id: int):
        self.__delete_object__(topic_id, self.topics)

    def delete_document(self, document_id: int):
        self.__delete_object__(document_id, self.documents)

    def get_document(self, document_id:int):
        return self.__find_object_by_id(document_id, self.documents)

    def __repr__(self):
        return '\n'.join(repr(doc) for doc in self.documents)

    def __edit_object__(self, object_id:int, collections: list[Union[Category, Topic, Document]], *new_values):
        current_object = self.__find_object_by_id(object_id, collections)
        if current_object:
            current_object.edit(*new_values)

    def __delete_object__(self, object_id: int, collections: list):
        object_to_delete = self.__find_object_by_id(object_id, collections)
        if object_to_delete:
            collections.remove(object_to_delete)

    @staticmethod
    def __find_object_by_id(object_id:int, collection: list):
        return next((obj for obj in collection if obj.id == object_id), None)

