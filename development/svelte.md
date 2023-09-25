# svelte

Tested on `Debian 11 Bullseye`

### packages

Install `nodejs`. See [nodejs](./nodejs.md).

Install `yarn`. See [yarn](./yarn.md).

### create app

run as `user`

```bash
mkdir -p ~/git-repo
cd ~/git-repo

npm create svelte@latest my-app
  Ok to proceed? (y) y
  Which Svelte app template? Skeleton project
  Add type checking with TypeScript? Yes, using TypeScript syntax
  Select additional options
    Add ESLint for code linting
    Add Prettier for code formatting

cd my-app
yarn install
```

### adapter

Install an adapter.

```bash
yarn add --dev @sveltejs/adapter-node
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
yarn run format
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
yarn run check
yarn run lint
```

```bash
cd src
deno fmt --check
deno lint
```

### run (dev)

```bash
yarn run dev --host --port 3000
```

### build

```bash
yarn run build
```

### run (prod)

```bash
node build/index.js
```

### links

- [svelte.dev](https://svelte.dev/)
- [sveltekit](https://kit.svelte.dev/)
- [adapter](https://kit.svelte.dev/docs#adapters)
