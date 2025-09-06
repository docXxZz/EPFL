
from primitives import PRIM_VALS


class Declaration:
    """Represents a variable declaration.
    
    The declaration associates a name with a type."""
    
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Expression:
    """Represents an expression in the language."""

    def eval(self, env):
        raise NotImplementedError("eval method not implemented")



class Literal(Expression):
    """Represents a literal value, such as an integer, string, or boolean."""
    
    def __init__(self, value):
        self.value = value


class Variable(Expression):
    """Represents a variable reference."""
    
    def __init__(self, name):
        self.name = name


class Assignment(Expression):
    """Represents an assignment of a value to a variable."""
    
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr


class Primitive(Expression):
    """Represents a primitive value, such as a function or a constant."""
    
    def __init__(self, name):
        self.name = name


class Block(Expression):
    """Represents a block of declarations and expressions.
    
    The environment is extended with each declaration, and then the
    expressions are evaluated in the extended environment.
    
    The value of the block is the value of the last expression."""
    
    def __init__(self, decls, exprs):
        self.decls = decls
        self.exprs = exprs


class IfThenElse(Expression):
    """Represents an if-then-else expression.
    
    The condition is evaluated first. If it is true, then the 'then'
    expression is evaluated. Otherwise, the 'els' expression is evaluated."""
    
    def __init__(self, cond, then, els):
        self.cond = cond
        self.then = then
        self.els = els


class While(Expression):
    """Represents a while loop.

    The condition is evaluated first. If it is true, then the body
    expression is evaluated and the loop repeats. Otherwise, the loop
    terminates."""
    
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body


class Abstraction(Expression):
    """Represents a function abstraction.

    When evaluated, an abstraction returns a function that captures the
    environment in which it was defined. The function takes arguments
    and evaluates the body expression in an environment that extends the
    captured environment with the arguments."""

    def __init__(self, params, body):
        self.params = params
        self.body = body

    def eval(self, env):
        def fun(*args):
            new_env = env.extend()
            for param, arg in zip(self.params, args):
                new_env.declare(param.name)
                new_env.update(param.name, arg)
            return self.body.eval(new_env)
        return fun


class Application(Expression):
    """Represents a function application.

    When evaluated, the function expression is evaluated to a function,
    and the argument expressions are evaluated. The function is then
    applied to the arguments."""

    def __init__(self, fun, args):
        self.fun = fun
        self.args = args





