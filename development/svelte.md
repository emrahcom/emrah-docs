## svelte

Tested on `Debian 11 Bullseye`

#### packages

```bash
apt-get --no-install-recommends install git patch
apt-get --no-install-recommends install npm
```

#### app folder

```bash
mkdir -p ~/git-repo
cd ~/git-repo

npx degit sveltejs/template myapp
cd myapp
node scripts/setupTypeScript.js
npm install
```

#### run

```bash
cd ~/git-repo/myapp
npm run dev
```

Edit `package.json` to listen all IPs

```
"start": "sirv public --no-clear --host",
```

#### links

- [svelte.dev](https://svelte.dev/)
