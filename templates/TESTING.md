# Testing

## Manual Testing

### Home Page
- Opened the homepage successfully.
- Confirmed the navbar displays Home, Events, Discussion, and Login.
- Confirmed the Home link returns to the homepage correctly.

### Events Page
- Created a test event in Django admin.
- Confirmed the event saved successfully in the database.
- Added an `events` view in `views.py` to retrieve event data from the model.
- Added a route for `/events/` in `club/urls.py`.
- Created `club/templates/club/events.html` to display event information.
- Confirmed the Events page loads correctly.
- Confirmed event data is displayed on the page in date and time order.

### Navbar Testing
- Tested the Events link in the homepage navbar.
- Found the Events link was not working because it used `href="#"`.
- Updated the link in `base.html` to use `{% url 'events' %}`.
- Retested and confirmed the Events link now opens the Events page successfully.

### Discussion Page
- Created `discussion.html` inside `club/templates/club/`.
- Added a `discussion` view in `views.py`.
- Added a `/discussion/` route in `club/urls.py`.
- Updated the navbar link to use `{% url 'discussion' %}`.
- Confirmed the Discussion page opens correctly from the navbar.

### Login Page
- Created `login.html` inside `club/templates/club/`.
- Added a `login` view in `views.py`.
- Added a `/login/` route in `club/urls.py`.
- Updated the navbar link to use `{% url 'login' %}`.
- Confirmed the Login page opens correctly from the navbar.

## Outcome
- The project now has a working homepage, events page, discussion page, and login page.
- Navigation between all pages is working correctly.
- Event data can be added through Django admin and displayed dynamically on the frontend.
