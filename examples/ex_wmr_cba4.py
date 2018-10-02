"""
A simple example of using the wmr_cba CBA4 python library.

For more information about the wmr_cba package, drivers and documentation, see
the GitHub repo at:
https://github.com/da66en/python_wmr_cba

Will connect to first available CBA4, draw 150mA for 10 seconds and then stop.
While it is drawing current it will print voltage/current status on the console
every second.

The CBA will not draw power if there is no voltage connected to it.  So if
you do not have voltage connected to it this is the reason why the feedback 
result will show 0 Amps even if you requested it to draw current.

Windows users:
If there is an error finding the CBA drivers, you have some options.  If you
are using the libusb/WinUSB drivers (the .inf file provided in the GitHub repo)
then you either need to install libusb so that the drivers can be found in the
global search path, or place libusb-1.0.dll (from libusb) into the same 
directory as the script.  If you are using the drivers provided by West
Mountain Radio, then place mpusbapi.dll into the same directory as the 
Python script.
"""

from wmr_cba import wmr_cba
import time

def cba4_example():
    def show_status():
        disp = "Volts=" + str(cba.get_voltage()) + "V"
        disp += " Load=" + str(cba.get_set_current()) + "A"
        disp += " Feedback=" + str(cba.get_measured_current()) + "A"
        disp += " Running=" + str(cba.is_running())
        disp += " PLim=" + str(cba.is_power_limited())
        print(disp)
        #end show_status()

    test = wmr_cba.CBA4.test()
    if test:
        print("Test ERROR: " + test)
    else:
        print("Test OK")

    devices = wmr_cba.CBA4.scan()
    print("Found "+str(len(devices))+" devices.")

    cba = wmr_cba.CBA4()

    if not cba.is_valid():
        print("ERROR!  Couldn't open a device!")
        exit(-1)
    
    print("Opened CBA4, serial #" + str(cba.get_serial_number()))

    show_status()

    load = 0.15

    print("Starting load = " + str(load))

    cba.do_start(load)

    reads = 10
    while reads:
        time.sleep(1)
        show_status()
        reads -= 1
    
    cba.do_stop()
    print("Stopped test")

    reads = 5
    while reads:
        time.sleep(1)
        show_status()
        reads -= 1

    cba.close()

    print("Done")
    #end __test_cba4

if __name__ == "__main__":
    print("running ex_wmr_cba4.py")

    cba4_example()