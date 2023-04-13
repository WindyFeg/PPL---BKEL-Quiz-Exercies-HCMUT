1. Given the following Scala fragment code:
object Timer {
def apply(interval: Int, repeats: Boolean = true)
         (op: => Unit) {
                  val timeOut = new javax.swing.AbstractAction() {
                            def actionPerformed(e: java.awt.event.ActionEvent) = op
                   }
                  val t = new javax.swing.Timer(interval, timeOut)
                  t.setRepeats(repeats)
                  t.start()
}
}
■ 3
□ 4
□ 2
□ 1


How many input parameters of method apply are there?

2. In the fragment code of question 1, how many input parameters of method actionPerformed  ?
□ 3
□ 4
□ 1
■ 2

3. Given a function definition as follows:

def f(a:Int, b:Int) = List(a,b)

Assume that when the function is called as follows: f(b=5,a=1), the result of the function is List(1,5). What is the argument-parameter corresponding?
□ By type
■ By name
□ By position
□ By value

4. Given the following fragment code:
void swap(int a, int b) {
   int t = a;
  a = b;
  b = t;
}
void main() {
    int a[3] = {2,1,0}, i = 0;
   swap(i,a[i]);
  cout << i << a[0] << a[1] << a[2];
}
If a and b of function swap are passed by value-result, the printed result is:
2010
If a and b of function swap are passed by reference, the printed result is:
2010
If a and b of function swap are passed by name, the printed result is :
2210