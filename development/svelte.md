## svelte

Tested on `Debian 11 Bullseye`

#### packages

run as `root`

```bash
apt-get install gnupg git build-essential

curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -
echo "deb https://deb.nodesource.com/node_16.x bullseye main" > \
    /etc/apt/sources.list.d/nodesource.list

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
/build
/.svelte-kit
/package
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
import preprocess from "svelte-preprocess";
import adapter from "@sveltejs/adapter-static";

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // Consult https://github.com/sveltejs/svelte-preprocess
  // for more information about preprocessors
  preprocess: preprocess(),

  kit: {
    // hydrate the <div id="svelte"> element in src/app.html
    target: "#svelte",
    adapter: adapter({
      // default options are shown
      pages: "build",
      assets: "build",
      fallback: null,
    }),
    files: {
      lib: "src/lib",
    },
    hydrate: true,
    ssr: false,
  },
};

export default config;
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

#### routes

Put pages inside `src/routes`

```bash
cat >src/routes/hello.svelte <<EOF
<h1>hello</h1>
EOF
```

Go to `http://ip-address:3000/hello`

#### layout

```html
<script lang="ts" context="module">
export async function load({page, fetch, session, context}) {
  try {
    const url = "https://kratos.mydomain.corp/sessions/whoami";
    const res = await fetch(url, {credentials: "include"})

    if (res.status != 200) throw new Error("no authorization");
  } catch {
    return {
      status: 302,
      redirect: "https://secureapp.mydomain.corp/auth/login"
    }
  }
}
</script>

<slot></slot>
```

#### links

- [svelte.dev](https://svelte.dev/)
- [sveltekit](https://kit.svelte.dev/)
- [adapter](https://kit.svelte.dev/docs#adapters)
