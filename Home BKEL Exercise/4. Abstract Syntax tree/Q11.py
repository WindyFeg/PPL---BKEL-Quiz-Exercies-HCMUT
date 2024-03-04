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

# Please copy the following class into your answer and modify the bodies of its methods to count the internal nodes in the parse tree?

class NonTerminalCount(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return 2 + self.visit(ctx.vardecls())

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return 2+self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        return (2+ self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())) if ctx.vardecl() else 0

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return 2 + self.visit(ctx.ids())

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return None

    def visitIds(self,ctx:MPParser.IdsContext):
        return (1 + self.visit(ctx.ids())) if ctx.ids() else 0