class Phone:
    def call(self):
        print("Calling...")

class Camera:
    def click(self):
        print("Clicking...")

class SmartPhone(Phone, Camera):
    def browse(self):
        print("Browsing the internet...")

if __name__ == "__main__":
    sp = SmartPhone()
    sp.call()  # Inherited from Phone
    sp.click()  # Inherited from Camera
    sp.browse()  # Defined in SmartPhone