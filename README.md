# Task Forge

Task Forge is a web-based project management application built with Django. It helps users create and manage projects, organize tasks, assign tasks to project members, track progress, and communicate through task comments.

## Features

### Authentication
- User registration
- User login and logout
- Django built-in authentication

### Project Management
- Create projects
- Edit project details
- Delete projects
- View project information
- Add project members
- Remove project members
- Project owner management

### Task Management
- Create tasks
- Edit tasks
- Delete tasks
- Assign tasks to project members
- Task status tracking
- Task priority levels
- Due dates
- Task detail pages

### Collaboration
- Add members to projects
- Assign tasks to project members
- Add comments to tasks
- View project members

### Dashboard
- Total project count
- Total task count
- Completed task count
- Project overview

### UI & Design
- Clean monochrome interface
- Responsive layout
- Mobile-friendly design
- Consistent card-based UI
- Hover and interaction effects

## Tech Stack

| Technology | Purpose |
|---|---|
| HTML5 | Frontend structure |
| CSS3 | Styling and responsive design |
| JavaScript | Frontend interactions |
| Django | Backend framework |
| SQLite | Database |
| Django Authentication | User authentication |

## Project Structure

```text
Task Forge/
│
├── manage.py
├── db.sqlite3
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── dashboard.html
│   │
│   ├── accounts/
│   │   ├── login.html
│   │   └── register.html
│   │
│   ├── projects/
│   │   ├── create_project.html
│   │   ├── edit_project.html
│   │   └── project_detail.html
│   │
│   └── tasks/
│       ├── create_task.html
│       ├── edit_task.html
│       └── task_detail.html
│
├── accounts/
├── core/
├── taskforge/
│
└── README.md



Installation
1. Clone the repository
git clone <your-repository-url>
2. Navigate to the project
cd "Task Forge"
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment
Windows
venv\Scripts\activate
5. Install Django
pip install django
6. Apply migrations
python manage.py migrate
7. Create an admin account
python manage.py createsuperuser
8. Start the development server
python manage.py runserver

Open the application at:

http://127.0.0.1:8000/
How It Works
Register a new account or log in.
Create a new project from the dashboard.
Add users as project members.
Create tasks inside the project.
Assign tasks to project members.
Set task status, priority, and due date.
Open a task to view its details.
Add comments for project communication.
Edit or delete tasks when required.
Project owners can edit or delete projects and manage members.
Future Enhancements

The following features can be added in future versions:

Real-time notifications
WebSocket-based real-time collaboration
Kanban drag-and-drop board
Task search and filtering
Project activity timeline
Comment editing and deletion
Email notifications
Dark mode
REST API integration
Screenshots

## Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Project Details
![Project Details](screenshots/project-detail.png)

### Task Details
![Task Details](screenshots/task-detail.png)

Learning Outcomes

Through this project, the following concepts were practiced:

Django project and app structure
Django models and relationships
ModelForms
CRUD operations
Django authentication
User authorization
Many-to-many relationships
Foreign key relationships
Template inheritance
Static files
Responsive CSS
SQLite database management
Backend and frontend integration
License

This project was developed as part of a Full Stack Development internship project.

Author

Shubhrodeep Majumder

B.Tech Computer Science and Engineering
RCC Institute of Information Technology


**Important:** এখন `<your-repository-url>` আর screenshot placeholders 그대로 রাখো। এগুলো আমরা পরে actual GitHub URL এবং screenshots দিয়ে replace করব।

Paste করার পর আমাকে `done` বলো।