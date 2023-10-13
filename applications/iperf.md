# iperf

Don't install `iperf3`

## Installing

```bash
apt-get install iperf
   No auto-start
```

## Testing

On server:

```bash
iperf -s -u -p 10000
```

On client:

```bash
iperf -c IP-ADDRESS -u -p 10000 -b 5M -i 5
```

## Options:

- s: server
- c: client
- u: udp
- p: port
- b: target bandwidth
- i: interval
