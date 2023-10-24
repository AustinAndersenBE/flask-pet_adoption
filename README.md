# Pet Adoption Agency

## Introduction

This is a simple web application built using Flask, SQLAlchemy, and WTForms. It allows users to view, add, and edit pets for adoption.

## Features

- List all available pets
- Add a new pet
- Edit an existing pet

## Installation

1. Clone this repository:
    ```bash
    git clone <repository_url>
    ```
2. Navigate into the project folder:
    ```bash
    cd <project_folder>
    ```
3. Create a virtual environment (optional but recommended):
    ```bash
    python3.7 -m venv venv
    ```
4. Activate the virtual environment:
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        .\venv\Scripts\Activate
        ```
5. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Initialize the database:
    ```bash
    python
    >>> from app import create_database
    >>> create_database()
    ```

2. Run the Flask application:
    ```bash
    flask run
    ```

Visit `http://127.0.0.1:5000/` in your web browser to interact with the application.

## Dependencies

- Flask
- Flask-SQLAlchemy
- Flask-WTF
- WTForms
- psycopg2-binary
