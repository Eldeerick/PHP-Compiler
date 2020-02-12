
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA ID IGUAL LPAREN NUMBER POT RPAREN SOMA VEZESexp : exp SOMA exp1 \n    | exp1exp1 : exp1 VEZES exp2 \n    | exp2exp2 : exp2 POT exp3\n    | exp3exp3 : assign\n    | NUMBER\n    | ID\n    | callcall : ID LPAREN params RPAREN \n    | ID LPAREN RPARENparams : ID COMMA params\n    | IDassign : ID IGUAL exp'
    
_lr_action_items = {'RPAREN':([13,19,20,23,],[18,21,-14,-13,]),'SOMA':([1,2,3,4,5,6,7,8,14,15,16,17,18,21,],[-4,-2,-8,-7,-6,-10,11,-9,-5,-3,-1,11,-12,-11,]),'POT':([1,2,3,4,5,6,8,14,15,16,17,18,21,],[9,-2,-8,-7,-6,-10,-9,-5,9,-1,-15,-12,-11,]),'NUMBER':([0,9,10,11,12,],[3,3,3,3,3,]),'VEZES':([1,2,3,4,5,6,8,14,15,16,17,18,21,],[-4,10,-8,-7,-6,-10,-9,-5,-3,10,-15,-12,-11,]),'IGUAL':([8,],[12,]),'COMMA':([20,],[22,]),'LPAREN':([8,],[13,]),'ID':([0,9,10,11,12,13,22,],[8,8,8,8,8,20,20,]),'$end':([1,2,3,4,5,6,7,8,14,15,16,17,18,21,],[-4,-2,-8,-7,-6,-10,0,-9,-5,-3,-1,-15,-12,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'exp3':([0,9,10,11,12,],[5,14,5,5,5,]),'exp2':([0,10,11,12,],[1,15,1,1,]),'exp1':([0,11,12,],[2,16,2,]),'call':([0,9,10,11,12,],[6,6,6,6,6,]),'exp':([0,12,],[7,17,]),'params':([13,22,],[19,23,]),'assign':([0,9,10,11,12,],[4,4,4,4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('exp -> exp SOMA exp1','exp',3,'p_exp_soma','ExpressionLanguageParser.py',11),
  ('exp -> exp1','exp',1,'p_exp_soma','ExpressionLanguageParser.py',12),
  ('exp1 -> exp1 VEZES exp2','exp1',3,'p_exp1_vezes','ExpressionLanguageParser.py',15),
  ('exp1 -> exp2','exp1',1,'p_exp1_vezes','ExpressionLanguageParser.py',16),
  ('exp2 -> exp2 POT exp3','exp2',3,'p_exp2_expo','ExpressionLanguageParser.py',19),
  ('exp2 -> exp3','exp2',1,'p_exp2_expo','ExpressionLanguageParser.py',20),
  ('exp3 -> assign','exp3',1,'p_exp3','ExpressionLanguageParser.py',23),
  ('exp3 -> NUMBER','exp3',1,'p_exp3','ExpressionLanguageParser.py',24),
  ('exp3 -> ID','exp3',1,'p_exp3','ExpressionLanguageParser.py',25),
  ('exp3 -> call','exp3',1,'p_exp3','ExpressionLanguageParser.py',26),
  ('call -> ID LPAREN params RPAREN','call',4,'p_call','ExpressionLanguageParser.py',29),
  ('call -> ID LPAREN RPAREN','call',3,'p_call','ExpressionLanguageParser.py',30),
  ('params -> ID COMMA params','params',3,'p_params','ExpressionLanguageParser.py',33),
  ('params -> ID','params',1,'p_params','ExpressionLanguageParser.py',34),
  ('assign -> ID IGUAL exp','assign',3,'p_assign','ExpressionLanguageParser.py',37),
]
