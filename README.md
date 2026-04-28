# Run Club Hub

Run Club Hub is a Django web application built for a running club community. It allows users to view, create, update, and delete running event records through a web interface, while also providing additional pages for discussion and login. The project demonstrates relational database use, CRUD functionality, structured navigation, and responsive layout design.

## Project Purpose

The purpose of Run Club Hub is to give a running club a simple platform to manage upcoming events and provide a central place for club members to navigate important pages. It provides value by allowing event information to be stored in a database and updated dynamically through the application.

## Features

- Homepage with shared navigation bar
- Events page displaying event records from the database
- Full CRUD functionality for event records
- Discussion page
- Login page
- Shared `base.html` template for consistent layout
- Django admin panel for record management
- Custom CSS styling
- Bootstrap-based page structure

## CRUD Functionality

Users can:
- **Create** a new event
- **Read** and view all existing events
- **Update** existing event details
- **Delete** existing events

## Data Model

The project currently uses a Django model for event records, storing information such as:
- title
- date
- time
- location
- description

These records are stored in the project database and displayed dynamically in the frontend templates.

## Technologies Used

- Python
- Django
- HTML
- CSS
- Bootstrap 5
- SQLite
- Git
- GitHub

## Project Structure

- `club/` - Django app containing models, views, URLs, forms, and templates
- `runclubhub/` - project settings and main URL configuration
- `templates/` - shared templates including `base.html`
- `static/css/` - custom stylesheet
- `TESTING.md` - manual testing documentation
- `README.md` - project overview and setup instructions

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd run-club-hub
