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
- **Database**: SQlite3
- **Frontend**: HTML, CSS
- **Version Control**: Git

## Installation

To set up this project locally, follow these steps:

### Clone the repository With SSH:

   ```bash
   git clone git@github.com:ILIAEVI/storehub.git
   ```

### Super User:
##### Email: giorgi@gmail.com
##### Password: admin

### How to Run
Firstly, start docker, then run following commands.
   ```
   pip install -r requirements.txt
   python manage.py migrate
   
   python manage.py runserver
   
   ```

### Endpoints:
- **GET** `' '`: Home Page
- **GET** `/contact/`
- **GET** `/store/categories/`: List all categories.
- **GET** `/store/categories/{category_id}/products/`: List products in a specific category
- **GET** `/store/product/{product_id}/`: Retrieve details of a specific product.
- **GET** `/order/checkout/`
- **GET** `/order/order_list/`