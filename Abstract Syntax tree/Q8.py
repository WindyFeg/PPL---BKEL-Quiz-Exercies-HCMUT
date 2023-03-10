# Given the grammar of MP as follows:

# INTLIT: [0-9]+ ;

# INTTYPE: 'integer';

# FLOATTYPE: 'real';

#? and AST classes as follows:

# @class Type():abstract

# @class CompoundType(Type):abstract

# @class UnionType(CompoundType):#firstType:Type,secondType:primType

# @class ArrayType(CompoundType):#indexType:Type,eleType:primType

# @class PrimType(Type):abstract

# @class IntType(PrimType): pass

# @class FloatType(PrimType): pass

# @class RangeType(PrimType): #lowbound:int; highbound:int

# ?Please copy the following class into your answer and modify the bodies of its methods to generate the AST of a MP input?

class ASTGeneration(MPVisitor):

    # program: mptype EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):

        return None

    # mptype: primtype | arraytype;
    def visitMptype(self,ctx:MPParser.MptypeContext):

        return None

    # arraytype:  primtype dimen | arraytype dimen  ;
    def visitArraytype(self,ctx:MPParser.ArraytypeContext):

        return None

    # primtype: INTTYPE | FLOATTYPE; 
    def visitPrimtype(self,ctx:MPParser.PrimtypeContext): 

        return None

    # dimen: '[' num '..' num ']';
    def visitDimen(self,ctx:MPParser.DimenContext):

        return None

    # num: '-'? INTLIT;
    def visitNum(self,ctx:MPParser.DimenContext):

        return None


 
