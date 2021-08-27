## svelte

Tested on `Debian 11 Bullseye`

#### packages

run as `root`

```bash
apt-get --no-install-recommends install git patch
apt-get --no-install-recommends install npm
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
  },
};

export default config;
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
```

#### links

- [svelte.dev](https://svelte.dev/)
- [sveltekit](https://kit.svelte.dev/)
- [adapter](https://kit.svelte.dev/docs#adapters)
