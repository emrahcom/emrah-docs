# llama.cpp

## Installation

Check `lspci`'s output and depending on the existing hardware, install the
additional packages.

### nvidia

For `nvidia`, add `contrib` and `non-free` into `debian.sources` and run:

```bash
apt-get update
apt-get install linux-headers-amd64
apt-get install nvidia-driver nvidia-cuda-toolkit

reboot
```

### builder

```bash
apt-get install build-essential cmake libssl-dev
```

### llama.cpp

```bash
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
```

Build depending on the hardware:

```bash
cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release -j $(nproc)
```
