# 🌍 ALX Travel App

<div align="center">

![Django](https://img.shields.io/badge/Django-4.2.7-green.svg?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.12+-blue.svg?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg?style=for-the-badge&logo=mysql)
![REST API](https://img.shields.io/badge/REST-API-red.svg?style=for-the-badge&logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

*A production-ready Django REST API for travel listing platform*

[Features](#5-feature-breakdown) •
[Tech Stack](#3-technology-stack-overview) •
[Installation](#getting-started) •
[API Docs](#api-documentation) •
[License](#9-license)

</div>

---

## 📜 Table of Contents

* [1. Project Overview](#1-project-overview)
* [2. Team Roles and Responsibilities](#2-team-roles-and-responsibilities)
* [3. Technology Stack Overview](#3-technology-stack-overview)
* [4. Database Design Overview](#4-database-design-overview)
* [5. Feature Breakdown](#5-feature-breakdown)
* [6. API Security Overview](#6-api-security-overview)
* [7. CI/CD Pipeline Overview](#7-cicd-pipeline-overview)
* [8. Resources](#8-resources)
* [9. License](#9-license)
* [10. Created By](#10-created-by)

---

## 1. Project Overview

### 📖 Brief Description

The **ALX Travel App** is a comprehensive, production-ready Django REST API application designed to serve as the backbone for a modern travel listing platform. This project demonstrates industry-standard best practices in backend development, featuring robust database management, automated API documentation, secure environment configuration, and scalable architecture. Built with Django and Django REST Framework, it provides a solid foundation for managing travel listings, bookings, and related travel services.

The application integrates modern development tools including Swagger for interactive API documentation, MySQL for reliable data persistence, Celery for asynchronous task processing, and CORS support for seamless frontend integration. This project serves as both a learning resource and a production-ready template for building scalable travel-related applications.

### 🎯 Project Goals

* **Scalable Backend Architecture**: Implement a modular, maintainable Django project structure that can grow with business needs
* **Secure Configuration Management**: Utilize environment variables and Django-environ for secure handling of sensitive credentials
* **Comprehensive API Documentation**: Provide interactive, auto-generated API documentation via Swagger/drf-yasg
* **Database Reliability**: Configure MySQL with proper connection handling and migrations for data integrity
* **Asynchronous Processing**: Set up Celery and Redis for handling background tasks and email notifications
* **Cross-Origin Support**: Enable CORS for seamless integration with modern frontend frameworks
* **Industry Best Practices**: Follow Django and REST API development standards for code quality and maintainability
* **Version Control Excellence**: Maintain clean Git history with proper .gitignore and repository structure

### 🔑 Key Tech Stack

Python 3.12+, Django 4.2.7, Django REST Framework, MySQL 8.0+, Redis, Celery, Swagger/drf-yasg

---

## 2. Team Roles and Responsibilities

| Role | Key Responsibility |
|------|-------------------|
| **🎯 Project Manager** | Oversees project timeline, coordinates team efforts, manages stakeholder communication, and ensures deliverables meet requirements |
| **💻 Backend Developer** | Implements Django models, views, serializers, and business logic; writes unit tests; optimizes database queries; maintains API endpoints |
| **🗄️ Database Administrator** | Designs database schema, manages MySQL configurations, handles migrations, optimizes queries, ensures data integrity and backup strategies |
| **🔐 DevOps Engineer** | Sets up CI/CD pipelines, manages deployment environments, configures Docker containers, monitors application performance, handles infrastructure |
| **🎨 Frontend Developer** | Integrates with REST API, consumes API endpoints, implements user interface, handles CORS configuration with backend team |
| **🧪 QA Engineer** | Develops test plans, performs integration testing, conducts API testing, validates security measures, reports bugs and regressions |
| **📚 Technical Writer** | Creates API documentation, writes user guides, maintains README files, documents deployment procedures and architecture decisions |
| **🔒 Security Specialist** | Conducts security audits, implements authentication/authorization, reviews code for vulnerabilities, ensures OWASP compliance |

---

## 3. Technology Stack Overview

| Technology | Purpose in the Project |
|-----------|----------------------|
| **Python 3.12+** | Core programming language providing modern syntax, type hints, and performance improvements for backend development |
| **Django 4.2.7** | High-level web framework handling ORM, authentication, admin interface, middleware, and overall application structure |
| **Django REST Framework** | Powerful toolkit for building REST APIs with serialization, authentication, permissions, and viewsets |
| **MySQL 8.0+** | Relational database management system for persistent data storage with ACID compliance and robust transaction support |
| **mysqlclient** | Python MySQL database adapter providing efficient native MySQL connectivity for Django |
| **django-environ** | Environment variable management tool for secure configuration of sensitive credentials and settings |
| **django-cors-headers** | Middleware for handling Cross-Origin Resource Sharing (CORS) to enable secure API access from different domains |
| **drf-yasg** | Swagger/OpenAPI documentation generator for automatic, interactive API documentation at /swagger/ endpoint |
| **Celery 5.3.4** | Distributed task queue for handling asynchronous operations like email sending, data processing, and scheduled tasks |
| **Redis** | In-memory data structure store used as Celery message broker and result backend for fast task queue management |
| **Git** | Version control system for tracking changes, collaboration, and maintaining project history |

---

## 4. Database Design Overview

### 🗂️ Key Entities

The ALX Travel App database is designed to support a comprehensive travel listing platform with the following core entities:

* **User** - Manages user accounts, authentication, profiles, and preferences
* **Listing** - Represents travel destinations, properties, or services with detailed information
* **Booking** - Tracks reservations and booking transactions made by users
* **Review** - Stores user feedback and ratings for listings
* **Category** - Organizes listings into different travel categories (hotels, tours, rentals, etc.)
* **Location** - Geographic information including countries, cities, and coordinates
* **Amenity** - Features and facilities available with listings
* **Payment** - Payment transaction records and financial data
* **Message** - Communication between users and listing owners

### 🔗 Relationships

* **One-to-Many**: A single User can create multiple Listings. Each Listing is owned by one User. This establishes content ownership and allows users to manage their posted travel offerings.

* **Many-to-One**: Multiple Bookings belong to a single Listing. Each Booking references one User who made the reservation. This enables tracking of all reservations for a property and maintains user booking history.

* **Many-to-Many**: Listings can have multiple Amenities (WiFi, pool, parking, etc.), and each Amenity can be associated with multiple Listings. This flexible relationship allows for comprehensive feature descriptions across different properties.

---

## 5. Feature Breakdown

* **🔐 User Authentication & Authorization** - Secure user registration, login, and role-based access control using Django's built-in authentication system with session and token-based authentication options. Enables different permission levels for guests, registered users, and administrators.

* **📋 Travel Listing Management** - Full CRUD operations for creating, reading, updating, and deleting travel listings including destinations, accommodations, and tour packages. Supports rich media uploads, detailed descriptions, pricing, and availability management.

* **🔍 Advanced Search & Filtering** - Powerful search functionality allowing users to find listings based on location, category, price range, amenities, ratings, and availability dates. Implements efficient database queries with pagination for optimal performance.

* **⭐ Review & Rating System** - Enables users to leave detailed reviews and star ratings for listings they've experienced. Includes aggregate rating calculations, review moderation, and helpful/unhelpful voting to build trust and community feedback.

* **📅 Booking & Reservation Management** - Complete booking workflow from availability checking to reservation confirmation. Tracks booking status (pending, confirmed, cancelled), manages payment integration, and sends automated notifications.

* **📊 RESTful API Endpoints** - Comprehensive REST API built with Django REST Framework providing JSON responses, proper HTTP status codes, request validation, and consistent error handling. Supports standard HTTP methods (GET, POST, PUT, PATCH, DELETE).

* **📖 Interactive API Documentation** - Auto-generated Swagger/OpenAPI documentation accessible at /swagger/ endpoint. Provides interactive testing environment, request/response examples, schema definitions, and authentication testing capabilities.

* **🌐 CORS Support** - Cross-Origin Resource Sharing configuration enabling secure API access from frontend applications hosted on different domains. Supports modern SPA frameworks like React, Vue, and Angular.

* **⚡ Asynchronous Task Processing** - Celery integration for handling background tasks such as sending confirmation emails, generating reports, processing images, and performing scheduled maintenance without blocking API responses.

* **🔒 Environment-based Configuration** - Secure management of sensitive data using environment variables for database credentials, secret keys, API tokens, and environment-specific settings (development, staging, production).

---

## 6. API Security Overview

Security is paramount in the ALX Travel App. The following measures are implemented to protect user data and ensure API integrity:

* **🔑 Authentication & Session Management** - Django's robust session-based authentication system with secure cookie handling, CSRF protection, and session timeout controls. Token authentication available for stateless API clients requiring persistent access without session cookies.

* **🛡️ Authorization & Permissions** - Role-based access control (RBAC) ensuring users can only access and modify resources they're authorized for. Implements object-level permissions so users can only edit their own listings and bookings while allowing read access to public data.

* **🔐 Environment Variable Protection** - Sensitive configuration data (SECRET_KEY, database passwords, API keys) stored in .env files excluded from version control. Uses django-environ for type-safe environment variable parsing and default value management.

* **🚦 Rate Limiting** - Prevents abuse and DDoS attacks by limiting the number of API requests per user/IP address within specific time windows. Protects against brute force attacks on authentication endpoints and ensures fair resource usage across all users.

* **✅ Input Validation & Sanitization** - Django REST Framework serializers validate all incoming data against defined schemas, type checking, and custom validation rules. Prevents SQL injection, XSS attacks, and malformed data from reaching the database layer.

* **🔒 HTTPS & Secure Headers** - Production deployment enforces HTTPS for all API traffic, protecting data in transit. Security middleware adds HTTP headers (X-Frame-Options, X-Content-Type-Options, Strict-Transport-Security) to prevent common web vulnerabilities.

* **🗄️ SQL Injection Prevention** - Django ORM provides automatic query parameterization, eliminating SQL injection vulnerabilities. All database queries use prepared statements, and raw SQL is avoided unless absolutely necessary with proper sanitization.

* **📝 Audit Logging** - Comprehensive logging of authentication attempts, data modifications, and suspicious activities. Enables security monitoring, incident response, and compliance with data protection regulations.

---

## 7. CI/CD Pipeline Overview

**Continuous Integration and Continuous Deployment (CI/CD)** is a modern software development practice that automates the process of testing and deploying code changes. For the ALX Travel App, CI/CD ensures that every code commit is automatically validated, tested, and prepared for deployment, reducing human error and accelerating the development lifecycle.

The CI/CD strategy for this project leverages **GitHub Actions** as the primary automation platform. When developers push code to the repository, GitHub Actions automatically triggers workflows that:

1. **Run automated tests** to verify that new changes don't break existing functionality
2. **Check code quality** using linters and static analysis tools to maintain coding standards
3. **Build Docker containers** for consistent deployment across different environments
4. **Deploy to staging environments** for integration testing before production release
5. **Manage database migrations** ensuring schema changes are applied safely
6. **Send notifications** to the team about build status and deployment progress

This automation pipeline is crucial for maintaining code quality, catching bugs early, and enabling rapid iteration. By automating repetitive tasks, the team can focus on feature development while having confidence that the application remains stable and secure throughout the development process. The use of **Docker** containers ensures that the application runs consistently across development, testing, and production environments, eliminating the "it works on my machine" problem.

---

## 8. Resources

### 📚 Official Documentation

* [Django Documentation](https://docs.djangoproject.com/) - Official Django framework documentation
* [Django REST Framework](https://www.django-rest-framework.org/) - DRF comprehensive guide
* [drf-yasg Documentation](https://drf-yasg.readthedocs.io/) - Swagger/OpenAPI integration guide
* [Celery Documentation](https://docs.celeryproject.org/) - Distributed task queue documentation
* [MySQL Documentation](https://dev.mysql.com/doc/) - MySQL database reference

### 🎓 Learning Resources

* [Build a CRUD API](https://savanna.alxafrica.com/rltoken/EUkNLYOyh9mh3zlESJbk8w) - Tutorial on building REST APIs
* [Django Best Practices](https://savanna.alxafrica.com/rltoken/nLDnWVi_0eH_zo7qE6hKig) - Industry-standard Django patterns
* [Manage Settings Securely](https://savanna.alxafrica.com/rltoken/AIhdrI--XIMZkvSF-L1XFA) - Environment variable management
* [Integrating drf-yasg for Swagger](https://savanna.alxafrica.com/rltoken/b0A9zBm_zAND0nf9ji3ZXQ) - API documentation setup

### 🛠️ Tools & Libraries

* [django-environ](https://django-environ.readthedocs.io/) - Environment variable configuration
* [django-cors-headers](https://github.com/adamchainz/django-cors-headers) - CORS handling
* [Redis](https://redis.io/) - In-memory data store and cache

---

## 🚀 Getting Started

### Prerequisites

* Python 3.12 or higher
* MySQL 8.0 or higher
* Redis server (for Celery)
* Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/MachariaP/alx_travel_app.git
cd alx_travel_app
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env file with your configuration
```

5. **Create MySQL database**
```sql
CREATE DATABASE alx_travel_app_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

6. **Run migrations**
```bash
python manage.py migrate
```

7. **Create superuser**
```bash
python manage.py createsuperuser
```

8. **Run development server**
```bash
python manage.py runserver
```

9. **Access the application**
* API: http://localhost:8000/api/
* Admin: http://localhost:8000/admin/
* Swagger: http://localhost:8000/swagger/

### Running Celery (Optional)

For background tasks, start Celery in a separate terminal:

```bash
celery -A alx_travel_app worker -l info
```

---

## 📖 API Documentation

Interactive API documentation is available at:

* **Swagger UI**: http://localhost:8000/swagger/
* **ReDoc**: http://localhost:8000/redoc/

The API documentation provides:
* Complete endpoint listing
* Request/response schemas
* Authentication testing
* Interactive request execution

---

## 📁 Project Structure

```
alx_travel_app/
├── alx_travel_app/          # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Project settings and configuration
│   ├── urls.py              # URL routing configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── listings/                # Listings app
│   ├── migrations/          # Database migrations
│   ├── __init__.py
│   ├── admin.py             # Admin interface configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Database models
│   ├── serializers.py       # API serializers
│   ├── views.py             # API views
│   ├── urls.py              # App URL routing
│   └── tests.py             # Unit tests
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
├── LICENSE                  # MIT License
└── README.md                # Project documentation
```

---

## 🧪 Running Tests

```bash
# Run all tests
python manage.py test

# Run tests with coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 9. License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The MIT License is a permissive license that allows for reuse with minimal restrictions. You are free to use, modify, distribute, and sell this software, provided you include the original copyright notice and license text.

---

## 10. Created By

**Phinehas Macharia**

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-MachariaP-black?style=for-the-badge&logo=github)](https://github.com/MachariaP)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/phineas-macharia)

*Built with ❤️ for ALX Africa*

</div>

---

<div align="center">

**[⬆ Back to Top](#-alx-travel-app)**

</div>
