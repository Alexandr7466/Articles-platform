# Articles-platform
Want to keep up to date with all the latest news? This web-application Articles Platform can be your perfect source. On Articles platform people share everything: from weather in their region to what is the economy in other countries. The platform enables you not only to view, but also create articles and drop a comment on articles (if you have registered, of course). 

# Features
-User registration and authorization 
-Creating articles 
-Leaving comments
-View profiles of users

#Installation 
1. Clone repository:
   git clone https://github.com/Alexandr7466/Articles-platform
2. Navigate to project folder:
   cd Articlesplatform
3. Create virtual environment: 
   python -m venv venv
4. Activate it:
   venv\Scripts\activate
5. Install dependencies:
   pip install -r requirements.txt
6. Apply migrations:
   python manage.py migrate
7. Run the server:
   python manage.py runserver
