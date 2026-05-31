## Claude CLI

Tested on Debian 13 Trixie virtual machine.

### Installation

Create a Debian 13 Trixie virtual machine.

#### Deb packages

```bash
apt-get install curl ripgrep
```

#### Application

As non-root user:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Put `~/.local/bin` into `PATH`. In `.zshrc`:

```shell
export PATH=$PATH:~/.local/bin
```

#### Checking

```bash
claude --version
claude doctor
```

### Configuration

#### Tmux

Add the following line into `.tmux.conf`

```
set -g focus-events on
```
