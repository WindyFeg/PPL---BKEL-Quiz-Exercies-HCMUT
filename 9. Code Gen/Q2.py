    def visitFloatLiteral(self, ctx, o):
        codegen = self.emit.emitPUSHFCONST(ctx.value, o.frame)
        return codegen, FloatType()