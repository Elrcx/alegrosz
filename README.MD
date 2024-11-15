# Alegrosz

## Description

Alegrosz is a simple training repository for learning Django. This project was developed as a practice environment to explore Django's core functionalities, including models, views, forms, and templates, along with integration of Bootstrap for styling.

This application was made as part of **CodersLab Python Course**.

## Features

- **Django Forms and Views**:
  - Use of Django forms, generic views, and `crispy-forms` for form rendering.
  - Contact form model with integration into the Django Admin interface.
- **Product Management**:
  - Basic product models with associated admin configurations and views for displaying product information.
- **Bootstrap Integration**:
  - Responsive design using Bootstrap's grid system and basic styling for images.
- **Django Template Setup**:
  - Configured templates with a basic setup for rendering pages.
- **Environment Configuration**:
  - Database configuration using environment variables for enhanced security and flexibility.

## Installation

To run the project locally, ensure you have Python and Django installed. Follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Elrcx/alegrosz.git
   cd alegrosz
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure the environment variables for the database connection.
4. Run the server:
   ```bash
   python manage.py runserver
   ```

## License

Licensed under the [MIT License](https://en.wikipedia.org/wiki/MIT_License).



## Algorytm tworzenia funkcjonalności w django

1. Czy potrzebne nowe django apps?
   - `django-admin startapp <name>`
   - rejestruje w settings.py -> INSTALLED_APPS
2. Czy potrzebne dane?
   - tworzę model w `<appname>/models.py`
   - `python manage.py makemigrations <app_label>`
   - `python manage.py migrate <app_label>`
3. Czy potrzebuję obsługę w CMS (Django Admin)?
   - rejestruję modele w `<app_name>/admin.py`
4. Czy potrzebuje pobierać dane od użytkownika?
   - tworzę `forms.py`
   - tworze klasę formularza
5. Czy potrzebna jest logika? (View)
   - `<app_name>/views.py`
6. Czy potrzebny jest routing?
