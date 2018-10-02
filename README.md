# wmr_cba

wmr_cba is a Python library for controlling a [West Mountain Radio CBAIV](http://www.westmountainradio.com/cba.php).

libusb is used, tested in both Linux and Windows.  A simple Linux udev rules file is provided, as well as a Windows libusb WinUSB driver.  See the /drivers/ folders of the [GitHub repo](https://github.com/da66en/python_wmr_cba) for these files.  Windows users can also use the Windows drivers provided by West Mountain Radio, achieved by ctyping the West Mountain Radio driver DLLs.

This was developed by following the [SDK](http://www.westmountainradio.com/zip/cba4_api_sdk.zip) of the CBAIV provided by West Mountain Radio.

## How to use

The package can be installed using pip:

```
pip install wmr_cba
```

Some example code:

```python
from wmr_cba import wmr_cba

cba = wmr_cba.CBA4()
cba.do_start(1.0)
time.sleep(5)
print("Measured voltage under 1 Amp load: "+str(cba.get_voltage()))
cba.do_stop()
cba.close()
```

## License
wmr_cba is released under the MIT License. See LICENSE for more information.