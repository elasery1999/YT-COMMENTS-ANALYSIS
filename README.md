# Welcome to YT-COMMENTS-ANALYSIS.

sentiment analysis on any youtube video’s comments

### Image from the project

![Image of Yaktocat](https://i.ibb.co/b7w8qbK/1.jpg)

### Setting up the project

1. Clone the repository <code>git clone https://github.com/elasery1999/YT-COMMENTS-ANALYSIS/</code>

2. Create your own virtual environment <code>python3 -m venv venv -> source venv/bin/activate</code>

3. Install your requirements <code>pip install -r requirements.txt</code>

7. Make your migrations <code>python manage.py migrate</code>

8. Create a new superuser <code>python manage.py createsuperuser</code>

5. Generate a new secret API key from Youtube API then add it to** <code>analysis/utlis.py</code>

9. Start the development server <code>python manage.py runserver</code>
