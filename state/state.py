from typing import Any

class State:
    '''
    hold the history of the conversation
    '''
    def __init__(self):
        self.messages = []
        self.state = {}
        self.state['messages'] = self.messages
    
    def get(self, key: str, default: Any = None) -> Any:
        return self.state.get(key, default)
