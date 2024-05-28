{{- define "keycloak.name" -}}
{{- printf "%s-keycloak" .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
