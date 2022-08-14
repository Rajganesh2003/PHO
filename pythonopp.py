class Student :#advatange of init is reduce code size
    def __init__(self,name,rollno,dob,city):
        self.name= name
        self.dob=dob
        self.rollno = rollno
        self. city = city
    def address(self):
        addr = f"Name:{self.name}\nDOB :{self.dob}\nRollno:{self.rollno}\ncity:{self.city}"
        return addr
st1 = Student("Rajganesh",100,2003,"Tharamangalam")
st2 = Student("Prasanth",101,2003,"Tharamangalam")
print(st1.address())
print("\n"+st2.address())
