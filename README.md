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
1. The project starts by registering a user (preferably admin, to test all features)
2. To make things easy, you simply need the email address of an existing user to log into the account of a particular user. (password can be easily configured by making changes to the user model)
3. Since it was communicated that for the sake of this project there is only one team, it has been made so that all the users present are in the team, and when a member is added to the team, a user of their details is created.

### Testing 
Edge cases taken care of:
1. User can't delete themself
2. User can't set their own role to admin if they are a regular user

### Screenshots
![](https://i.imgur.com/wPGoCie.png)
![](https://i.imgur.com/duM0vG8.png)
![](https://i.imgur.com/MeT407J.png)
![](https://i.imgur.com/Xz8A2T2.png)
![](https://i.imgur.com/dDqf4jc.png)