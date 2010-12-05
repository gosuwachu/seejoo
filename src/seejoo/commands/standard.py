'''
Created on 2010-12-05

@author: xion

Standard useful commands, such as evaluation of expressions.
'''
from seejoo.ext import command
import math


@command('c') 
def evaluate_expression(exp):
    '''
    Evaluates given expression.
    '''
    if not exp: res = None
    else:
        exp = str(exp)
        if len(exp) == 0:   res = None
        else:
            
            # Construct a (relatively) safe dictionary of globals
            # to be used by evaluated expressions
            def _import(name, globals={}, locals={}, from_list=[], level=-1):
                raise ImportError
            g = math.__dict__
            g['__builtins__'] = __builtins__
            g['__builtins__']['__import__'] = _import
            
            # Evaluate expression
            try:                res = eval(exp, g)
            except SyntaxError: return "Syntax error."
            except ImportError: return "Sorry, only math allowed."
        
    return "= " + str(res)