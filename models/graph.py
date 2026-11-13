class Graph:
    def __init__(self):
        self.links = {}

    def add_link(self, source_id, destination_id):
        if self.links.get(source_id) == None:
            self.links[source_id] = []
        self.links[source_id].append(destination_id)

    def remove_link(self, source_id, destination_id):
        if self.links.get(source_id) != None:
            self.links[source_id].remove(destination_id)
        else:
            raise Exception("Source ID does not exist: {source_id}") 

        self.links.get(source_id).remove(destination_id)

        def print_links(self):
            for source_id, destination_ids in self.links.items():
                print(f"{source_id} -> {destination_ids}")
