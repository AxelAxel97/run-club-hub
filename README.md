# Run Club Hub

Run Club Hub is a Django web application built for a running club community. It allows users to register an account, browse upcoming running events, and create, edit, or delete their own events. This site was developed using Python (Django), HTML, CSS and by storing data in a PostgreSQL database.

[Live Website](https://run-club-hub-4c7ff48afff2.herokuapp.com/)

---

## Table of Contents

- [Wireframes](#wireframes)
- [User Goals and Stories](#user-goals-and-stories)
- [Design](#design)
- [Development](#development)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

---
## Wireframes

Wireframes were created at the beginning of the project to plan the layout and structure of each page before development began.

### Home Page

+--------------------------------------------------+
|  NAVBAR: Run Club Hub       Login | Register     |
+--------------------------------------------------+
|                                                  |
|   Find your next group run                       |
|                                                  |
|   Join your local running community,             |
|   discover events, and stay connected            |
|   with other runners!                            |
|                                                  |
|              [HERO IMAGE]                        |
|                                                  |
+--------------------------------------------------+
|         Welcome to Run Club Hub                  |
|   Run Club Hub is a community platform...        |
+--------------------------------------------------+
|  FOOTER: Follow us! [FB] [IG] [X]               |
|  2026 Run Club Hub. All rights reserved.         |
+--------------------------------------------------+


### Evernts Page 

+--------------------------------------------------+
|  NAVBAR: Run Club Hub    Hello, user | Logout    |
+--------------------------------------------------+
|  Events                        [+ Add Event]     |
+--------------------------------------------------+
|  +--------------------------------------------+  |
|  | Event Title                                |  |
|  | Date: 01/06/2026  Time: 07:00              |  |
|  | Location: Holland Park                     |  |
|  | Description: Morning 10K group run...      |  |
|  |                          [Edit] [Delete]   |  |
|  +--------------------------------------------+  |
|                                                  |
|  +--------------------------------------------+  |
|  | Event Title                                |  |
|  | Date: 08/06/2026  Time: 09:00              |  |
|  | Location: City Centre                      |  |
|  | Description: Casual 5K social run...       |  |
|  +--------------------------------------------+  |
+--------------------------------------------------+
|  FOOTER                                          |
+--------------------------------------------------+

### Add Event 

+--------------------------------------------------+
|  NAVBAR: Run Club Hub    Hello, user | Logout    |
+--------------------------------------------------+
|  Add New Event                                   |
+--------------------------------------------------+
|  +--------------------------------------------+  |
|  |  Title:       [________________________]   |  |
|  |  Date:        [________________________]   |  |
|  |  Time:        [________________________]   |  |
|  |  Location:    [________________________]   |  |
|  |  Description: [________________________]   |  |
|  |               [________________________]   |  |
|  |                                            |  |
|  |                    [Save Event]            |  |
|  +--------------------------------------------+  |
+--------------------------------------------------+
|  FOOTER                                          |
+--------------------------------------------------+

### Discussions 

+--------------------------------------------------+
|  NAVBAR: Run Club Hub    Hello, user | Logout    |
+--------------------------------------------------+
|  Discussion Board                                |
+--------------------------------------------------+
|  +--------------------------------------------+  |
|  | [PIN] PINNED  - Posted by Admin            |  |
|  | Welcome to the Run Club Hub Discussion!    |  |
|  | This is your space to connect with fellow  |  |
|  | runners...                                 |  |
|  +--------------------------------------------+  |
|                                                  |
|  +--------------------------------------------+  |
|  | [ROUTES]  - Posted by Sarah K. - 2 days ago|  |
|  | Best routes for a Sunday long run?         |  |
|  | Looking for something scenic around 12km.. |  |
|  |  > Mike T: The riverside loop is great!    |  |
|  +--------------------------------------------+  |
|                                                  |
|  +--------------------------------------------+  |
|  | [RACING]  - Posted by Dan R. - 4 days ago  |  |
|  | Anyone targeting a sub-25 5K this season?  |  |
|  |  > Emma W: I am! Let's coordinate a run.   |  |
|  +--------------------------------------------+  |
|                                                  |
|  +--------------------------------------------+  |
|  | [TRAINING] - Posted by Priya M. - 6 days   |  |
|  | Favourite recovery tips after a long run?  |  |
|  |  > Tom B: Foam rolling and protein meal!   |  |
|  +--------------------------------------------+  |
+--------------------------------------------------+
|  FOOTER                                          |
+--------------------------------------------------+

## User Goals and Stories

### User goals
- As a user I want to:
  - Easily and intuitively navigate throughout the website
  - Browse the website naturally and with ease
  - Be able to view the website and read all information on all screen sizes
  - Create an account on the website
  - View all upcoming running events
  - Create my own running events
  - Manage my events and edit or delete them if needed

### Business owner goals
- As the website business owner I want to:
  - Provide users with information about the running club
  - Allow users to easily access and use the site
  - Allow users to create and manage running events
  - Allow users to edit and delete their own events
  - Provide a discussion space for club members
  - Provide social media links to users

### User Stories

#### As a user
  - As a user I want to visit the website and understand its purpose immediately
  - As a user I want to easily understand how to use the website
  - As a user I want to create an account easily
  - As a user I want to view all upcoming running events
  - As a user I want to create a new event with ease
  - As a user I want the ability to edit my own events
  - As a user I want the ability to delete my own events
  - As a user I want to receive clear feedback when I complete an action
  - As a user I want to have an enjoyable experience
  - As a user I want to return to the site to manage my events

#### As a website business owner
  - As a site owner I want to allow for a good user experience
  - As a site owner I want to allow the user to easily navigate the website without issues
  - As a site owner I want to encourage users to create an account
  - As a site owner I want to encourage users to create and manage events
  - As a site owner I want the user to have a positive experience by allowing them to edit or delete their own events
  - As a site owner I want only authenticated users to be able to create or modify events

#### As a new user
  - As a new user I want to navigate the page intuitively and with ease
  - As a new user I want to understand the page purpose upon first viewing
  - As a new user I want to see the club's social media presence
  - As a new user I want to easily create an account
  - As a new user I want to easily browse upcoming events
  - As a new user I want to easily create my own event
  - As a new user I want to edit or delete an event I created
  - As a new user I want to enjoy the experience and return to the site

---

## Design

### Font
Bootstrap 5's default font stack was used throughout the project. This provides clean, readable typography across all devices without requiring additional font imports.

### Colours
The site uses a dark navbar and footer (bg-dark) with white text for strong contrast, combined with Bootstrap's default white card backgrounds and muted text for secondary content. This creates a clean, high-contrast design suited to an active sports community.

### Data Model

| Field | Type | Notes |
|---|---|---|
| title | CharField | Max 200 characters |
| date | DateField | Event date |
| time | TimeField | Event time |
| location | CharField | Max 200 characters |
| description | TextField | Full event description |
| created_on | DateTimeField | Auto-set on creation |
| created_by | ForeignKey (User) | Links event to its creator; SET_NULL on user delete |

---

## Development

### Agile Methodology

This project was developed using the Agile methodology. User stories and tasks were tracked across the following epics:

**Epic 1 - Initial Setup**
  - As a developer, I need to create the base.html page and structure so that other pages can reuse the layout
  - As a developer, I need to create static resources so that images and CSS work on the website
  - As a developer, I need to set up the project so that it is ready for implementing the core features
  - As a developer, I need to create the footer with social media links
  - As a developer, I need to create the navbar so that users can navigate the website from any device

**Epic 2 - User Registration and Authentication**
  - As a developer, I need to implement the Register page using Django's built-in UserCreationForm
  - As a developer, I need to implement the Login page using Django's AuthenticationForm
  - As a developer, I need to implement Logout functionality
  - As a site owner, I want protected pages to redirect unauthenticated users to the login page

**Epic 3 - Event Management (CRUD)**
  - As a user, I would like to be able to create a new running event
  - As a user, I would like to view all upcoming events ordered by date and time
  - As a user, I would like to be able to edit my own events
  - As a user, I would like to delete my own events when I no longer need them

**Epic 4 - Deployment**
  - As a developer, I need to deploy the project to Heroku so that it is live for users
  - As a developer, I need to configure PostgreSQL as the production database
  - As a developer, I need to configure WhiteNoise for static file serving

**Epic 5 - Documentation**
  - Complete README documentation
  - Complete TESTING.md documentation

---

## Technologies Used
- **Python** - the main language used in this project
- **Django** - the web framework used to build the application
- **HTML** - used to structure all templates
- **CSS** - used for custom styling
- **Bootstrap 5** - used for predefined styled elements and responsive layout
- **Font Awesome** - used for social media icons in the footer
- **Unicode Emoji** - used as visual icons throughout the UI (no library required)
- **PostgreSQL** - production database hosted on Heroku
- **SQLite** - local development database
- **WhiteNoise** - for serving static files in production
- **Gunicorn** - production WSGI server
- **GitHub** - used to host the repository
- **Git** - used to commit and push code during development
- **Heroku** - used to host the deployed live site
- **Favicon.io** - used for generating the website favicon
- **Chrome Dev Tools** - used for debugging and testing responsiveness
- **CI Python Linter** - used for validating Python code

---

## Features

### Existing Features

- **Home Page**
  - This is the first page the user sees when they arrive on the website. The primary goal is to allow the user to understand the purpose of the website immediately.
  - A clear navigation bar makes it intuitive for the user to navigate to all sections of the site.
  - The footer section provides social media links so users can follow the club online.

- **Events Page**
  - Displays all upcoming running events stored in the database, ordered by date and time.
  - Each event card shows the title, date, time, location, and description.
  - Logged-in users who created an event will see Edit and Delete buttons on their own events.

- **Add Event Page**
  - Logged-in users can create a new event by filling out a simple form.
  - Unauthenticated users are redirected to the Login page if they attempt to access this page.

- **Edit Event Page**
  - Allows the event creator to update an existing event's details.
  - Only the user who created the event can edit it - other users are shown a permission denied message.

- **Delete Event Page**
  - Allows the event creator to delete one of their events via a confirmation page.
  - Only the user who created the event can delete it - other users are shown a permission denied message.

- **Discussion Page**
  - Provides a community discussion board with pinned announcements and threads covering routes, racing goals, recovery tips, and meetup planning.

- **Register Page**
  - New users can create an account with a username and password.
  - Upon successful registration, the user is automatically logged in and redirected to the homepage with a flash message.

- **Login Page**
  - Existing users can log in with their username and password.
  - Upon successful login, a flash message confirms the login and the navbar updates to show their username.

- **Logout**
  - Logged-in users can log out via the navbar button.
  - A flash message confirms the logout.

- **Flash Messages**
  - Success and error messages display after every key user action including login, logout, register, create event, edit event, and delete event.

- **Navigation Menu**
  - The navigation bar is present on all pages.
  - When logged out: Login and Register links are shown.
  - When logged in: the user's username and a Logout button are shown.

  The following navigation items are available on all pages:

  Home -> home.html - Visible to all

  Events -> events.html - Visible to all

  Discussion -> discussion.html - Visible to all

  Add Event -> add_event.html - Visible to logged in users only

  Logout - Visible to logged in users only

  Login -> login.html - Visible to logged out users only

  Register -> register.html - Visible to logged out users only

- **Favicon**
  - A custom favicon sits in the browser tab allowing users to instantly recognise the webpage.

### Features Left to Implement
  - A real-time discussion board where users can post and reply to messages
  - User profile pages with personal bests and event history
  - Email confirmation on registration
  - Event image uploads
  - Search and filter functionality on the Events page

---

## Testing

Full manual testing has been documented in [TESTING.md](TESTING.md).

### User Testing

The application was tested on a MacBook Pro using the Google Chrome browser.

It was also tested using Chrome DevTools across the following screen sizes:
- Mobile (375px)
- Tablet (768px)
- Desktop (1280px+)

All screen sizes worked as intended.

### Validator Testing

- **Python** - No errors were found when passing through the [CI Python Linter](https://pep8ci.herokuapp.com/)
- **HTML** - Tested using the [W3C HTML Validator](https://validator.w3.org/)
- **CSS** - Tested using the [W3C CSS Validator (Jigsaw)](https://jigsaw.w3.org/css-validator/)

### Bugs

- **Login form not submitting** - The original login template was missing method="POST" and the csrf_token tag, causing the form to silently do nothing on submission. Fixed by rewriting the login template to use Django's AuthenticationForm with proper POST handling.

- **Register page showing overwhelming help text** - Django's default form.as_p rendered all built-in password help text. Fixed by rendering each field manually and only displaying error messages when validation fails.

- **Flash messages not rendering** - The MESSAGE_TAGS setting was missing from settings.py, causing Bootstrap alert classes to not map correctly. Fixed by adding the MESSAGE_TAGS configuration.

- **@login_required redirecting to wrong URL** - Django's default login redirect pointed to /accounts/login/ which did not exist. Fixed by adding LOGIN_URL = '/login/' to settings.py.

- **Existing events breaking after adding created_by** - Adding a ForeignKey field to the Event model would have caused existing records to fail migration. Fixed by setting null=True, blank=True on the created_by field.

### Unfixed Bugs
- There are no current bugs that we are aware of.

---

## Deployment

The live site is deployed on Heroku:

**Live site:** https://run-club-hub-4c7ff48afff2.herokuapp.com/

### Steps to deploy

1. Create a Heroku account at https://heroku.com
2. Install the Heroku CLI: `brew install heroku`
3. Log in: `heroku login`
4. Create the app: `heroku create`
5. Add Postgres: `heroku addons:create heroku-postgresql:essential-0`
6. Set config vars: `heroku config:set SECRET_KEY=your-secret-key` and `heroku config:set DEBUG=False`
7. Push code: `git push heroku main`
8. Run migrations: `heroku run python manage.py migrate`
9. Create a superuser: `heroku run python manage.py createsuperuser`
10. Load fixture data (optional): `heroku run python manage.py loaddata sample_events`

### Local Development

1. 1. Clone the repository: `git clone https://github.com/AxelAxel97/run-club-hub.git`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start the server: `python manage.py runserver`
7. Access at: http://127.0.0.1:8000/

---
## Credits

- [Django Documentation](https://docs.djangoproject.com/) - framework reference
- [Bootstrap 5](https://getbootstrap.com/) - responsive layout and components
- [Font Awesome](https://fontawesome.com/) - social media icons
- [WhiteNoise](http://whitenoise.evans.io/) - static file serving in production
- [Heroku](https://heroku.com) - cloud deployment platform
- [dj-database-url](https://github.com/jazzband/dj-database-url) - database URL configuration
- [CI Python Linter](https://pep8ci.herokuapp.com/) - Python code validation
- [Favicon.io](https://favicon.io/) - favicon generation

### Content

- The format and template for the README file was inspired by the [Code Institute](https://codeinstitute.net/ie/)

- The hero image was sourced from [Unsplash](https://unsplash.com/)

- The discussion board content and event fixture data were written specifically for this project

### Coding Help

- The Django documentation was one of the main resources used throughout development - [Django Documentation](https://docs.djangoproject.com/)
- A lot of the Python and Django coding was supported by tutorials at [W3Schools](https://www.w3schools.com/)
- Bootstrap 5 documentation was used extensively for layout and components - [Bootstrap Docs](https://getbootstrap.com/docs/5.3/)
- Stack Overflow was used to help solve minor Django related bugs throughout development
- The following YouTube tutorials were helpful during development:
  - [Learn Django in 20 Minutes - Tech With Tim](https://www.youtube.com/watch?v=nGIg40xs9e4)
  - [Python Django Tutorial - Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- The CI Python Linter was used to validate all Python files - [CI Python Linter](https://pep8ci.herokuapp.com/)
- [dj-database-url](https://github.com/jazzband/dj-database-url) was used to configure the PostgreSQL database URL on Heroku
- [WhiteNoise documentation](http://whitenoise.evans.io/) was used to configure static file serving in production
- [Favicon.io](https://favicon.io/) was used to generate the site favicon
- The following projects were used as inspiration - [HappyTravels](https://github.com/d-lynch95/Portfolio-Project4), [SizzleAndSteak](https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak), [TennisBuddies](https://github.com/lucia2007/tennis_buddies)
- I received support and advice from the Code Institute, special thanks to Nikki Haig! 






