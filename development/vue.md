# Vue.js

### packages

Install `nodejs` (_16.x or newer_). See [nodejs](./nodejs.md).

### install vue-cli

```bash
npm install -g @vue/cli
npm install -g @vue/cli-service-global
npm install -g @vue/compiler-sfc

vue --version
```

### create project

As `user`

```bash
vue create project-name
    > Manually select features
      > Choose Vue version
        > 3.x
      > Babel
      > TypeScript
      > Linter / Formatter
        > ESLint + Prettier
    > config in package.json
```

or

```bash
vue ui
chromium http://localhost:8000
```

### customize

```bash
cd proje-name
rm -rf .git                  # if it's already in a git repo
                             # compare .gitignore files
ln -s ../node_modules src/   # do this if the vue command will be used
                             # but npm seems more stable
```

### run serve

```bash
cd project-name
npm run serve
```

### lint

```bash
cd project-name
npm run lint
```

### deployment

```bash
npm run build
cp -arp dist /var/www/html
```

### upgrade app

```bash
vue upgrade
```
