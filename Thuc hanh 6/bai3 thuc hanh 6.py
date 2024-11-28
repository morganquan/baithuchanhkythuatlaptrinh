print("Pham Viet Quan mssv 235752021610022")
class Nguoi:
    def getGender(self):
        pass

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"
nguoi_nam = Nam()
nguoi_nu = Nu()

print("Giới tính của người thứ nhất:", nguoi_nam.getGender())
print("Giới tính của người thứ hai:", nguoi_nu.getGender())
