class Topic:
    def __init__(self, t_id:int, topic:str, storage_folder:str):
        self.id = t_id
        self.topic = topic
        self.storage_folder = storage_folder

    def edit(self, new_topic:str, new_storage_folder:str):
        self.topic = new_topic
        self.storage_folder = new_storage_folder

    def __repr__(self):
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"