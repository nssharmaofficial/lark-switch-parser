# Switch parser using Lark

This project was an assignment for the NLP class at University of Siena.

## Assignment 

Using lark implement a parser for managing the **switch** statement in a simplified version.

- the variable used in the switch is one integer variable in a predefined set of two variables `x`, `y`.
- the values to `x`, `y` are assigned before the if statement (assume 0 if there is no assignment)
- the switch instruction has the following syntax

   ```lark
   switch(var) {
     case 0: z=cost0;
             break;

      ...
     case N: z=costN;
             break;

     default: z=costD;
             break;
   }
   ```

- the instruction contains only the assignment of a constant value to the variable `z`
- at the end print the value of the variable `z`

