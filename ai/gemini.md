## Gemini

Tested on Debian 13 Trixie virtual machine.

#### Installation

- Create a Debian 13 Trixie vritual machine
- Install [NodeJS](../development/nodejs.md)
- Install Docker from Debian repo
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
