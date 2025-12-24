memory = {}

def save(key, value):
    memory[key] = value

def get(key):
    return memory.get(key)
