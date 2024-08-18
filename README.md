# AutoBooking
---
Python script that will auto book rooms at Dalhousie University
---

## Installation
### Step 1: Install Dependencies
#### Windows
```
pip install selenium webdriver-manager python-dotenv
```

#### macOS
WIP

#### (Optional) Run add user function to database
```
pip install supabase cryptography
```


### Step 2: Creat .env file
Create a new `.env` file at the root of the project
Copy variable from the `.env.template` and add your own variables by insert your own netID email and password

---

## Run Commands
At root folder, these commands can be run

### Book room G40I
`python main.py`

### Test Login Function
`python -m test_folder.test_login`

### Test Booking Function
`python -m roombooking.book_room.py`

### (Optional) run add user function
Un-comment `add_user(email, password)` at line 42
Then run
`python -m database.db_functions`
