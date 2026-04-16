# llama.cpp

## Installation

Check `lspci`'s output and depending on the existing hardware, install the
additional packages.

For `nvidia`, add `contrib` and `non-free` into `debian.sources` and run:

```bash
apt-get update
apt-get install nvidia-driver nvidia-cuda-toolkit

reboot
```
