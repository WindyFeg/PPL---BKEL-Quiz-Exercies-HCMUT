# Given the grammar of MP as follows:

# INTTYPE: 'int';

# FLOATTYPE: 'float';

# ID: [a-z]+ ;

#? Please copy the following class into your answer and modify the bodies of its methods to return the HEIGHT of the parse tree? Your code starts at line 10.

class TerminalCount(MPVisitor):
# program: vardecls EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return 1 + self.visit(ctx.vardecls())

# vardecls: vardecl vardecltail;
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return 1 + max(self.visit(ctx.vardecl()), self.visit(ctx.vardecltail()))

# vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        return 1 + max(self.visit(ctx.vardecl()), self.visit(ctx.vardecltail())) if ctx.vardecl() else 0 

# vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return 1 + self.visit(ctx.ids())

# mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return None

# ids: ID ',' ids | ID; 
    def visitIds(self,ctx:MPParser.IdsContext):
        return 1 + self.visit(ctx.ids()) if ctx.ids() else 1