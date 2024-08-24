# AutoBooking
Python script that will auto book rooms at Dalhousie University

## Pre-requisite
Doker desktop would need to be install to run the docker build.
If not, the normal `python` command can be run.

## Installation
### Step 1: Install Dependencies
#### Windows
```
pip install -r requirements.txt
```

#### macOS
WIP


### Step 2: Creat .env file
Create a new `.env` file at the root of the project
Copy variable from the `.env.template` and add your own variables by insert your own netID email and password

## Run Commands
At root folder, these commands can be run

### Option 1: Run with Docker
```
docker build -t autobooking .
docker run -e EMAIL=<your_email@example.com> -e PASSWORD=,your_password> -e TIME_BLOCK_ASSIGNED=<your_assigned_timeblock> autobooking
```

### Option 2: Run with Python
```
python -m main
```
