# VS Code

## Installation

```bash
wget -qO /tmp/microsoft.gpg.key \
    https://packages.microsoft.com/keys/microsoft.asc
cat /tmp/microsoft.gpg.key | gpg --dearmor \
    >/usr/share/keyrings/microsoft.gpg

cat <<EOF >/etc/apt/sources.list.d/microsoft.sources
Types: deb
URIs: https://packages.microsoft.com/repos/code
Suites: stable
Components: main
Signed-By: /usr/share/keyrings/microsoft.gpg
EOF

apt-get update
apt-get install code --install-recommends
   >>> Add Microsoft apt repository for Visual Studio Code?
   <<< NO
```

## Running

Go to the project folder and run

```bash
code .
```

## Extensions

### Claude Code for VS Code

From `View` -> `Extensions`, find "Claude Code for VS Code" and install it.
