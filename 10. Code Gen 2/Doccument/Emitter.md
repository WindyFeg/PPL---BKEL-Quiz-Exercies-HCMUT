Code Gen
Framework:
	- Machine-Dependent Code Generation
	- Intermediate Code Gen: phụ thuộc mã nguồn + máy.
	- Frame: quản các local array
	- Machine-Independent Code Generation: sẽ viết cái này.
--------------------------------------------------------------
Machine-Dependent Code Generation
- Hiện thực MachineCode.py
- Imple in JasminCode.
- Có các phương thức ứng với các lệnh Jasmin.
VD:
emitLDC(20) -> "ldc 20"
emitICONST(1) -> iconst_1
-------------------------------------------------------------
Intermediate Code Gen
- Emitter.py
- Giúp việc sinh mã thuận lợi.
VD:
emitREADVAR(a)	-> emitILOAD(index) / emitFLOAD(index)
- Lựa chọn data obj.
- Simulate việc thực thi máy.
	emitICONST -> push()
	emitISTORE -> pop()
---------------------------------------------------------------
API
emitVAR(self,index, varName, inType, fromLabel, to Label)
.var 0 is this Lio; from Label0 to Label1
-> sinh ra 1 khai báo lệnh.
	- index biến local
	- tên
	- type
	- from Label
	- to Label 

emitATTRIBUTE(self, lexeme, inType, isFinal, value=None)
.field public static write Ljava/io/Write;
-> xuất ra field
	- tên
	- type
	- const ? or ko const ?(T/F)
	- value= ?

emitMETHOD(self, lexeme, inType, isStatic)
.method public foo(I)I
-> khai báo method
	- tên/ type/ T or F

emitENDMETHOD(self, frame)
.limit stack 1
.limit locals 1	//xem là đang xài bao nhiêu biến
.end method
-> kết thúc
	- dựa vào frame

emitPROLOG(self, name, parent)
.source io.java
.class public io
.super java/lang/Object
-> gọi khi tạo class (tên, lớp cha)

emitEPILOG(self)
->ghi lệnh mình ghi (đang ở buffer) đổ xuống file

--------------------------------------------------------
Type

class IntType(Type)
(Float/String/Void/Bool)
class ClassType(Type): #cname:str
class ArrayType(Type): #eleType: Type, dimen: List[int]
class MType(Type): #partype: List[Type], rettype: Type
---------------------------------------------------------
API
emitADDOP(self,lexeme, inType, frame)
-> iadd, fadd, isub, fsub
- Xuất phát từ thông số đưa vào
- lexeme: +, -
- inType: IntType, FloatType

emitMULOP(self,lexeme, inType, frame)
-> imul, fmul, idiv, fdiv

emitDIV(self, frame)
-> idiv

emitMOD(self, frame)
->irem

emitANDOP(self, frame)
-> iand

emitOROP(self, frame)
->ior

emitREOP(self, op, inType, frame)
-> >, <, >=, <=, !=, ==

emitRELOP(self, op, inType, trueLabel, falseLable, frame)
-> for condition in ifstmt
-----------------------------------------------------------
READ/WRITE

emitREADVAR(self, name, inType, index, frame)
-> [ifa]load

emitALOAD(self, inType, frame)
-> đọc 1 thành phần dãy
-> [ifa]load
-> qui trình: đọc từ tp dãy: aload đọc địa chỉ dãy,
đọc chỉ số, lệnh load

emitWRITEVAR(self, name, inType, index, frame) 
-> [ifa]store

emitASTORE(self, inType, frame) 
-> [ifa]astore

emitGETSTATIC(self, lexeme, inType, frame) 
-> getstatic

emitGETFIELD(self, lexeme, inType, frame) 
-> getfield

emitPUTSTATIC(self, lexeme, inType, frame) 
-> putstatic

emitPUTFIELD(self, lexeme, inType, frame) 
-> putfield
-------------------------------------------------------------
Others

emitPUSHICONST(self, input, frame)
-> iconst, bipush, sipush, ldc

emitPUSHFCONST(self, input, frame) 
-> fconst, ldc

emitINVOKESTATIC(self, lexeme, inType, frame) 
-> invokestatic

emitINVOKESPECIAL(self, frame, lexeme=None, inType=None)
-> invokespecial (constuctor, private field method, method cha)

emitINVOKEVIRTUAL(self, lexeme, inType, frame) 
-> invokevirtual (gọi instance method)

emitIFTRUE(self, label, frame) 
-> ifgt (sinh mã trên đỉnh stack)

emitIFFALSE(self, label, frame) 
-> ifle

emitDUP(self,frame) 
-> dup x2

emitPOP(self,frame) 
-> pop

emitI2F(self, frame) 
-> i2f

emitRETURN(self, inType, frame) 
-> return, ireturn

emitLABEL(self, label, frame) 
-> Label sinh ra label (địa chỉ)

emitGOTO(self, label, frame) 
-> goto, chuyển đến Label (all giá trị nguyên)
--------------------------------------------------------------
Frame
- Dùng để quản lý, quản lý method.
*Label: hợp lệ thân phương thức
getNewLabel(): return a new label

getStartLabel(): return the beginning label of a scope
-> trả về label đầu tiên scope (gọi khi vào scope)

getEndLabel(): return the end label of a scope
-> tương tự

getContinueLabel(): return the label where a continue should
come
-> trả về label lệnh continue nhảy đến (phải đặt emit Label trước)

getBreakLabel(): return the label where a break should come

enterScope()
-> đi với start label

exitScope()

enterLoop()

exitLoop()
*Local variable array
getNewIndex(): return a new index for a variable

getMaxIndex(): return the size of the local variable array
-> biến trong scope cấp index, ra thì hủy -> dawmmmm

* Operand stack
push(): simulating a push execution

pop(): simulating a pop execution

getMaxOpStackSize(): return the max size of the operand stack

- Implemented in class Frame.py
---------------------------------------------------------
Machine-Independent Code Generation
- Dựa trên ngôn ngữ
- Dùng method Frame.py, Emitter.py
- Viết các mapping
A src program -> Java class
A global variable -> static field
A function -> a static method
A parameter -> a parameter
A local variable -> a local variable
An expression -> an expression
A statement -> a statement
An invocation -> an invocation