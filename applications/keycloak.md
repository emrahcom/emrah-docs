# Keycloak

## Redirecting

Redirecting to `Keycloak` auth service to get a short-term authorization code.

```bash
KEYCLOAK_ORIGIN="https://ucs-sso-ng.mydomain.corp"
KEYCLOAK_REALM="ucs"
KEYCLOAK_CLIENT_ID=jitsi
REDIRECT_URI="https://jitsi.mydomain.corp/hello"

KEYCLOAK_AUTH_URI="$KEYCLOAK_ORIGIN/realms/$KEYCLOAK_REALM\
/protocol/openid-connect/auth?client_id=$KEYCLOAK_CLIENT_ID\
&response_mode=query&response_type=code&scope=openid\
&prompt=login&redirect_uri=$REDIRECT_URI"

chromium $KEYCLOAK_AUTH_URI
```

## Response after the authentication

`Kecyloak` redirects the user to `REDIRECT_URI` with the followings after
authentication:

- `session_state`
- `code`

e.g.

`https://jitsi.mydomain.corp/hello?session_state=a6c...d0c&code=100...656`

## Getting the token

Getting the long-term token by using the authorization code.

_Use the same `$REDIRECT_URI` otherwise the request will be rejected._

```bash
KEYCLOAK_ORIGIN="https://ucs-sso-ng.mydomain.corp"
KEYCLOAK_REALM="ucs"
KEYCLOAK_CLIENT_ID=jitsi
REDIRECT_URI="https://jitsi.mydomain.corp/hello"

KEYCLOAK_TOKEN_URI="$KEYCLOAK_ORIGIN/realms/$KEYCLOAK_REALM\
/protocol/openid-connect/token"

CODE="100...656"

DATA="client_id=$KEYCLOAK_CLIENT_ID\
&grant_type=authorization_code\
&redirect_uri=$REDIRECT_URI\
&code=$CODE"

curl $KEYCLOAK_TOKEN_URI \
  --header "Accept: application/json" \
  -X POST --data "$DATA"
```

Response will contain the followings:

- `access_token`
- `scope`
- `token_type`
- `expires_in`
- ...

## User Info

Getting `UserInfo` by using `access_token`.

```bash
KEYCLOAK_ORIGIN="https://ucs-sso-ng.mydomain.corp"
KEYCLOAK_REALM="ucs"
ACCESS_TOKEN="eyJhb...8B6Jy_Q"

KEYCLOAK_INFO_URI="$KEYCLOAK_ORIGIN/realms/$KEYCLOAK_REALM\
/protocol/openid-connect/userinfo"

curl $KEYCLOAK_INFO_URI \
  --header "Accept: application/json" \
  --header "Authorization: Bearer $ACCESS_TOKEN"
```

Response will contain the followings:

- `sub`
- `preferred_username`
- ...
