# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:54:07 2022

@author: Nataša
"""

import lark
from lark import Lark, Transformer

grammar = """
    ?start: switch_stmt
    switch_stmt: "switch" "(" variable ")" "{" case+ default "}"
    case: "case" value ":" "z" "=" cost ";" "break" ";"
    default: "default" ":" "z" "=" cost ";" "break" ";"
    variable: VAR
    cost: INT
    value: INT
    VAR: /x|y/
    
    %import common.INT
    %import common.WS
    %ignore WS
"""

parser = Lark(grammar)

input_str = """

switch(x){
    case 0: z = 5;
        break;
    case 1: z = 3;
        break;
    case 2: z = 8;
        break;
    case 3: z = 17;
        break;
    default: z = 1;
        break;
    }
"""

switch_parser = lark.Lark(grammar, start="switch_stmt")
result = switch_parser.parse(input_str)
#print("\n*** Parse tree ***\n",result)
print("\n*** Parse tree pretty print ***\n", result.pretty())


x = 3
#y = 0

class switchTransformer(Transformer):
    
    # go through all cases and find the same case_value as my_case_value
    # then get the cost... if nothing matches give default cost as result
          
    
    def switch_stmt(self, items):
        var = items[0]
        cases = items[1:-1]
        default = items[-1]
        result = None
        
        switch_var = var.value
        if switch_var == "x":
            try: 
                my_case_value = x
                print('x = {}'.format(my_case_value))
            except: 
                my_case_value = 0
                print('Variable not declared so using initialized x = {}'.format(my_case_value))
        if switch_var == "y":
            try: 
                my_case_value = y
                print('y = {}'.format(my_case_value))
            except: 
                my_case_value = 0
                print('Variable not declared so using initialized y = {}'.format(my_case_value))
        
        for case in cases:
            if int(case[0]) == int(my_case_value):
                result = case[1]
                print("z = {}".format(result))
        
        if result is None and default is not None:
            result = default[0]
            print("There is no case for {} = {}, therefore by default z = {}".format(switch_var ,my_case_value, result))
        #return result
    
    
    def case(self,items):
        value, cost = items        
        return value,cost

    def default(self,items):
        cost = items[0]  
        return cost
     
    def variable(self,items):
        return items[0]
            
    def value(self,items):
        return items[0]
    
    def cost(self, items):
        return items[0]
                 

switchTransformer().transform(result)