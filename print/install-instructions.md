
# Install instructions (printing)
There are a number of steps that need to be took in order to successfully print using a Brother QL series label printer. This repository uses the `brother-ql` package to print labels.

## Installing required packages

The first step is to install the required packages with:

```ps
pip install pillow pyusb brother-ql
```

## Installing libusb
You then need to install `libusb` next. For windows this is just a case of downloading `libusb-win32` from https://sourceforge.net/projects/libusb-win32/. For Ubuntu, you need to install it via `sudo apt-get install libusb-1.0-0-dev`.

