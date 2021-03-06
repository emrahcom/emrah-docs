## svelte

Tested on `Debian 11 Bullseye`

#### packages

run as `root`

```bash
wget -qO /tmp/nodesource.gpg.key \
    https://deb.nodesource.com/gpgkey/nodesource.gpg.key
cat /tmp/nodesource.gpg.key | gpg --dearmor \
    >/usr/share/keyrings/nodesource.gpg
echo "deb [signed-by=/usr/share/keyrings/nodesource.gpg] \
    https://deb.nodesource.com/node_16.x bullseye main" \
    >/etc/apt/sources.list.d/nodesource.list

apt-get update
apt-get install nodejs
```

#### create app

run as `user`

```bash
mkdir -p ~/git-repo
cd ~/git-repo

npm create svelte my-app
  Ok to proceed? (y) y
  Which Svelte app template? Skeleton project
  Add type checking with TypeScript? Yes, using TypeScript syntax
  Add ESLint for code linting? Yes
  Add Prettier for code formatting? Yes
  Add Playwright for browser testing? No

cd myapp
npm install
```

#### adapter

Install an adapter.

```bash
npm install @sveltejs/adapter-node@next --save-dev
```

Edit `svelte.config.js`

```javascript
//import adapter from '@sveltejs/adapter-auto';
import adapter from "@sveltejs/adapter-node";
```

#### .gitignore

Add the followings into `.gitignore`

```config
*~
*.sw?
*.log
package-lock.json
```

#### .prettierrc

```json
{
  "printWidth": 80,
  "quoteProps": "preserve",
  "singleQuote": false,
  "tabWidth": 2,
  "trailingComma": "all",
  "useTabs": false
}
```

#### check

```bash
npm run check
npm run lint
```

```bash
cd src
deno fmt --check
deno lint
```

#### run (dev)

```bash
npm run dev -- --host --port 3000
```

#### build

```bash
npm run build
```

#### run (prod)

```bash
node build/index.js
```

#### links

- [svelte.dev](https://svelte.dev/)
- [sveltekit](https://kit.svelte.dev/)
- [adapter](https://kit.svelte.dev/docs#adapters)
