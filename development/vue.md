## Vue.js

#### purge old nodejs

```bash
apt-get purge nodejs

rm -rf /usr/lib/node_modules
rm -rf /usr/local/lib/node_modules
```

#### install nodejs

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

node --version
npm --version
```

#### npm update

DON'T upgrade or install!

```bash
npm update -g npm
npm --version
```

#### install vue-cli

```bash
npm install -g @vue/cli
npm install -g @vue/cli-service-global
npm install -g @vue/compiler-sfc

vue --version
```

#### create project

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

#### customize

```bash
cd proje-name
rm -rf .git                  # if it's already in a git repo
                             # compare .gitignore files
ln -s ../node_modules src/   # do this if the vue command will be used
                             # but npm seems more stable
```

#### run serve

```bash
cd project-name
npm run serve
```

#### lint

```bash
cd project-name
npm run lint
```

#### deployment

```bash
npm run build
cp -arp dist /var/www/html
```

#### upgrade app

```bash
vue upgrade
```
