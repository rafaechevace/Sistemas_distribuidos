
class StringSet(set):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def add(self, item):
        if not isinstance(item, str):
            raise ValueError(item)
        super().add(item)