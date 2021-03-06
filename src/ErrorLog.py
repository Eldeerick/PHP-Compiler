import SymbolTable as st

def AttributionTypeError(self, assignExpr, exprType):
  print('ERROR: Atribution to variable ', end='')
  assignExpr.variable.accept(self.printer)
  print(' returned type', exprType)
  
def AttributionInvalidTypeError(self, exprType, assignExpr, bindable):
  print('ERROR: Invalid atribution of type', exprType, end='') 
  print(' on variable ', end='') 
  assignExpr.variable.accept(self.printer)
  print(' that has type', bindable[st.TYPE])

def UnresolvedArithError(self, expr,op):
  print('ERRRO: Cannot resolve this arithmetic expression: ',end='')
  expr.expr1.accept(self.printer)
  print(op,end='')
  expr.expr2.accept(self.printer)

def IncrementVariableError(variable):
  print('ERROR: Cannot increment variable', variable[st.NAME], 'with type', variable[st.TYPE])
  
def DecrementVariableError(variable):
  print('ERROR: Cannot decrement variable', variable[st.NAME], 'with type', variable[st.TYPE])
  
def UnaryArithError(self, variable, op):
  print('ERRRO: Cannot ',op,' a variable: ', variable[st.NAME],', because is not contains valid number')

def ExpressionTypeError(self, expr, type1, type2):
  print('ERROR: Expression ', end='')
  expr.expr1.accept(self.printer)
  print(' has type', type1, 'while expression ', end='')
  expr.expr2.accept(self.printer)
  print(' has type', type2)

def ExpressionBoolError(self, exprBoolean, opComp, arrInvalid):
  print('ERROR: Expected boolean expression, but got type:', arrInvalid, end=' ') 
  exprBoolean.expr1.accept(self.printer)
  print(opComp,end='')
  exprBoolean.expr2.accept(self.printer)
  print('')
