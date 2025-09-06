class TypeError(Exception):
    def __init__(self, message):
        self.message = message

class Type:
    pass

class SimpleType(Type):
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        return isinstance(other, SimpleType) and \
               self.name == other.name

INT_TYPE = SimpleType("int")
STR_TYPE = SimpleType("str")
BOOL_TYPE = SimpleType("bool")
UNIT_TYPE = SimpleType("unit")

class FunctionType(Type):
    def __init__(self, arg_types, return_type):
        self.arg_types = arg_types
        self.return_type = return_type
    
    def __eq__(self, other):
        return isinstance(other, FunctionType) and \
               self.arg_types == other.arg_types and \
               self.return_type == other.return_type

class TypeEnv:
    def __init__(self):
        self.env = {}
        self.outer = None

    def set(self, key, value):
        self.env[key] = value

    def find(self, key):
        if key in self.env:
            return self
        elif self.outer is not None:
            return self.outer.find(key)
        else:
            return None

    def get(self, key):
        env = self.find(key)
        return env.env[key]

    def update(self, key, value):
        env = self.find(key)
        env.env[key] = value

    def extend(self):
        env = TypeEnv()
        env.outer = self
        return env