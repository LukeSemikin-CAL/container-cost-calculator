apiVersion: apps/v1
kind: deployment 
metadata:
  name: {{ .Values.app_name }}
  labels: 
   language: python 
   app: Flask 
spec:
  replicas: 0
  selector:
    matchLabels:
      app: Flask 
  template:
    metadata:
      labels:
        app: Flask 
    spec:
      containers:
        - name: {{ .Values.app_name }}
          image: {{ .Values.image_name }}
  

