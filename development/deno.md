# deno

### install

```bash
cd /tmp
wget -T 30 -O deno.zip https://github.com/denoland/deno/releases/latest/download/deno-x86_64-unknown-linux-gnu.zip
unzip deno.zip
./deno --version

cp /tmp/deno /usr/local/bin/
deno --version
```

### help

```bash
deno help
deno help run
```

### run

```bash
deno run --allow-net index.ts
deno run --watch --unstable --allow-net index.ts
```

### format check

```bash
deno fmt --check
deno fmt --check index.ts
```

### lint

```bash
deno lint
deno lint index.ts
```

### cache

```bash
rm -rf .cache/deno
```
