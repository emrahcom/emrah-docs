## Gemini

Tested on Debian 13 Trixie virtual machine.

#### Installation

- Create a Debian 13 Trixie vritual machine
- Install [NodeJS](../development/nodejs.md)
- Install Docker from Debian repo.\
  _Docker is needed for sandboxing._
  ```bash
  apt-get install docker.io --install-recommends
  adduser emrah docker
  ```
- Install Gemini as user
  ```bash
  npm install @google/gemini-cli

  mkdir -p ~/bin
  ln -s ~/node_modules/.bin/gemini  ~/bin/
  ```

#### Settings

Update `.gemini/settings.json`:

```json
{
  "security": {
    "auth": {
      "selectedType": "oauth-personal"
    }
  },
  "tools": {
    "sandbox": "docker"
  },
  "general": {
    "preferredEditor": "vim"
  }
}
```
