#
# * class VarDecl in AST is declared with field name in str type, typ in Type type. 
#* The visitor CodeGeneration has field emit keeping an object of Emitter 
# Field frame of the argument passed to parameter o of visitVarDecl contains object Frame for a local/parameter declaration and None for a global declaration.
# The method visitVarDecl must print out a directive declaration in jasmin code (use method printout(str) of Emitter) and 
#@ RETURNS an object of "Symbol" which has field name in str type, mtype in Type type and val in Val type. The Val type has 2 concrete classes: Index with field value in int type  (contain index of variable) and CName with field value in str type (contains name of the class which can get from self.className)
#$ Structure of return
# # return = Symbol(
# #     name = <str>,
# #     mtype = <Type object>,
# #     val = <Index or CName object> {value: <int or str>}
# # )

#name: str, typ: Type
#@ emitVAR(self, index, name, typ, startLabel, endLabel, frame)
#! ALL OF CODE BELOW NEED TO BE TABBED WHEN SUBMITTING TO BKEL

# name: str, typ: Type
#@ emitVAR(self,index, varName, inType, fromLabel, to Label)
def visitVarDecl(self,ctx,o):
    varName = ctx.name
    varType = ctx.typ
    if o.frame is None:
        codegen = self.emit.emitATTRIBUTE(varName, varType, False)
        self.emit.printout(codegen)
        return Symbol(varName, varType, CName(self.className))
    index = o.frame.getNewIndex()
    startLabel = o.frame.getStartLabel()
    endLabel = o.frame.getEndLabel()
    codegen = self.emit.emitVAR(index, varName, varType, startLabel, endLabel)
    self.emit.printout(codegen)
    return Symbol(varName, varType, Index(index))
