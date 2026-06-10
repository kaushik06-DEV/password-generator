# Password Generator

A simple web-based password generator built with Python, Flask, HTML, and CSS. The application lets users generate strong random passwords by choosing the password length and the types of characters to include.

## Overview

This project is designed to generate secure passwords through a clean web interface. Users can choose whether the password should contain uppercase letters, lowercase letters, numbers, and special symbols. Based on the selected options, the Flask backend creates a random password and displays it on the page.

This project is useful for learning how to connect frontend form input with backend Python logic using Flask.

## Features

- Select password length
- Include uppercase letters
- Include lowercase letters
- Include numbers
- Include special symbols
- Generate passwords instantly
- Simple and clean interface

## Tech Stack

- Python
- Flask
- HTML
- CSS

## Project Structure

```bash
password-generator/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── README.md
└── requirements.txt
```

## File Details

- `app.py` - Main Flask application file with route handling and password generation logic
- `templates/index.html` - HTML template for the user interface
- `static/style.css` - CSS styling for the application
- `README.md` - Project documentation
- `requirements.txt` - Python dependencies required to run the project

## Installation

### Clone the repository

```bash
git clone https://github.com/kaushik06-DEV/password-generator.git
cd password-generator
```

### Create a virtual environment

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

On macOS or Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
python -m pip install flask
```

Or use:

```bash
pip install -r requirements.txt
```

`requirements.txt`

```txt
Flask
```

## Run the Application

```bash
python app.py
```

Then open this address in your browser:

```text
http://127.0.0.1:5000
```

## How It Works

1. The user opens the application in a browser.
2. The user enters the password length.
3. The user selects which character types to include.
4. The form is submitted to the Flask backend.
5. The backend creates a character pool based on the selected options.
6. A random password is generated from that pool.
7. The generated password is displayed on the webpage.

## Example

Sample input:

- Password length: 12
- Uppercase letters: Yes
- Lowercase letters: Yes
- Numbers: Yes
- Symbols: Yes

Sample output:

```text
T#8mQ!2zLp@4
```

## Learning Value

This project helps in understanding:

- Flask routing
- HTML form handling
- Backend and frontend integration
- Random string generation in Python
- Basic project structuring for Flask apps

## Future Improvements

- Copy password to clipboard
- Password strength indicator
- Responsive design improvements
- Dark mode
- Deploy the application online

## Author

Kaushik  
GitHub: https://github.com/kaushik06-DEV

## License

This project is licensed under the MIT License.
