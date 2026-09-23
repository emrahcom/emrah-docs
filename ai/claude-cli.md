## Claude CLI

Tested on Debian 13 Trixie virtual machine.

### Installation

Create a Debian 13 Trixie virtual machine.

#### Deb packages

```bash
apt-get install curl ripgrep gh
```

#### Application

As non-root user:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Put `~/.local/bin` into `PATH`. In `.zshrc`:

```shell
export PATH=$PATH:~/.local/bin
export ANTHROPIC_MODEL=claude-opus-5-5
```

#### Checking

```bash
claude --version
claude doctor
```

### Configuration

#### Global settings

~/.claude/settings.json

```json
{
  "env": {
    "CLAUDE_CODE_DISABLE_MOUSE": "1"
  },
  "tui": "fullscreen",
  "theme": "auto"
}
```

#### Tmux

Add the following line into `.tmux.conf`

```
set -g focus-events on
```

### Commands

#### Sessions

Creating a named session:

```bash
claude -n "session-name"
```

Attaching the session:

```bash
claude -r "session-name"

# or just -r to get a list
claude -r
```

- Use `/resume` to change the session during the runtime.
- Use `/rename` to change the session name.
- Using two separate sessions for planning and implementing works great.\
  Such as "project-planner" and "project-worker"
