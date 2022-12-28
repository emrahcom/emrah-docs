## playwrigh

Tested on `Debian 11 Bullseye`

#### packages

Install `nodejs` (_16.x or newer_). See [nodejs](./nodejs).

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
  await page.locator("text=Jitok").click();
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

#### Jitsi sample

```javascript
const { chromium } = require("playwright");

async function main() {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext();
  await context.grantPermissions([]);

  const page = await context.newPage();
  await page.goto("https://meet.jit.si/test-1234");
  await page.locator('input[type="checkbox"]').check();
  await page.locator('[aria-label="Close"]').click();
  await page.locator('[placeholder="Enter your name here"]').fill("teacher");
  await page.locator('[data-testid="prejoin\\.joinMeeting"]').click();
  await page.locator('[aria-label="More actions"]').click();
  await page.locator('[aria-label="Toggle video sharing"]').click();
  await page.locator('[placeholder="YouTube link or direct video link"]').fill(
    "https://youtu.be/U-xjYyIOPAs",
  );
  await page.locator('button:has-text("Share")').click();

  await page.waitForSelector('[id="sharedVideoPlayer"]');
  const hdl = await page.$('[id="sharedVideoPlayer"]');
  const iframe = await hdl.contentFrame();
  await iframe.waitForSelector('[title="Replay"]', { timeout: 0 });

  await page.locator('[aria-label="More actions"]').click();
  await page.locator('[aria-label="Toggle video sharing"]').click();
  await browser.close();
}

main();
```
