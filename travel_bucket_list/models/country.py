class Country:

    def __init__(self, name, visited = False, id = None):
        self.name = name
        self.visited = visited
        self.id = id

    def mark_as_visited(self):
        self.has_visited = True

