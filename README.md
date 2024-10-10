# Store Hub

## Description

This project is a Django web application that allows users to manage products and orders. It includes user authentication, product creation, and order management features.

## Features

- User authentication (login/logout)
- Product listing
- Category listing
- Add new products (only for authenticated users)
- Create and manage orders (only for authenticated users)

## Technologies Used

- **Backend**: Django 5.1
- **Database**: PostgresSQL
- **Frontend**: HTML, CSS
- **Version Control**: Git
- **Containerization**: Docker

## Installation

To set up this project locally, follow these steps:

### Clone the repository With SSH:

   ```bash
   git clone git@github.com:ILIAEVI/storehub.git
   ```

### Configure .env.example

### How to Run
Firstly, start docker, then run following commands.
   ```
   pip install -r requirements.txt
   docker-compose up -d --build
   python manage.py makemigrations
   python manage.py migrate
   
   python manage.py createsuperuser
   
   python manage.py runserver
   
   ```