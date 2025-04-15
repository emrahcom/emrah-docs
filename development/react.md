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

In `eslint.config.js`:

```json
{ ignores: ['build', 'dist', 'node_modules'] },
```

In `.gitignore`:

```json
build
*~
```

In `.dockerignore`:

```
.git
build
dist
node_modules
Dockerfile
```

In `.prettierignore`:

```
node_modules
build
dist
```

In `.prettierrc`:

```json
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

In `index.html`:

```html
<link rel="icon" type="image/svg+xml" href="/vite.svg" />

<title>My App</title>

<script type="module" src="/src/index.tsx"></script>
```

