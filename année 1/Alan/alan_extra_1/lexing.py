import re

from tokens import *

# List of patterns and constructors.
#
# The constructor should be callable.
# Its number of parameters must match that of the number of groups
# in the pattern.
# The value captured by each group is used as an argument.
TOKENS = [(re.compile(pat), cons) for pat, cons in [
    (r'', NoneLiteral),  # À compléter
    (r'', BoolLiteral),  # À compléter
    (r'', IntLiteral),  # À compléter
    (r'', StrLiteral),  # À compléter
    (r'\(', OpenParenthesis),
    (r'\)', CloseParenthesis),
    (r'\{', OpenBrace),
    (r'\}', CloseBrace),
    (r':', ColonSymbol),
    (r';', SemicolonSymbol),
    (r',', CommaSymbol),
    (r'\.', DotSymbol),
    (r'=', EqualSymbol),
    (r'if', IfKeyword),
    (r'else', ElseKeyword),
    (r'while', WhileKeyword),
    (r'let', LetKeyword),
    (r'def', DefKeyword),
    (r'fun', FunKeyword),
    (r'and', AndOperator),
    (r'or', OrOperator),
    (r'not', NotOperator),
    (r'(==|!=|<=|>=|<|>)', ComparisonOperator),
    (r'(\+|-)', AdditiveOperator),
    (r'(\*|/|%)', MultiplicativeOperator),
    (r'', Identifier),  # À compléter
    (r'\s+', None),
]]

def lex(text):

    current_pos = 0
    line = 1
    col = 1

    len_text = len(text)

    while current_pos < len_text:

        # Find the longest matching token
        # at the current position
        best_cons = None
        best_match = None
        for regex, cons in TOKENS:
            match = regex.match(text, current_pos)
            if match is None or match.end() == current_pos:
                continue

            if best_match is None or match.end() > best_match.end():
                best_cons = cons
                best_match = match
        
        # If no token matched, raise an error
        if best_match is None:
            raise ValueError(f"Invalid token at position {current_pos}")
        
        # Create the token and yield it
        if best_cons is not None:
            token = best_cons(*best_match.groups())
            token.setPos(current_pos, line, col)
            yield token

        # Update the position
        current_pos = best_match.end()
        matched_text = best_match.group(0)
        matched_lines = matched_text.split("\n")
        line += len(matched_lines) - 1
        if len(matched_lines) > 1:
            col = len(matched_lines[-1]) + 1
        else:
            col += len(matched_text)
        

if __name__ == "__main__":
    
    print("Laissez un espace vide pour terminer.")
    while True:
        try:
            text = input("Entrez du texte: ")
            if not text:
                break
            tokens = list(lex(text))
            print("Tokens:")
            for token in tokens:
                print(token)
        except EOFError:
            break
        except ValueError as e:
            print(e)



