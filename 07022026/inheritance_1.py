class Device:
    def device_info(self):
        print("This is a device.")

class TV(Device):
    def tv_info(self):
        print("This is a TV.")

class Mobile(TV):
    def mobile_info(self):
        print("This is a Mobile.")


if __name__ == "__main__":
    m1 = Mobile()
    m1.device_info()
    m1.tv_info()  # This will raise an error since Mobile does not have tv_info method
    m1.mobile_info()


