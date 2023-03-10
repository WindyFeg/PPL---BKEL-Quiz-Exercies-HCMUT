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

# ?Please copy the following class into your answer and modify the bodies of its methods to generate the AST of a MP input?

class ASTGeneration(MPVisitor):

    # program: vardecls EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(self.visit(ctx.vardecls())) 

    # vardecls: vardecl vardecltail;
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        res = self.visit(ctx.vardecl())
        if ctx.vardecltail():
            res += self.visit(ctx.vardecltail())
        return res  
    
    # int a; -> vardecl
    # int b; -> vardecltail -> vardecl
    # int c; -> vardecltail -> vardecltail -> vardecl
    # vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
    
    # vardecl: mptype ids ';' ;
    # int a,b; -> [VarDecl(Id(a),IntType())] + [VarDecl(Id(b),IntType())]
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return list(map(
            lambda x: VarDecl(x, self.visit(ctx.mptype())),
            self.visit(ctx.ids())
        ) )

    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    # ids: ID ',' ids | ID; 
    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        # return as a list
        return [Id(ctx.ID().getText())] + self.visit(ctx.ids())