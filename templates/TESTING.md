# Testing

## Manual Testing

### Events Page
- Created a test event in Django admin.
- Confirmed the event saved successfully in the database.
- Created an `events` view in `views.py` to retrieve event data.
- Added a URL route for `/events/` in `club/urls.py`.
- Created `club/templates/club/events.html` to display event information.
- Ran the development server and visited `/events/`.
- Confirmed the event appeared correctly on the page.

### Navbar Testing
- Tested the Events link in the homepage navbar.
- Found that the Events link was not working because it used `href="#"`.
- Updated the link in `base.html` to use `{% url 'events' %}`.
- Retested navigation from the homepage.
- Confirmed clicking **Events** now opens the Events page successfully.

## Outcome
- The Events feature is working end-to-end.
- Events can be created in admin and displayed on the frontend.
- Navigation to the Events page is now functional.
