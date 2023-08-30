# container-cost-calculator
Hackathon Resources for Container Cost Calculator 

### Templates 

Contains HTML templates for rendering webpages with flask 

### Calculator

Contains Helm Chart for Deploying Calculator on Kubernetes 

### Modules 

#### Import Prices 

    Contains import prices function to read in from yaml file and return prices etc.

#### Webhelper 

    Contains get functions to return formatted prices and costs

### Running locally

##### Standalone app 

```BASH
python -m flask run -h <host_ip> -p <port>
```

##### Docker Container 

```BASH
#Build Container
docker build -t container-cost-calculator .

#Run Container 
docker run container-cost-calculator -p <container_port>:<host_port>
```

Can also be deployed as a helm chart (work in progress)




