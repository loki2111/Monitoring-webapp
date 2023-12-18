# **Cloud Native Resource Monitoring Python App on K8s!(eks-cluster)**

# Monitoring-webapp
**CPU-Memory Monitoring Web application-Python based
**
Prerequisites:
1. AWS Account.
2. Programmatic access and AWS configured with CLI: Create Access key secrete key from IAM roles  Open CMD and run command aws configure and Access key secrete key, region. Run command aws iam list-users to list users configured on system. Awscli should be latest so install and upgrade it: sudo apt upgrade awscli
3. Python3 Installed.
4. Docker and Kubectl installed.
5. Code editor (Vscode)

## **App Development:
Create Application using psutil, flask and UI using HTML.

## **Part 1: Deploying the Flask application locally**
1. Create EC2 Instance (redhat or debian based).
2. Configure AWS CLI. awscli should have latest version so install and check for update and upgrade it.
```
sudo apt install awscli -y
sudo apt update -y
sudo apt upgrade awscli
```
3. If you are not able to install v2 awscli using above command then follow following way.
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip“
unzip awscliv2.zip
sudo ./aws/install
```

### **Step 2: Clone the code**

Clone the code from the repository:

```
git clone <repository_url>
```

### **Step 3: Install dependencies**

The application uses the **`psutil`** and **`Flask`, Plotly, boto3** libraries. Install them using pip:

```
pip3 install -r requirements.txt
```

## **ECR: We will create ECR using Python automation.
1. Create ECR Manually:  awscli should be configured first. Awscli should be latest so install and upgrade it: sudo apt upgrade awscli
2. Select private or public = Name of repository = done.
3. Automate using python: Using boto3 library. ( Check boto3 website and search for aws ecr) (https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#client) Create repository.


### **Step 3: Run the application**

To run the application, navigate to the root directory of the project and execute the following command:

```
python3 app.py
```
This will start the Flask server on **`ip:5000`**. Navigate to on your browser to access the application.


## **Part 2: Dockerizing the Flask application**
### **Step 1: Create a Dockerfile**

Create a **`Dockerfile`** in the root directory of the project with the following contents:

```
# Use the official Python image as the base image
FROM python:3.9
# Set the working directory in the container
WORKDIR /app
# Copy the requirements file to the working directory
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
# Copy the application code to the working directory
COPY . .
# Set the environment variables for the Flask app
ENV FLASK_RUN_HOST=0.0.0.0
# Expose the port on which the Flask app will run
EXPOSE 5000
# Start the Flask app when the container is run
CMD ["flask", "run"]
```

### **Step 2: Build the Docker image**

To build the Docker image, execute the following command: Image name should in this format so it will be easy while pushing into repository <dockerusername/image_name:v>

```
docker build -t <image_name> .
```


### **Step 3: Run the Docker container**

To run the Docker container, execute the following command:

```
docker run -p 5000:5000 <image_name>
```

This will start the Flask server in a Docker container on you system IP:5000

## **Part 3: Pushing the Docker image to ECR**

### **Step 1: Create an ECR repository**

Create an ECR repository using Python:

```
import boto3

# Create an ECR client
ecr_client = boto3.client('ecr')

# Create a new ECR repository
repository_name = 'my-ecr-repo'
response = ecr_client.create_repository(repositoryName=repository_name)

# Print the repository URI
repository_uri = response['repository']['repositoryUri']
print(repository_uri)
```

### **Step 2: Push the Docker image to ECR**

Push the Docker image to ECR using the push commands on the console:

```
docker push <ecr_repo_uri>:<tag>
```

## **Part 4: Creating an EKS cluster and deploying the app using Python**

### **Step 1: Create an EKS cluster**

Create an EKS cluster and add node group

### **EKS Cluster: Requirements**
1. AWS account with Admin privileges or specific privileges as requirements.
2. AWS CLI access to kubectl utility. Awscli should be latest so install and upgrade it: sudo apt upgrade awscli
3. Instance (to manage cluster using kubectl)

### **Step 2: Create a node group**
Create a node group in the EKS cluster.

### **Kubectl Installation:**
1. kubectl version --client
2. curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.28.3/2023-11-14/bin/linux/amd64/kubectl
3. chmod +x ./kubectl
4. mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH
5. kubectl version --client
6. aws eks update-kubeconfig --region region-code --name <eks-cluster-name>

### **Step 3: Create deployment and service**
eks.py file present in repo contains deployment and service.

### **Deploy application using python or manual manifest files:**
make sure to edit the name of the image with your image Uri.

Once you run this file by running “python3 eks.py” deployment and service will be created.
Check by running following commands:
kubectl get deployment -n default (check deployments)
kubectl get service -n default (check service)
kubectl get pods -n default (to check the pods)

### **If you face issue in deployment:**
Use following commands:
```
kubectl describe deploy <deployement-name>
#This will give you detailed information of deployment where you can find the reason of failure.
#like this you can use this command for replicaset pods.
kubectl describe rs <replicaset-name>
kubectl describe po <pod-name>
```
