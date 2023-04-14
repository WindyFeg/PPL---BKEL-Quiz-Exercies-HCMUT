
#! ALL OF CODE BELOW NEED TO BE TABBED WHEN SUBMITTING TO BKEL

def visitFloatLiteral(self, ctx, o):
    codegen = self.emit.emitPUSHFCONST(ctx.value, o.frame)
    return codegen, FloatType()