# React

Tested on `Debian 12 Bookworm`

### Packages

Install `nodejs`. See [nodejs](./nodejs.md).

Install `yarn`. See [yarn](./yarn.md).

### Create app

Run as `user`

```bash
mkdir -p ~/git-repo
cd ~/git-repo

yarn create vite my-app --template react-ts

cd my-app
yarn install
```

### Modules

```bash
yarn add -D prettier
```

### Config

In `.dockerignore`:

```
.git
build
dist
node_modules
Dockerfile
```

Update followings in `eslint.config.js`:

```
{ ignores: ['build', 'dist', 'node_modules'] },
```

Add the followings in `.gitignore`:

```
build
*~
```

Update followings in `index.html`:

```html
<link rel="icon" type="image/svg+xml" href="/vite.svg" />

<title>My App</title>

<script type="module" src="/src/index.tsx"></script>
```

Update and add the followings in `package.json`:

```
"name": "my-app",

"check": "prettier --check .",
"format": "prettier --write .",
"lint": "prettier --check . && eslint .",
```

In `.prettierignore`:

```
node_modules
build
dist
```

In `.prettierrc`:

```
{
  "semi": true,
  "singleQuote": true,
  "jsxSingleQuote": true,
  "trailingComma": "es5",
  "printWidth": 80,
  "useTabs": false,
  "tabWidth": 2,
  "arrowParens": "always",
  "endOfLine": "auto"
}
```

Use `tsconfig.app.json` as `tsconfig.json` for SPA:

```bash
mv tsconfig.app.json tsconfig.json
rm tsconfig.node.json
```

Add `base` into `vite.config.ts` if it will run in a subpath:

```
base: '/myapp',
```

`src/`:

```bash
mv src/main.tsx src/index.tsx
```

### Format

Format files

```bash
yarn run check
yarn run format
```

### Coomands

Install dependencies:

```bash
yarn install
```

Format checking:

```bash
yarn run check
```

Format:

```bash
yarn run format
```

Linter:

```bash
yarn run lint
```

Run in dev mode:

```bash
yarn run dev
```

Build:

```bash
yarn run build
```

Run in preview mode:

```bash
yarn run preview
```
