# Given the grammar of MP as follows:

# program: vardecls EOF;

# vardecls: vardecl vardecltail;

# vardecltail: vardecl vardecltail | ;

# vardecl: mptype ids ';' ;

# mptype: INTTYPE | FLOATTYPE;

# ids: ID ',' ids | ID; 

# INTTYPE: 'int';

# FLOATTYPE: 'float';

# ID: [a-z]+ ;

# and AST classes as follows:

# class Program:#decl:list(VarDecl)

# class Type(ABC): pass

# class IntType(Type): pass

# class FloatType(Type): pass

# class VarDecl: #variable:Id; varType: Type

# class Id: #name:str

# Please copy the following class into your answer and modify the bodies of its methods to generate the AST of a MP input?
class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(self.visit(ctx.vardecls()))

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail()) if ctx.vardecltail() else []

    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if(ctx.vardecl()):
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
        return []
        
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return [str(VarDecl(x, self.visit(ctx.mptype()))) for x in self.visit(ctx.ids())]

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        if(ctx.ids()):
            return [Id(ctx.ID().getText())] + self.visit(ctx.ids())
        return [Id(ctx.ID().getText())]