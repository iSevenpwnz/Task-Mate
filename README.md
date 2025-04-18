# Система Управління Завданнями Команди

https://task-mate-5od7.onrender.com

Система для ефективного управління завданнями в IT-команді, яка дозволяє створювати завдання, призначати їх членам команди та відстежувати їх виконання.

## Опис проекту

Це веб-додаток для управління завданнями в IT-командах, який дозволяє керувати проектами та організовувати роботу команди. Система розроблена для команд, які складаються з розробників, дизайнерів, project-менеджерів та QA-спеціалістів, і вирішує проблеми комунікації та розподілу завдань під час розробки продукту.

## Функціональність

- **Управління працівниками**:
  - Реєстрація та авторизація користувачів
  - Різні посади (розробник, дизайнер, project-менеджер, QA-спеціаліст)
  - Перегляд профілів працівників

- **Управління завданнями**:
  - Створення завдань з описом, дедлайном та пріоритетом
  - Призначення завдань одному або кільком членам команди
  - Позначення завдань як виконаних
  - Фільтрація завдань за різними критеріями

- **Типи завдань**:
  - Виправлення помилок (Bug Fix)
  - Розробка нових функцій (Feature Development)
  - Документація
  - Тестування
  - Дизайн інтерфейсу

## Встановлення

1. Клонуйте репозиторій:
```
git clone https://github.com/username/TaskProject.git
cd TaskProject
```

2. Створіть віртуальне середовище та активуйте його:
```
python -m venv venv
venv\Scripts\activate  # для Windows
```

3. Встановіть залежності:
```
pip install -r requirements.txt
```

4. Виконайте міграції:
```
python manage.py migrate
```

5. Завантажте тестові дані:
```
python manage.py loaddata task_app/fixtures/initial_data.json
```

6. Запустіть сервер:
```
python manage.py runserver
```

## Технології

- Django
- Python
- HTML/CSS
- Bootstrap

## Структура проекту

- **models.py** - визначає моделі даних (Worker, Task, Position, TaskType)
- **views.py** - містить логіку обробки HTTP запитів
- **forms.py** - визначає форми для створення та редагування об'єктів
- **templates/** - HTML шаблони для відображення сторінок
- **fixtures/** - початкові дані для наповнення бази даних
- **tests/** - модульні та інтеграційні тести проекту

## Тестування

Проект включає набір тестів для забезпечення коректності роботи всіх компонентів:

- **test_models.py** - тести для моделей, які перевіряють їх атрибути, методи та зв'язки
- **test_views.py** - тести для представлень, які перевіряють відповіді сервера та контекст шаблонів
- **test_forms.py** - тести для форм, які перевіряють валідацію даних

Для запуску тестів використовуйте команду:
```
python manage.py test tests
```

## Використання

1. Відкрийте браузер та перейдіть за адресою http://127.0.0.1:8000/
2. Авторизуйтесь в системі (для тестових даних використовуйте логін: admin, та створіть новий пароль)
3. У розділі "Завдання" ви можете переглядати існуючі завдання, створювати нові та керувати ними
4. У розділі "Працівники" ви можете додавати нових членів команди та призначати їм посади

---

# Team Task Management System

https://task-mate-5od7.onrender.com

A system for effective task management in IT teams, allowing users to create tasks, assign them to team members, and track their completion.

## Project Description

This is a web application for managing tasks in IT teams, helping to manage projects and organize team work. The system is designed for teams consisting of developers, designers, project managers, and QA specialists, and solves problems of communication and task distribution during product development.

## Features

- **Employee Management**:
  - User registration and authentication
  - Various positions (developer, designer, project manager, QA specialist)
  - Employee profile viewing

- **Task Management**:
  - Creating tasks with description, deadline, and priority
  - Assigning tasks to one or more team members
  - Marking tasks as completed
  - Filtering tasks by various criteria

- **Task Types**:
  - Bug Fix
  - Feature Development
  - Documentation
  - Testing
  - UI Design

## Installation

1. Clone the repository:
```
git clone https://github.com/username/TaskProject.git
cd TaskProject
```

2. Create and activate a virtual environment:
```
python -m venv venv
venv\Scripts\activate  # for Windows
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run migrations:
```
python manage.py migrate
```

5. Load sample data:
```
python manage.py loaddata task_app/fixtures/initial_data.json
```

6. Start the server:
```
python manage.py runserver
```

## Technologies

- Django
- Python
- HTML/CSS
- Bootstrap

## Project Structure

- **models.py** - defines data models (Worker, Task, Position, TaskType)
- **views.py** - contains HTTP request handling logic
- **forms.py** - defines forms for creating and editing objects
- **templates/** - HTML templates for page rendering
- **fixtures/** - initial data for populating the database
- **tests/** - unit and integration tests for the project![It_Company_Task_Manager_a8510d162c](https://github.com/user-attachments/assets/d8328b6f-9914-4a60-8293-106517803ee9)


## Testing

The project includes a comprehensive test suite to ensure all components function correctly:

- **test_models.py** - tests for models that check their attributes, methods, and relationships
- **test_views.py** - tests for views that check server responses and template context
- **test_forms.py** - tests for forms that check data validation

To run tests, use the command:
```
python manage.py test tests
```

## Usage

1. Open your browser and go to http://127.0.0.1:8000/
2. Log in to the system (for test data, use login: admin, and create a new password)
3. In the "Tasks" section, you can view existing tasks, create new ones, and manage them
4. In the "Workers" section, you can add new team members and assign them positions
