# oathtool

### install

```bash
apt-get install oathtool
```

### 2fa.conf

```
github="github_key"
google="google_key"
...
```

### 2fa.sh

```bash
#!/usr/bin/bash
set -e

# -----------------------------------------------------------------------------
# Dependencies:
#   apt-get install oathtool
#
# Usage:
#   2fa key_name
# -----------------------------------------------------------------------------

REALLINK=$(readlink -f "$0")
BASEDIR=$(dirname "$REALLINK")
source "$BASEDIR/2fa.conf"

KEY_NAME="$1"
if [ -z "$KEY_NAME" ]; then
    echo "missing key"
    exit 1
fi

KEY_VALUE="${!KEY_NAME}"
if [ -z "$KEY_VALUE" ]; then
    echo "invalid key"
    exit 1
fi

oathtool --base32 --totp "$KEY_VALUE"
```

### permissions

```bash
chmod 700 folder
chmod 600 2fa.conf
chmod 700 2fa.sh
```

### Link

```bash
cd ~/bin
ln -s path/2fa.sh 2fa
```
