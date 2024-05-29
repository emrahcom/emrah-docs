{{- define "keycloak.name-app" -}}
{{- printf "%s-keycloak" .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "keycloak.name-pvc" -}}
{{- printf "%s-keycloak-pvc" .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
