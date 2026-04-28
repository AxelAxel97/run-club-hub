# Testing

## Manual Testing

### Home Page
- Opened the homepage successfully.
- Confirmed the navigation bar displays links for Home, Events, Discussion, and Login.
- Confirmed the Home link returns to the homepage correctly.

### Events Page
- Opened the Events page successfully from the navigation bar.
- Confirmed event records display correctly on the page.
- Confirmed events are listed in date and time order.

### Create Event
- Clicked the **Add Event** button on the Events page.
- Completed the event form with test data.
- Submitted the form successfully.
- Confirmed the new event appeared on the Events page after submission.

### Update Event
- Clicked the **Edit** button for an existing event.
- Updated event details such as title or location.
- Submitted the form successfully.
- Confirmed the updated event details appeared correctly on the Events page.

### Delete Event
- Clicked the **Delete** button for an existing event.
- Opened the delete confirmation page successfully.
- Confirmed deletion of the selected event.
- Confirmed the event was removed from the Events page.

### Discussion Page
- Opened the Discussion page from the navigation bar successfully.
- Confirmed the page content displayed correctly.

### Login Page
- Opened the Login page from the navigation bar successfully.
- Confirmed the login form fields display correctly.

### Admin Panel
- Logged into the Django admin panel successfully.
- Confirmed event records can be created and managed in the admin area.

## Validation Summary
- CRUD functionality for events is working correctly.
- Navigation between all main pages is functioning correctly.
- Event data is stored in the database and displayed dynamically on the frontend.
- Shared layout and templates are working consistently across pages.
