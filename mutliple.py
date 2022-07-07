class A:
    def test1(self):
        print("from test1")
class B:
    def test2(self):
        print("from test2")
class c:
    def test3(self):
        print("from test3")
c1=c()
c1.test1()
c1.test2()
c1.test3()
print(issubclass(A,B))
print(issubclass(A,B))
print(issubclass(A,B))

print(isinstance(c1,A))



