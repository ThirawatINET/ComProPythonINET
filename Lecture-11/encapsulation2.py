class employee():
    def __init__(self):
        self.__maxearn = 30000

    def earn(self):
        print("earning is:{}".format(self.__maxearn))

    # setter method used for accessing private class
    def setmaxearn(self, earn):
        self.__maxearn = earn


emp1 = employee()
emp1.earn()

emp1.__maxearn = 10000   # ไม่ได้แก้ค่า private จริง
emp1.earn()

emp1.setmaxearn(15000)   # ใช้ setter แก้ค่า private จริง
emp1.earn()
