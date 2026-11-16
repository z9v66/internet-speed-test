from pip._internal.commands import download
from speedtest import Speedtest
wifi=Speedtest()
print("Internet speed .....")
Download=wifi.Download()
print(f"Downlad {Download / 1024 / 1024:.2f} mbs")
upload=wifi.upload()
print(f"Upload {upload / 1024 / 1024:.2f}")