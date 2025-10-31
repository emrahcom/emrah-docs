## GNUPG
GnuPG  is  a  set  of programs for public key encryption and digital signatures.

#### Package

```bash
apt-get install gnupg
```

#### Generating key

```bash
gpg --full-generate-key
  Key type: (1) RSA and RSA
  Key size: 4096
  Expire time: 0
  Real name: emrah
  Email: hello@emrah.com
  Comment:
  Okay

  Passphrase:
```

#### List keys

```bash
gpg --list-keys --keyid-format LONG

>>> pub   rsa4096/21BD2878787A63C9 2025-10-31 [SC]
>>>       C5D9E95232BF9A9A9A9A9A9A9ABD2CD87A9A63C9
>>> uid                 [ultimate] emrah <hello@emrah.com>
>>> sub   rsa4096/D2B9868686867A7D 2025-10-31 [E]
```

#### Publish public key

```bash
gpg --keyserver hkps://keys.openpgp.org --send-keys 21BD2878787A63C9
```

#### Validate public key

```bash
gpg --keyserver hkps://keys.openpgp.org --recv-keys 21BD2878787A63C9
```

#### Delete a key

```bash
gpg --delete-secret-keys 'hello@emrah.com'
gpg --delete-keys 'hello@emrah.com'
```
