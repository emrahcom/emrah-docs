## awscli

#### installation

```bash
apt-get install awscli
```

#### credentials

```bash
aws configure set aws_access_key_id "myid"
aws configure set aws_secret_access_key "mysecret"
aws configure set default.region "us-east-3"
```

#### S3

```bash
aws s3 ls s3://bucket
```
