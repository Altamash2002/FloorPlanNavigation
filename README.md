# Indoor Navigation System - Lokmanya Tilak College of Engineering

An indoor navigation system built for **Lokmanya Tilak College of Engineering** that helps users navigate the campus with ease, from the main gate to any destination within the college building and surrounding areas. The project utilizes floor-specific navigation maps, helping users find their desired locations efficiently using real-time directions.

## Main Features

- **Real-time Navigation**: Helps users navigate through each floor of the college campus and its surroundings.
- **Interactive Floor Maps**: Dynamic SVG-based floor plans to guide users.
- **Searchable Locations**: Users can search for classrooms, departments, offices, and other facilities within the campus.
- **Floor-specific Navigation**: The system provides navigation for each floor, including facilities outside the main building.
- **User Authentication**: Register, log in, and save your navigation history for easy future access.
- **Admin Dashboard**: Administrators can upload and manage floor plans, including floor navigation details.
- **Tagging Locations**: Special tags to highlight important locations like the library, cafeteria, and more.
- **Responsive UI**: Clean and user-friendly interface built with HTML, CSS, and JavaScript.
- **Seamless Integration**: Uses **Python Django** for backend operations and **SVG** for floor mapping.

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: JavaScript, SVG, HTML, CSS
- **Database**: MongoDB
- **Others**: 
  - **ASGI** for handling asynchronous operations
  - **Pymongo** and **dnspython** for MongoDB integration

## Requirements

Below is the list of dependencies for this project. You can install them via `pip`:

```bash
asgiref==3.7.2
Django==4.1.13
djongo==1.3.6
dnspython==2.4.2
pymongo==3.12.3
pytz==2023.3.post1
sqlparse==0.2.4
typing_extensions==4.8.0
tzdata==2023.3


Getting Started
Follow the steps below to set up the project locally:

1. Clone the Repository
Clone the project to your local machine:

bash
Copy
[git clone https://github.com/Altamash2002/FloorPlanNavigation.git]

2. Set Up Virtual Environment
Create and activate a virtual environment:

bash
Copy
virtualenv env --no-site-packages
source env/bin/activate

3. Install Dependencies
Install the project dependencies:

bash
Copy
pip install -r requirements.txt

4. Database Configuration
Ensure that MongoDB is installed and running on your machine, then configure the database connection in settings.py:

python
Copy
DATABASES = {
    'default': {
        'ENGINE': 'djongo.db.backends.mongo',
        'NAME': 'db_name',  # Your database name here
        'CLIENT': {
            'host': 'mongodb://localhost:27017',  # MongoDB URI
        }
    }
}

5. Apply Migrations
Run the migrations to set up the database:

bash
Copy
python manage.py migrate

6. Create Superuser (Admin Account)
Create an admin user to access the Django admin panel:

bash
Copy
python manage.py createsuperuser

7. Make Migrations for the App
Generate any additional migrations for your app:

bash
Copy
python manage.py makemigrations

8. Migrate Again (if necessary)
Run the migrations again to apply any changes:

bash
Copy
python manage.py migrate

9. Start the Development Server
Start the development server:

bash
Copy
python manage.py runserver

Visit http://localhost:8000 in your browser to view the app.
```
Feel free to fork the repository and submit issues or pull requests for bug fixes, feature requests, or enhancements. Contributions are welcome!
