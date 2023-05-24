# DoiNK Shippers - Food Delivery App

DoiNK Shippers is a food delivery app developed by students, for students. It aims to provide a convenient and efficient way for students to order food from local restaurants and have it delivered to their doorstep.

## Features

- Browse through a variety of restaurants and their menus.
- Place orders and track their status in real-time.
- Secure OTP-based order verification through email using Sendinblue API.
- User-friendly interface for easy navigation and ordering.
- Developed using the Django framework.

## Installation

To set up and run DoiNK Shippers on your local machine, follow these steps:

### Prerequisites

Make sure you have the following installed on your system:

- Python (version 3.6 or higher)
- pipenv (if not already installed, run the below command:)
```bash
pip install pipenv
```

### Clone the repository

```bash
git clone https://github.com/S/DoiNk-Shippers.git
```

### Set up the virtual environment

```bash
pipenv install
```

### Activate the virtual environment

```bash
pipenv shell
```

### Install dependencies

```bash
pipenv install django
```

## Accessing the App

### Run the Django Server

Run the Django Server with the command below:
```bash
python manage.py runserver
```

### Accessing the Server

Open your web browser and visit http://localhost:8000 to access the DoiNK Shippers app. 💻

## Project Structure

`index.html` - Home page of the app.
`settings.py` - Django settings file.
`manage.py` - Django management script.
`DoiNKShippers/` - Django app directory containing the main project code.

## Configuration

DoiNK Shippers uses a temporary link for Stripe API and Sendinblue API for OTP-based order verification through email. No additional configuration or API keys are required. 🔒

## Contributing

We welcome contributions from everyone! If you find any issues or have suggestions for improvement, please fork the repository and submit a pull request. 🚀

## Contact
If you have any questions or inquiries, please contact us at doinkshippers@example.com. ✉️

#### With Love❤️ and Caffeine☕️ from - highOnCaffeine! ❤️☕️

