class Fun(object):
   @property
   def f1(self):
     print("20")
     return 1
   @f1.setter
   def f1(self, value):
     print("%r" % value)
   @f1.deleter
   def f1(self):
     print("Deleting")

f = Fun()
f.f1
f.f1 = 30
del f.f1
f.f1