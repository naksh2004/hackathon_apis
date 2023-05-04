# hackathon_apis
Download the zip file or code
cd to root folder
cd hackathonapp
python manage.py makemigrations hackathonapi
python manage.py migrate

Create superuser
python manage.py createsuperuser

then run the application
python manage.py runserver

Following are the urls for the website
1. Create hackathons :- "localhost xxxx/create-hackathons"
2. Listing of hackathons :- "localhost xxxx"
3. Register to a hackathon :-  "localhost xxxx/hackathons/<int:hackathon_id>/registrations/"
4. Make Submissions :- "localhost xxxx/submissions/"
5. Users should be able to list the hackathons they are enrolled to :- "localhost xxxx/enrolled-hackathons/"
6. Users should be able to view their submissions in the hackathon they were enrolled in :- "localhost xxxx/hackathons/<int:hackathon_id>/submissions/"



