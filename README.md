### Steps to view project deployed locally

1. Clone the repository
```
git clone https://github.com/Avikam03/atsni.git
```
2. `$ python3 manage.py makemigrations`
3. `$ python3 manage.py migrate`
4. `$ python3 manage.py runserver`
5. Open `http://localhost:8000/` in your browser


### Note:
1. There is no proper mode of authentication for the project. You simply need the email address of an existin guser to log into the account of that user.
2. You have to start by registering a user.

### Testing 
Edge cases taken care of:
1. User can't delete their own 