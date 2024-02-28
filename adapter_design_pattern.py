class UsbCable:
    def __init__(self) -> None:  # Constructor for the UsbCable class
        self.isPlugged = False  # Initialize the cable as not plugged in

    def plugSub(self):  # Method to plug the USB cable into a port
        self.isPlugged = True  # Set the cable as plugged in

class UsbPort:
    def __init__(self) -> None:  # Constructor for the UsbPort class
        self.portAvailable = True  # Initialize the port as available

    def plug(self, usb):  # Method to plug a USB device into the port
        if self.portAvailable:  # Check if the port is available
            usb.plugSub()  # Plug the USB device into the port
            self.portAvailable = False  # Set the port as not available after plugging

usbCable = UsbCable()  # Create a USB cable object
usbPort1 = UsbPort()  # Create a USB port object
usbPort1.plug(usbCable)  # Plug the USB cable into the port

class MicroUsbCable:
    def __init__(self) -> None:  # Constructor for the MicroUsbCable class
        self.isPlugged = False  # Initialize the cable as not plugged in

    def plugMicroUsb(self):  # Method to plug the micro USB cable into a port
        self.isPlugged = True  # Set the cable as plugged in

class MicroToUsbAdapter(UsbCable):  # Subclass of UsbCable for micro USB to USB adapter
    def __init__(self, microUsbCable):  # Constructor for the MicroToUsbAdapter class
        self.microUsbCable = microUsbCable  # Initialize the micro USB cable
        self.microUsbCable.plugMicroUsb()  # Plug the micro USB cable into the adapter

microToUsbAdapter = MicroToUsbAdapter(MicroUsbCable())  # Create a micro USB to USB adapter object
usbPort2 = UsbPort()  # Create another USB port object
usbPort2.plug(microToUsbAdapter)  # Plug the adapter into the port
