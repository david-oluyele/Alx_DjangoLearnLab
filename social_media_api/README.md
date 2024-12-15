
# Social Media API

This project is a Social Media API built using Django and Django REST Framework (DRF). It focuses on user authentication, including registration, login, and token-based authentication.

## Features

- **Custom User Model**:
  - `bio`: A text field for the user's biography.
  - `profile_picture`: An image field for the user's profile picture.
  - `followers`: A ManyToMany field allowing users to follow each other (asymmetrical).

- **Authentication System**:
  - Token-based authentication using DRF's `rest_framework.authtoken`.

- **Endpoints**:
  - User registration (`/accounts/register/`)
  - User login (`/accounts/login/`)

## API Usage

### 1. User Registration
- **Endpoint**: `/accounts/register/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "example_user",
      "email": "user@example.com",
      "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
      "token": "generated_token_here"
  }
  ```

### 2. User Login
- **Endpoint**: `/accounts/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "example_user",
      "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
      "token": "generated_token_here"
  }
  ```

## Overview of the User Model

The custom user model extends Django's `AbstractUser` class with the following additional fields:
- `bio`: Allows users to add a short biography.
- `profile_picture`: Lets users upload a profile picture.
- `followers`: Tracks the users who follow this user, implemented as a self-referential ManyToMany field.

The model supports flexible user management and is configured in `settings.py` using:
```python
AUTH_USER_MODEL = 'accounts.CustomUser'
```

## Contributors

- Your Name (your_email@example.com)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
