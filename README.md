# AutoBooking
Python script that will auto book rooms at University

## Pre-requisite
Doker desktop would need to be install to run the docker build.
If not, the normal `python` command can be run.
(Optional): Install AWS CLI to upload to AWS.

## Installation
### Step 1: Install Dependencies
#### Windows
```bash
pip install -r requirements.txt
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux
```bash
pip install -r requirements.txt
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Creat .env file
Create a new `.env` file at the root of the project
Copy variable from the `.env.template` and add your own variables by insert your own netID email and password.
This would allow you to run with `python` but would not be necessary when run using Docker

## Run Commands
At root folder, these commands can be run

### Option 1: Run with Docker
Choose platfrom is linux/amd64 for your compute platform.
```bash
docker build --platform linux/amd64 -t autobooking .
docker run -e EMAIL=<your_email@example.com> -e PASSWORD=<your_password> -e TIME_BLOCK_ASSIGNED=<your_assigned_timeblock> autobooking
```

### Option 2: Run with Python
```bash
python -m main
```

## Schedule Run with AWS

### Pre-requisite
- Install AWS CLI on your local computer.
- Login to AWS CLI with `aws configure`.
- Create a repo in your AWS account region in ECR with the repo named `docker images`.

### Step 1: Upload Container to ECR

```bash
docker build --platform linux/amd64 -t killambooking . 

docker tag killambooking <aws account id>.dkr.ecr.<your aws region>.amazonaws.com/docker-images:v1.0.0

aws ecr get-login-password --region <your aws region> | docker login --username AWS --password-stdin <amazon account id>.dkr.ecr.<your aws region>.amazonaws.com/docker-images

docker push <amazon account id>.dkr.ecr.<your aws region>.amazonaws.com/docker-images:v1.0.0
```

### Step 2: Run Docker images with ECS
Choose linux/x86 for your compute platform.

Using the AWS Console, run the Docker Image just uploaded with the added enviroment variables.
- Add the following enviroment variables to the ECS task:
  - EMAIL
  - PASSWORD
  - TIME_BLOCK_ASSIGNED

### Step 3: Add CRON Job to ECS
- Add schedule run to your ECS group using CRON.