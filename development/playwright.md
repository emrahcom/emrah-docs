## playwrigh

Tested on `Debian 11 Bullseye`

#### packages

run as `root`

```bash
apt-get update
apt-get install wget gpg

wget -qO /tmp/nodesource.gpg.key \
    https://deb.nodesource.com/gpgkey/nodesource.gpg.key
cat /tmp/nodesource.gpg.key | gpg --dearmor \
    >/usr/share/keyrings/nodesource.gpg
echo "deb [signed-by=/usr/share/keyrings/nodesource.gpg] \
    https://deb.nodesource.com/node_16.x bullseye main" \
    >/etc/apt/sources.list.d/nodesource.list

apt-get update
apt-get install nodejs
node --version
```

```bash
apt-get install libopengl0 libwoff1 libgles2
```

#### create app

run as `user`

```bash
mkdir myplay
cd myplay

npm init playwright
  Do you want to use TypeScript or JavaScript?
    TypeScript
  Where to put your end-to-end tests?
    tests
  Add a GitHub Actions workflow?
    false
  Install Playwright operating system dependencies?
    false
```

#### install dependencies

Show dependencies

```bash
npx playwright install-deps --dry-run
```

run as `root`

```bash
npx playwright install-deps
```

#### test

run as `user`

```bash
npx playwright test
npx playwright show-report
```

#### package.json

```javascript
  "browserName": "chromium",
```

#### sample code

_index.ts_

```javascript
const { chromium } = require("playwright");

async function main() {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto("https://emrah.com/");
  await page.locator('text=Jitok').click();
  await browser.close();
}

main();
```

#### run

```bash
node index.ts
```

#### codegen

A desktop environment is needed.

```bash
npx playwright codegen URL
```
