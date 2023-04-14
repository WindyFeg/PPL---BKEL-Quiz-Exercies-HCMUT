
#* class Assign(Stmt) in AST is declared with field lhs and rhs in Expr type.  The types of the left hand side and right hand side are the same.
#* The visitor CodeGeneration has field emit keeping an object of Emitter 
#* Object is passed to the parameter o of visitId has 2 fields:
#* Field frame keeps object Frame. 
#* Field sym of the argument keeps a list of Symbol which has three fields: name (str type), mtype (Type type) and value (Val type). The Val type has two concrete classes: Index with field value in int type and CName with field value in str type. An Index object keeps the index of the variable while a CName keeps the name of the class name (used for global variable). The first element of sym contains the identifier which belongs to the innermost referencing environment while the last element of sym contains one in the outermost referencing environment (global).
# When visiting the expression in the left hand side or the right hand side of the assignment statement, object Access must be passed to parameter o where Access has 3 fields:
#* frame and sym are similar to the object passed to parameter o 
#* Field isLeft in boolean type indicates the identifier in the left (isLeft true) or in the right (isLeft false).
# The method visitAssign must print out the code of the assignment statement (use method printout of Emitter)

#$ Object o:
# o = {
#     "frame": <Frame object>,
#     "sym": [
#         {
#             "name": "x",
#             "mtype": <Type object>,
#             "value": <Index or CName object> {value: <int or str>}
#         },
#         ...
#     ]
# }

#$ Object Access:
# Access = {
#     "frame": <Frame object>,
#     "sym": [
#         {
#             "name": "x",
#             "mtype": <Type object>,
#             "value": <Index or CName object> {value: <int or str>}
#         },
#         ...
#     ],
#     "isLeft": <boolean>
# }

# lhs: Expr, rhs: Expr

def visitAssign(self, ctx, o):
    left_access = Access(o.frame, o.sym, True)
    right_access = Access(o.frame, o.sym, False)
    rhs = ctx.rhs.accept(self, right_access)
    lhs = ctx.lhs.accept(self, left_access)
    return self.emit.printout(rhs[0] + lhs[0])