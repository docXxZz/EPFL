import unittest

from trees import *
from env import Env


class TestEval(unittest.TestCase):
    

    def test_literal_int(self):
        expr = Literal(42)
        env = Env()
        self.assertEqual(expr.eval(env), 42)


    def test_literal_bool(self):
        expr = Literal(True)
        env = Env()
        self.assertEqual(expr.eval(env), True)


    def test_variable(self):
        expr = Variable("x")
        env = Env()
        env.declare("x")
        env.update("x", 1337)
        self.assertEqual(expr.eval(env), 1337)

    
    def test_assignment(self):
        expr = Assignment("x", Literal(71370537))
        env = Env()
        env.declare("x")
        self.assertEqual(expr.eval(env), 71370537)
        self.assertEqual(env.get("x"), 71370537)
    

    def test_primitive(self):
        expr = Primitive("PLUS")
        env = Env()
        fun = expr.eval(env)
        self.assertEqual(fun(34, 85), 34 + 85)

    
    def test_block_base(self):
        expr = Block([
            Declaration("x", None),
            Declaration("y", None)
        ], [
            Assignment("x", Literal(42)),
            Assignment("y", Literal(17)),
            Variable("x")
        ])

        env = Env()
        self.assertEqual(expr.eval(env), 42)


    def test_block_extend(self):
        expr = Block([
            Declaration("x", None),
            Declaration("y", None)
        ], [
            Assignment("x", Literal(42)),
            Assignment("y", Literal(17)),
            Variable("z")
        ])

        env = Env()
        env.declare("z")
        env.update("z", 1337)
        self.assertEqual(expr.eval(env), 1337)

    
    def test_block_shadow(self):
        expr = Block([
            Declaration("x", None),
            Declaration("y", None)
        ], [
            Assignment("x", Literal(42)),
            Assignment("y", Literal(17)),
            Variable("y")
        ])

        env = Env()
        env.declare("y")
        env.update("y", 1337)
        self.assertEqual(expr.eval(env), 17)

    
    def test_if_true(self):
        expr = IfThenElse(Literal(True), Literal(42), Literal(17))
        env = Env()
        self.assertEqual(expr.eval(env), 42)

    
    def test_if_false(self):
        expr = IfThenElse(Literal(False), Literal(42), Literal(17))
        env = Env()
        self.assertEqual(expr.eval(env), 17)


    def test_while(self):
        expr = While(Literal(False), Literal(42))
        env = Env()
        self.assertEqual(expr.eval(env), None)


    def test_abstraction(self):
        expr = Abstraction([Declaration("x", None), Declaration("y", None)], Variable("y"))
        env = Env()
        fun = expr.eval(env)
        self.assertEqual(fun(32, 17), 17)

    
    def test_application(self):
        expr = Application(Primitive("PLUS"), [Literal(42), Literal(17)])
        env = Env()
        self.assertEqual(expr.eval(env), 42 + 17)


if __name__ == "__main__":
    unittest.main()