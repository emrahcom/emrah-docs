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
apt-get install nvtop

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
./build/bin/llama-cli --list-devices
```

```bash
mkdir -p ~/bin

ln -s ~/git-repo/llama.cpp/build/bin/llama-cli ~/bin/
ln -s ~/git-repo/llama.cpp/build/bin/llama-server ~/bin/
```

## Model

### llama-cli

```bash
llama-cli -hf unsloth/gemma-4-E2B-it-GGUF:UD-Q4_K_XL -ngl 99
llama-cli -hf ggml-org/gemma-4-E4B-it-GGUF:Q4_K_M -ngl 99
llama-cli -hf unsloth/Qwen3.5-9B-GGUF:Q4_K_M -ngl 99
```

### llama-server

```bash
llama-server -hf ggml-org/gemma-4-E4B-it-GGUF:Q4_K_M -ngl 99
llama-server -hf unsloth/Qwen3.5-9B-GGUF:Q4_K_M -ngl 99
```

### parameters

- `--reasoning [on|off|auto]`
- `--embeddings --pooling mean`

### removing the model

```bash
cd ~/.cache/huggingface/hub
ls
rm -rf folder
```
