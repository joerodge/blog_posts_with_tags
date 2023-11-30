class Post:
    def __init__(self, post_id, title, tags =[]):
        self.post_id = post_id
        self.title = title
        self.tags = tags


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Post({self.post_id}, {self.title})"
    

class Tag:
    def __init__(self, tag_id, name):
        self.tag_id = tag_id
        self.name = name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Tag({self.tag_id}, {self.name})"
