from trees import Expression, Declaration
from typechecking import Type

def show_tree(tree):
    class_name = tree.__class__.__name__

    def go(attr):
        if isinstance(attr, Expression):
            return show_tree(attr)
        elif isinstance(attr, Type):
            return show_tree(attr)
        elif isinstance(attr, Declaration):
            return show_tree(attr)
        elif isinstance(attr, list):
            return "[" + ", ".join(go(x) for x in attr) + "]"
        return repr(attr)
    
    attrs = [f"{attr}={go(getattr(tree, attr))}" for attr in dir(tree) if
                 not attr.startswith('_') and
                 not callable(getattr(tree, attr))]
    
    return f"<{class_name}" + "(" + ", ".join(attrs) + ")>"


    