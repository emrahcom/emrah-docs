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
    >>/etc/apt/sources.list

apt-get update
apt-get install nodejs
```

#### app folder

run as `user`

```bash
mkdir -p ~/git-repo
cd ~/git-repo

npm init svelte@next myapp
  Ok to proceed? (y) y
  Which Svelte app template?
    Skeleton project
  Use TypeScript? Yes
  Add ESLint for code linting? Yes
  Add Prettier for code formatting? Yes

cd myapp
npm install
```

#### .gitignore

Edit `.gitignore`

```config
*~
*.sw?
*.log
.DS_Store
node_modules
package-lock.json
/build
/.svelte-kit
/package
.env
.env.*
!.env.example
```

#### run

```bash
npm run dev -- --host --port 3000
```

#### adapter

Install an adapter before building.

```bash
npm install @sveltejs/adapter-static@next --save-dev
```

Edit `svelte.config.js`

```javascript
//import adapter from '@sveltejs/adapter-auto';
import adapter from "@sveltejs/adapter-static";
import preprocess from "svelte-preprocess";

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // Consult https://github.com/sveltejs/svelte-preprocess
  // for more information about preprocessors
  preprocess: preprocess(),

  kit: {
    adapter: adapter(),

    files: {
      lib: "src/lib",
    },
  },
};

export default config;
```

Edit src/hooks.ts

```javascript
/** @type {import('@sveltejs/kit').Handle} */
export async function handle({ event, resolve }) {
  const response = await resolve(event, {
    ssr: false,
  });

  return response;
}
```

#### package.json

Don't use default `prettier` format.

```json
{
  ...
  "scripts": {
    ...
    "lint": "eslint --ignore-path .gitignore .",
    "prettier": "prettier --ignore-path .gitignore  --check --plugin-search-dir=. .",
    "format": "prettier --ignore-path .gitignore  --write --plugin-search-dir=. .",
    ...
  }
  ...
}
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

#### build

```bash
npm run build
```

#### preview

```bash
npm run preview -- --host --port 3000
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

#### links

- [svelte.dev](https://svelte.dev/)
- [sveltekit](https://kit.svelte.dev/)
- [adapter](https://kit.svelte.dev/docs#adapters)
