# firstDjangoDatabase
ITC assignment
Saksham Gupta
20D170037

This is the repository for task 1.
Unfortunately, Task 2 and bonus was not able to be completed, and thus was not added.

This django project has two apps:
1) The ITSP app which contains the html templates and the database
2) The REST API, which is connected to ITSP database and is able to alter it

The database used is sqlite as the number of entries are small and it was mainly used for testing the app.
It can be changed in the future.
The database has three elements: team_name, team_id(this is primary key) and team_members(supposed to have member names with comma separation)

*These are the instructions on how to use the app after migrating the whole project and running it on a local liveserver

The homepage opens the ITSP app at local(http://127.0.0.1:8000/) and displays all the team names of all the teams in the database.
Clicking on them leads you to a dynamic url http://127.0.0.1:8000/<team_id> which displays the info of the team with that team_id
The ITSP app has bootstrap integrated, as is evident by the navbar, but due to it being a backend project, not a lot of designing has been done.

The Rest API is loaded at http://127.0.0.1:8000/API, and accesses the same database as the ITSP app. 
It can be used to add and remove the same data

Login details for superuser are as follows:(to be entered at http://127.0.0.1:8000/admin)
username : admin
password : admin

set a superuser if one has not been set...

This should cover all subtasks of Task1
This was my first experience with django, and it took me lots of tutorials and videos to get through this.
Also, it is my first time writing a proper ReadME, so it might be lacking, sorry for that ...




