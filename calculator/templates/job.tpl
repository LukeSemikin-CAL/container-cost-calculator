apiVersion: batch/v1
kind: Job
metadata:
  name: Expose-App
  annotations:
    "helm.sh/hook": pre-delete, post-install
    "helm.sh/hook-weight": "1"
    "helm.sh/hook-delete-policy": hook-succeeded
spec: 
  template:
    metadata:
      name: Expose Pod 
      labels:
        app: Flask 
    spec: 
      containers:
        - name: kubectl
          image: "k8s.gcr.io/hyperkube:v1.12.1"
          imagePullPolicy: "IfNotPresent"
          command:
            - /bin/sh
            - -c 
            - >
              kubectl expose deployment {{ .Values.app_name }} --name={{ .Values.app_name }}-service --type=LoadBalancer --port 18500 --target-port 5000