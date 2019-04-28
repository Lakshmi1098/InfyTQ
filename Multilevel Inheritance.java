import java.io.*;
import java.util.*;
import java.lang.*;
class A
{
void add()
{
System.out.println("Add method");-
}
}
class B extends A
{
void sub()
{
System.out.println("Subractor Method");
}
}
class C extends B
{
void multiply()
{
System.out.println("Multiply");
}
}
class D extends C
{
public static void main(String args[])
{
A aa=new A();
B bb=new B();
C cc=new C();
aa.add();
bb.sub();
cc.multiply();
}}
