# Articles-platform
Want to keep up to date with all the latest news? This web-application Articles Platform can be your perfect source. On Articles platform people share everything: from weather in their region to what is the economy in other countries. The platform enables you not only to view, but also create articles and drop a comment on articles (if you have registered, of course). 

# Features
-User registration and authorization 
-Creating articles 
-Leaving comments
-View profiles of users
-Liking articles
-displaying number of views and likes of the article.

#Installation 
1. Clone repository:
   git clone https://github.com/Alexandr7466/Articles-platform
2. Navigate to project folder:
   cd Articlesplatform
3. Create virtual environment: 
   python -m venv venv
4. Activate it:
   venv\Scripts\activate
5. Apply migrations:
   python manage.py migrate
6. Run the server:
   python manage.py runserver

# Tech Stack
- Python
- Django
- SQLite
- HTML
- CSS
- Django templates

#Now on the website:
1. Click on your nickname to view your profile. 
2. If you have not registered yet, click on yellow text "logged in" to either log in or register. 
3. After logging in or creating an account, a grey plus button will appear to the left of the inscription "Create article". Press on it to create a new article.
4. While creating, you must come up with title and main content of your article. Also, if you wish, you can download a picture for your article. After filling out all info, click on "Create Article" button.
5. Created articles can be viewed on the main page and your profile page.
6. Click on any article to read it or leave a comment below it.
7. Like article by clicking on the like button below.
8. Visit profiles of different authors by clicking on their nicknames to the left of the article title or in comments.
9. Delete your articles by clicking on trash can to the left of the title.
10. Use "Go back", "Back to all articles" and "Return to main page" buttons to go to the main page or profile.
11. By clicking on "Logout" button which is to the left of your nickname on your profile page, you are logging out of your curent account. 

#ER-scheme:
