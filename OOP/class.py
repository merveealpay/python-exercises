class X:
    def met(self):
        print("X OK")

class Y:
    def met(self):
        print("Y OK")


class Z(X,Y):
    def met(self):
        print("z ok")
        super(Z, self).met()
        #super().nesne()

class A(Z):
    def met(self):
        print("a ok")
        super(A,self).met()
       

object = A()
object.met()

 #y OK gor