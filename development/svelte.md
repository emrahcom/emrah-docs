# svelte

Tested on `Debian 11 Bullseye`

### packages

Install `nodejs` (_16.x or newer_). See [nodejs](./nodejs.md).

### create app

run as `user`

```bash
mkdir -p ~/git-repo
cd ~/git-repo

npm create svelte@latest my-app
  Ok to proceed? (y) y
  Which Svelte app template? Skeleton project
  Add type checking with TypeScript? Yes, using TypeScript syntax
  Add ESLint for code linting? Yes
  Add Prettier for code formatting? Yes
  Add Playwright for browser testing? No

cd my-app
npm install
```

### adapter

Install an adapter.

```bash
npm i -D @sveltejs/adapter-node
```

Edit `svelte.config.js`

```javascript
//import adapter from '@sveltejs/adapter-auto';
import adapter from "@sveltejs/adapter-node";
```

### .prettierrc

```json
{
  "useTabs": false,
  "singleQuote": false,
  "trailingComma": "all",
  "printWidth": 80,
  "plugins": ["prettier-plugin-svelte"],
  "pluginSearchDirs": ["."],
  "overrides": [{ "files": "*.svelte", "options": { "parser": "svelte" } }],
  "quoteProps": "preserve",
  "tabWidth": 2
}
```

```bash
npm run format
```

### vite.config.ts

Add HMR port if needed.

```json
server: {
  hmr: {
    clientPort: 3000,
},
```

### check

```bash
npm run check
npm run lint
```

```bash
cd src
deno fmt --check
deno lint
```

### run (dev)

```bash
npm run dev -- --host --port 3000
```

### build

```bash
npm run build
```

### run (prod)

```bash
node build/index.js
```

### links

- [svelte.dev](https://svelte.dev/)
- [sveltekit](https://kit.svelte.dev/)
- [adapter](https://kit.svelte.dev/docs#adapters)
