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

### VSCodeVim

From `View` -> `Extensions`, find "VSCodeVim" and install it.

### Remote - SSH

From `View` -> `Extensions`, find "Remote - SSH (Microsoft)" and install it.

Add hosts into `~/.ssh/config` and open it with:

```bash
code --remote ssh-remote+hostname /tmp
```

### Claude Code for VS Code

From `View` -> `Extensions`, find "Claude Code for VS Code (Anthropic)" and
install it.
