from trees import *
from env import Env

if __name__ == "__main__":
    expr = Application(Primitive("PLUS"), [Literal(1), Literal(1)])
    env = Env()
    print(expr.eval(env))