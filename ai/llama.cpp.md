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

./build/bin/llama-cli --version
```

```bash
mkdir -p ~/bin

ln -s ~/git-repo/llama.cpp/build/bin/llama-cli ~/bin/
ln -s ~/git-repo/llama.cpp/build/bin/llama-server ~/bin/
```

## Model

### llama-cli

```bash
llama-cli -ngl 26 -c 8192 -hf ggml-org/gemma-3-1b-it-GGUF
llama-cli -ngl 35 -c 8192 -hf unsloth/gemma-4-E2B-it-GGUF:Q8_0
llama-cli -ngl 42 -c 8192 -hf unsloth/gemma-4-E4B-it-GGUF:Q8_0
llama-cli -ngl 32 -c 8192 -hf unsloth/Qwen3.5-9B-GGUF:Q4_K_M
```

### llama-server

```bash
llama-server -ngl 99 -c 8192 -hf ggml-org/gemma-3-1b-it-GGUF
llama-server -ngl 99 -c 8192 -hf unsloth/gemma-4-E2B-it-GGUF:Q8_0
llama-server -ngl 99 -c 8192 -hf unsloth/gemma-4-E4B-it-GGUF:Q8_0
llama-server -ngl 99 -c 8192 -hf unsloth/Qwen3.5-9B-GGUF:Q4_K_M
```

### removing the model

```bash
cd ~/.cache/huggingface/hub
ls
rm -rf folder
```
