from datetime import datetime

class JournalEntry:
    def __init__(self, title ,content):
        self.title =title
        self.content = content
        self.created_at =datetime.now().strftime("%Y-%m-%d %H %M")
    
    def to_dict(self):
        return {
            "title":self.title,
            "content":self.content,
            "created_at":self.created_at
        }
    