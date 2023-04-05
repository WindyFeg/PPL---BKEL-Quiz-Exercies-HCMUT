1. Given the following infix expression: (a + b + c) * d - e * f * g  and the precedence and associativity of the operators in the expression are like those in C. Transverse it into the Polish prefix format?

□ - * + a +  b c d * f * g h
□ - * + + a b c d * e * f g
■ - * + + a b c d * * e f g
□ - + + a b c * d * * e f g

2. Determine each of the following statements is TRUE or FALSE?

Cambridge Polish Prefix expression requires the number of operands of every operator fixed.
□ True	■ False

Polish prefix expression is suitable just for binary operators.  
□ True	■ False

Normal prefix expression has operators staying outside  (). 
■ True	□ False

3. Assume that the precedence and associativity of operators in the following infix expression are like those in C: a * b * ( c - e - f) * g.  Rewrite the expression in other notations while keeping the appearance order of operands. No space is allowed.

The Polish prefix notation of the above expression is 
***ab--cefg


The Cambridge Polish prefix notation of the above expression is


The Polish postfix of the above expression is
ab*ce-f-*g*

4. Given the following expression in Polish prefix notation: * * a + b c - d * e f
With the minimum of egg, the same appearance order of operands and no space, the equivalent expression in infix notation is?

□ a*b+c*d-e*f
■ a*(b+c)*(d-e*f)
□ (a+b)*(c-d)*e*f
□ (a*(b+c))*(d-(e*f))

5. Assume that the value of variable a is  6. Select possible values of the following C expression: a + (a = 3) * a?

■ 24
■ 21
■ 15
■ 12

6. Assume that the value of variable x is  5. After the execution of the following logical expression written in C (where logical expressions are short-circuit evaluated): ((x = 1) == 1) && ((x = 2) == 3) && ((x = 3) == 3), what is the value of  x ?

□ 3
□ 5
■ 2
□ 1


7. When execution an assignment statement, the left hand side expression will be calculated to determine its

□ value
□ type
□ name
■ address


8. When execution an assignment statement, the right hand side expression will be calculated to determine its

□ name
■ value
□ type
□ address