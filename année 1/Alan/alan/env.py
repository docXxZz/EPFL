
class Env:
    """Environment class for storing variables and their values.
    
    An environment is a dictionary that maps variable names to values.
    Each environment has a reference to an outer environment, which is
    used to look up variables that are not declared in the current environment."""

    def __init__(self):
        self.env_dict = {}
        self.outer = None
    
    def declare(self, key):
        """Declare a new variable in the environment."""

        self.env_dict[key] = None

    def find(self, key):
        """Find the environment where a variable is declared."""

        if key in self.env_dict:
            return self
        elif self.outer is not None:
            return self.outer.find(key)
        else:
            return None

    def get(self, key):
        """Get the value of a variable from the environment."""

        env = self.find(key)
        return env.env_dict[key]
        
    def update(self, key, value):
        """Update the value of a variable in the environment."""

        env = self.find(key)
        env.env_dict[key] = value

    def extend(self):
        """Create a new environment that extends the current environment."""
        
        env = Env()
        env.outer = self
        return env