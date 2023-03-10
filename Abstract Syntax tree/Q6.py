# Given the grammar of MP as follows:

# INTTYPE: 'int';

# FLOATTYPE: 'float';

# ID: [a-z]+ ;

# ?and AST classes as follows:

# $class Program:#decl:list(VarDecl)

# @class Type(ABC): pass

# $class IntType(Type): pass

# $class FloatType(Type): pass

# $class VarDecl: #variable:Id; varType: Type

# $class Id: #name:str

# ?Please copy the following class into your answer and modify the bodies of its methods to generate the AST of a MP input?

from functools import reduce

class ASTGeneration(MPVisitor):

    # program: vardecl+ EOF;
    # int a,b; -> [VarDecl(Id(a),IntType())] + [VarDecl(Id(b),IntType())]
    def visitProgram(self,ctx:MPParser.ProgramContext):
        # flattern list of list
        result = reduce(
            lambda acc, cur: acc + cur,
            [self.visit(vars) for vars in ctx.vardecl()],
            []
        )
        return Program(result)

    # vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return [VarDecl(Id(id.getText()), self.visit(ctx.mptype())) for id in ctx.ids().ID()]

    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    # ids: ID (',' ID)*; 
    # int a,b,c; -> [Id(a),Id(b),Id(c)]
    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(str(id.getText())) for id in ctx.ID()]