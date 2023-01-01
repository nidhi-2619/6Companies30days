class Solution:
    def evalRPN(self, tokens) -> int:
       s = []
       Operators={
           '+': lambda x,y:(x+y),
           '-': lambda x,y:(x-y),
           '*': lambda x,y:(x*y),
           '/': lambda x,y:(x/y)
       }  
       for i in tokens:
           if i not in Operators:
               s.append(int(i))
           else:
            #    when we encounter the operator
               op1 = s.pop()
               op2 = s.pop()
               ans = Operators[i](op2,op1)
               s.append(int(ans))
       return s.pop()