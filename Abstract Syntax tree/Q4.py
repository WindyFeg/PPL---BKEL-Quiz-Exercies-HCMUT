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

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return None

    def visitVardecls(self,ctx:MPParser.VardeclsContext):

        return None

    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 

        return None

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return None

    def visitMptype(self,ctx:MPParser.MptypeContext):

        return None

    def visitIds(self,ctx:MPParser.IdsContext):

        return None