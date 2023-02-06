### Steps to view project deployed locally

1. Clone the repository
```
git clone https://github.com/Avikam03/atsni.git
```
2. `chmod +x ./install.sh ./run.sh`
3. `./install.sh` (this will install all the dependencies)
4. `./run.sh` (this will run two processes simultaneously - one that hosts the django server on port 8000, and another that is needed for tailwind to work)
5. Open `http://localhost:8000/` in your browser
6. Press `Ctrl + C` **twice** to stop the processes

Optional:
1. Create superuser to view admin panel
```
python manage.py createsuperuser
```


### Note:
1. The project starts by registering a user (preferably admin, to test all features)
2. To make things easy, you simply need the email address of an existing user to log into the account of a particular user. (password can be easily configured by making changes to the user model)
3. Since it was communicated that for the sake of this project there is only one team, it has been made so that all the users present are in the team, and when a member is added to the team, a user of their details is created.

### Testing 
Edge cases taken care of:
1. User can't delete themself
2. User can't set their own role to admin if they are a regular user
3. User can't change their own email or someone else's email to an email that already exists

### Screenshots
![](https://i.imgur.com/wPGoCie.png)
![](https://i.imgur.com/duM0vG8.png)
![](https://i.imgur.com/MeT407J.png)
![](https://i.imgur.com/Xz8A2T2.png)
![](https://i.imgur.com/dDqf4jc.png)