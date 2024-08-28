# Technicians Hub

## Overview
Technicians Hub is an innovative web application that serves as a bridge between users and skilled technicians across a variety of trades including electricians, carpenters, plumbers, smiths, bricklayers, and maids. This platform facilitates seamless interaction by allowing users to conveniently book appointments and manage sessions with professionals based on their specific service needs. Each technician profile includes detailed information on skills, past work, and user reviews, ensuring transparency and trust. Whether you need urgent repairs, routine maintenance, or skilled labor for a special project, Technicians Hub provides a reliable, user-friendly solution.

## Features
- **User Registration and Authentication**: Users can sign up and log into the application with secure authentication measures in place, ensuring that user data is kept private and secure.
  
- **Technician Management**: Technicians are added to the platform exclusively by administrators, ensuring a curated and reliable listing. For each technician, the admin can input essential details such as first name, last name, bio, phone number, city, and age. This comprehensive profiling helps in maintaining a high-quality database of technicians, providing users with valuable information to aid their selection process.

- **Booking System**: Users can easily book appointments with technicians through a user-friendly interface. The system allows users to select the type of service, choose available times, and manage their appointments with options to update or cancel as needed. This feature ensures flexibility and convenience, adapting to the dynamic schedules of both users and technicians.

- **Appointment Notifications**: Whenever a user books, updates, or cancels an appointment, the system automatically sends an email notification to their registered email address. This ensures that users are always informed about the status of their appointments and any changes.

- **Review System**: Users have the freedom to leave reviews for technicians at any time, allowing them to share insights and experiences directly related to the technicians’ profiles and skills. Moreover, users can update or delete their reviews to reflect their current opinions, ensuring that the feedback remains relevant and accurate over time.

- **Responsive Design**: The application is fully responsive and provides a seamless experience across various devices and screen sizes, ensuring accessibility and ease of use anytime, anywhere.

## Technologies Used

- **Django**: Used as the primary web framework for building the backend of the application. Django is chosen for its robustness, scalability, and ease of integrating with various databases and third-party libraries.
- **Python**: The core programming language used in conjunction with Django to handle logic, data processing, and server-side scripting.
- **MySQL**: The chosen database for production due to its performance, reliability, and support for complex queries. Ideal for handling the extensive data needs of Technicians Hub.
- **JavaScript**: Utilized to enhance interactivity on the client side, including form validations and dynamic content updates.
- **HTML and CSS**: Employed for structuring and styling the frontend of the application, ensuring it is responsive and user-friendly across different devices and browsers.
- **Bootstrap**: A front-end framework used for developing responsive and mobile-first web pages.
 - **SMTP Library/Email Integration (Mailjet)**: Utilizes Mailjet to send real-time notifications and updates to users about their appointments. Mailjet provides robust email delivery and management capabilities, ensuring reliable communication through SMTP protocols and easy integration into our system.
- **Git**: Used for version control to manage the codebase and track changes, facilitating collaboration among developers.

## Installation

Follow these steps to set up the Technicians Hub project on your local machine.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.6.4**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Virtualenv**: Install via pip if you don't have it:
  ```bash
  pip install virtualenv

### Steps to Set Up the Project
# Clone the Repository
git clone https://github.com/talakh1798/Technicians-Hub.git

# Navigate to the Project Directory
cd Technicians-Hub

# Set Up the Virtual Environment
# On macOS/Linux
python3 -m venv env
source env/bin/activate

# On Windows
# python -m venv env
# env\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Run Database Migrations
python manage.py migrate

# Running the Application
python manage.py runserver



## Website Images

![Home page Screenshot](https://github.com/user-attachments/assets/b4e24ced-7be8-4771-b58b-5c682c6d868a?raw=true)
![Login Dashboard Screenshot](https://github.com/user-attachments/assets/8f3cb58d-7fb6-42f7-9e64-3b902faf52a9?raw=true)
![Sign Up Dashboard Screenshot](https://github.com/user-attachments/assets/a165016e-a069-43e1-bc12-c20205443129?raw=true)
![Services Dashboard Screenshot](https://github.com/user-attachments/assets/470debfd-9be4-4beb-b304-c15e92782a1c?raw=true)
![Services Categories Screenshot](https://github.com/user-attachments/assets/77b1c165-d87f-41c4-acee-ea7679f1ba6b?raw=true)
![Technicians Screenshot](https://github.com/user-attachments/assets/c8c1b3f7-f255-4821-8850-3b82eac0a14b?raw=true)


















