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

# Please copy the following class into your answer and modify the bodies of its methods to return the height of the parse tree? Your code starts at line 10.

class Height(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return 1 + self.visit(ctx.vardecls())

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return 1 + max(self.visit(ctx.vardecl()), self.visit(ctx.vardecltail()))
 
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if ctx.vardecl():
            return 1 + max(self.visit(ctx.vardecl()), self.visit(ctx.vardecltail()))
        return 1

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return 1 + max(self.visit(ctx.mptype()), self.visit(ctx.ids()))

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return 2

    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.ids():
            return 1 + self.visit(ctx.ids())
        return 2