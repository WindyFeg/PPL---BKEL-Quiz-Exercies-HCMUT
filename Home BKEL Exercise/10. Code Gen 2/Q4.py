    
#* class Id in AST is declared with field name in str type. 
#* The visitor CodeGeneration has field emit keeping an object of Emitter 
#* Object is passed to the parameter o of visitId has 3 fields:
#* Field frame keeps object Frame. 
#* Field sym of the argument keeps a list of Symbol which has three fields: name (str type), mtype (Type type) and value (Val type). The Val type has two concrete classes: Index with field value in int type and CName with field value in str type. 
#* An Index object keeps the index of the variable while a CName keeps the name of the class name (used for global variable). The first element of sym contains the identifier which belongs to the innermost referencing environment while the last element of sym contains one in the outermost referencing environment (global).
# Field isLeft in boolean type indicates the identifier in the left (isLeft true) or in the right (isLeft false).
# The method visitId must return a pair of jasmin code to read or write value of the identifier and the type of the identifier (one object of a subclass of class Type)

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
#     ],
#     "isLeft": <boolean>
# }

#$ return value: (jasmin <str>, Type <Type object>)
#! ALL OF CODE BELOW NEED TO BE TABBED WHEN SUBMITTING TO BKEL 
    
# name: str
def visitId(self, ctx, o):
    name = ctx.name
    sym = o.sym
    #print([(x.name,x.value) for x in sym])
    for s in sym:
        #print(type(s.value))
        if s.name == name:
            if o.isLeft:
                if type(s.value) is Index:
                    # Local variable
                    codegen = self.emit.emitWRITEVAR(name, s.mtype, s.value.value, o.frame)
                else:
                    # Global variable
                    codegen = self.emit.emitPUTSTATIC(s.value.value + '/' + name, s.mtype, o.frame)
            else:
                if type(s.value) is Index:
                    # Local variable
                    codegen = self.emit.emitREADVAR(name, s.mtype, s.value.value, o.frame)
                else:
                    # Global variable
                    codegen = self.emit.emitGETSTATIC(s.value.value + '/' + name, s.mtype, o.frame)
            return codegen, s.mtype
