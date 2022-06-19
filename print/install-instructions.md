
# Install instructions (printing)
There are a number of steps that need to be took in order to successfully print using a Brother QL series label printer. This repository uses the `brother-ql` package to print labels.

## Installing required packages

The first step is to install the required packages with:

```ps
pip install pillow pyusb brother-ql
```

## Exposing the installation folder globally
You need to add the `brother-ql` installation path to the global path variable. In Windows, you can simply do this via **Control Panel > Edit Environment Variables**.

You can see this path by typing `pip show brother-ql` or `pip show brother-ql | grep "Location"`

In Ubuntu, you can use `export PATH=...` to do this.


## Installing libusb
You then need to install `libusb` next. For windows this is just a case of downloading `libusb-win32` from https://sourceforge.net/projects/libusb-win32/. For Ubuntu, you need to install it via `sudo apt-get install libusb-1.0-0-dev`.

## Installing filter driver for the usb device
On windows, you just need to install the filter driver 