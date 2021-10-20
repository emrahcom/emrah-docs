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
git pull upstream master
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
git switch master
git branch -d fix-my-branch
```

- Delete remote branch

```bash
git push origin --delete fix-my-branch
```
