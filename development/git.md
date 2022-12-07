## git

#### github pull request

- Fork the repo using `GitHub` panel

- Clone the repo to the local machine

```bash
git clone ssh://git@github.com:22/emrahcom/forked-repo.git repo-emrah
```

- Create a new remote for the upstream repo

```
cd repo-emrah
git remote add upstream https://github.com/developer/repo.git
```

- Update the clone

```
#git pull upstream master
git pull upstream main
git push
```

- Create a new branch

```bash
git branch fix-my-branch
```

- Switch to the new branch

```bash
git switch fix-my-branch
```

- Edit the repo

- Add, commit

```bash
git status
git diff

git add -A
git commit -m 'fix: ...'
git push --set-upstream origin fix-my-branch
```

- Pull request

`Compare & pull request` on `GitHub` panel

- List all branches

```bash
git branch -a
```

- Delete local branch

```bash
#git switch master
git switch main
git branch -d fix-my-branch
```

- Delete remote branch

```bash
git push origin --delete fix-my-branch
```

#### Signed commit

##### GPG key

```bash
gpg --full-generate-key
  4 - RSA (sign only)
  4096
  0
  y
  Real name: <name>
  Email address: <the same e-mail which is in .gitconfig'
  Okay
  <passphrase>
```

##### Git config

```bash
gpg --list-secret-keys --keyid-format=long
  sec   rsa4096/<KEY> 2020-02-14 [SC]

git config --global user.signingkey <KEY>
git config --global commit.gpgsign true
```

##### Upload signed key to GitHub

```bash
gpg --armor --export <KEY>
```

- `Profile`
- `settings`
- `SSH and GPG keys`
- `New GPG key`
- Paste `gpg --armor --export` output

##### gpg tty

Add the following into `.zshrc` or `.bashrc`

```bash
export GPG_TTY=$(tty)
```
