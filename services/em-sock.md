## em-sock and em-vpn

#### vpn user

```bash
adduser vpn --system --group --disabled-password --home /home/vpn \
  --shell /bin/zsh
chmod 700 /home/vpn

mkdir /home/vpn/.ssh
chmod 700 /home/vpn/.ssh

cp em-vpn em-vpn.pub /home/vpn/.ssh/
cp /root/.ssh/authorized_keys /home/vpn/.ssh/
chmod 644 /home/vpn/.ssh/authorized_keys

chown vpn:vpn /home/vpn/.ssh -R
```

#### /home/vpn/.ssh/config

```
Host em-sock
    Hostname mydomain0.com
    User vpn
    Port 10251
    DynamicForward 65022
    IdentityFile ~/.ssh/em-vpn
    IdentitiesOnly yes
    ConnectTimeout 10
    ServerAliveInterval 10
    ServerAliveCountMax 3
    StrictHostKeyChecking no
    UserKnownHostsFile /dev/null
    BatchMode yes
    LogLevel ERROR

Host em-sock-1
    Hostname mydomain1.com
    User vpn
    Port 22
    DynamicForward 65022
    IdentityFile ~/.ssh/em-vpn
    IdentitiesOnly yes
    ConnectTimeout 10
    ServerAliveInterval 10
    ServerAliveCountMax 3
    StrictHostKeyChecking no
    UserKnownHostsFile /dev/null
    BatchMode yes
    LogLevel ERROR

Host em-vpn
    Hostname mydomain.com
    User vpn
    Port 10251
    RemoteForward 60090 localhost:22
    IdentityFile ~/.ssh/em-vpn
    IdentitiesOnly yes
    ConnectTimeout 10
    ServerAliveInterval 10
    ServerAliveCountMax 3
    StrictHostKeyChecking no
    UserKnownHostsFile /dev/null
    BatchMode yes
    LogLevel ERROR
```

#### /etc/systemd/system/em-sock.service

```
[Unit]
Description=My Socks Proxy
After=network.target

[Service]
User=vpn
Group=vpn
WorkingDirectory=/home/vpn
ExecStart=/usr/bin/ssh em-sock
Restart=always
RestartSec=2s

[Install]
WantedBy=multi-user.target
```

Activate the service:

```bash
systemctl daemon-reload
systemctl enable em-sock.service
systemctl start em-sock.service
```

#### /etc/systemd/system/em-vpn.service

```
[Unit]
Description=My VPN
After=network.target

[Service]
User=vpn
Group=vpn
WorkingDirectory=/home/vpn
ExecStart=/usr/bin/ssh em-vpn
Restart=always
RestartSec=2s

[Install]
WantedBy=multi-user.target
```

Activate the service:

```bash
systemctl daemon-reload
systemctl enable em-vpn.service
systemctl start em-vpn.service
```
