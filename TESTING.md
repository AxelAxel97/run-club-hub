# Run Club Hub - Testing

## Table of Contents

- [Manual Testing](#manual-testing)
- [User Story Testing](#user-story-testing)
- [Validator Testing](#validator-testing)
- [Browser Testing](#browser-testing)
- [Responsiveness Testing](#responsiveness-testing)
- [Bugs](#bugs)

---

## Manual Testing

### Navigation

| Test | Action | Expected Result | Pass/Fail |
|---|---|---|---|
| Home link | Click Home in navbar | Redirects to home page | Pass |
| Events link | Click Events in navbar | Redirects to events page | Pass |
| Discussion link | Click Discussion in navbar | Redirects to discussion page | Pass |
| Login link | Click Login in navbar (logged out) | Redirects to login page | Pass |
| Register link | Click Register in navbar (logged out) | Redirects to register page | Pass |
| Logout button | Click Logout in navbar (logged in) | Logs user out and redirects to home | Pass |
| Navbar brand | Click Run Club Hub logo text | Redirects to home page | Pass |

### Home Page

| Test | Action | Expected Result | Pass/Fail |
|---|---|---|---|
| Page loads | Navigate to home page | Hero image and welcome text display correctly | Pass |
| Hero image | View home page | Background image displays correctly | Pass |
| Responsive layout | Resize browser window | Layout adjusts correctly on all screen sizes | Pass |

### Events Page

| Test | Action | Expected Result | Pass/Fail |
|---|---|---|---|
| Events display | Navigate to events page | All events display ordered by date and time | Pass |
| Event details | View event card | Title, date, time, location and description all display | Pass |
| Add event button | Click Add Event (logged in) | Redirects to add event form | Pass |
| Edit button visible | View own event (logged in) | Edit button visible on own events only | Pass |
| Delete button visible | View own event (logged in) | Delete button visible on own events only | Pass |
| Edit button hidden | View another user's event | Edit button not visible | Pass |
| Delete button hidden | View another user's event | Delete button not visible | Pass |

### Add Event

| Test | Action | Expected Result | Pass/Fail |
|---|---|---|---|
| Add event (logged in) | Fill out form and submit | Event saved and redirected to events page | Pass |
| Flash message | Submit valid form | Success message displays | Pass |
| Add event (logged out) | Navigate to /events/add/ | Redirected to login page | Pass |
| Empty form submission | Submit form with no data | Form validation errors display | Pass |

### Edit Event

| Test | Action | Expected Result | Pass/Fail |
|---|---|---|---|
| Edit own event | Click Edit on own event | Form pre-filled with event data | Pass |
| Save changes | Submit edited form | Changes saved and redirected to events page | Pass |
| Flash message | Submit valid edit | Success message displays | Pass |
| Edit other user's event | Attempt to edit another user's event | Permission denied message displays | Pass |
| Edit event (logged out) | Navigate to edit URL | Redirected to login page | Pass |

### Delete Event

| Test | Action | Expected Result | Pass/Fail |
|---|---|---|---|
| Delete own event | Click Delete on own event | Confirmation page displays | Pass |
| Confirm delete | Click confirm on deletion page | Event deleted and redirected to events page | Pass |
| Flash message | Confirm deletion | Success message displays | Pass |
| Delete other user's event | Attempt to delete another user's event | Permission denied message displays | Pass |
| Delete event (logged out) | Navigate to delete URL | Redirected to login page | Pass |

### User Authentication

| Test | Action | Expected Result | Pass/Fail |
|---|---|---|---|
| Register new account | Fill out register form and submit | Account created, user logged in, redirected to home | Pass |
| Register flash message | Successful registration | Welcome flash message displays | Pass |
| Register - passwords not matching | Submit with mismatched passwords | Error message displays | Pass |
| Login valid credentials | Fill out login form and submit | User logged in and redirected to home | Pass |
| Login flash message | Successful login | Welcome back flash message displays | Pass |
| Login invalid credentials | Submit wrong username/password | Error message displays | Pass |
| Logout | Click Logout button | User logged out and redirected to home | Pass |
| Logout flash message | Successful logout | Logged out flash message displays | Pass |
| Navbar logged in | Log in to account | Navbar shows username and Logout button | Pass |
| Navbar logged out | Log out of account | Navbar shows Login and Register links | Pass |

### Discussion Page

| Test | Action | Expected Result | Pass/Fail |
|---|---|---|---|
| Page loads | Navigate to discussion page | All discussion threads display correctly | Pass |
| Pinned post | View discussion page | Pinned announcement displays at top | Pass |

### Flash Messages

| Test | Action | Expected Result | Pass/Fail |
|---|---|---|---|
| Login success | Log in | Green success message displays | Pass |
| Logout success | Log out | Blue info message displays | Pass |
| Register success | Register new account | Green success message displays | Pass |
| Event created | Create new event | Green success message displays | Pass |
| Event updated | Edit existing event | Green success message displays | Pass |
| Event deleted | Delete event | Green success message displays | Pass |
| Permission denied | Attempt to edit/delete another user's event | Red error message displays | Pass |

### Footer

| Test | Action | Expected Result | Pass/Fail |
|---|---|---|---|
| Facebook link | Click Facebook icon | Opens Facebook in new tab | Pass |
| Instagram link | Click Instagram icon | Opens Instagram in new tab | Pass |
| Twitter/X link | Click Twitter/X icon | Opens Twitter/X in new tab | Pass |
| Footer position | View any page | Footer stays at bottom of page | Pass |

---

## User Story Testing

| User Story | Test | Result |
|---|---|---|
| Easily navigate the website | Clicked all navbar links across all pages | Pass |
| View the website on all screen sizes | Tested on mobile, tablet and desktop | Pass |
| Create an account | Registered a new user account | Pass |
| View all upcoming running events | Navigated to events page and viewed all events | Pass |
| Create a new event | Logged in and created a new event via the form | Pass |
| Edit my own event | Edited an existing event as the creator | Pass |
| Delete my own event | Deleted an existing event as the creator | Pass |
| Receive clear feedback for actions | Flash messages confirmed for all key actions | Pass |
| Only owners can edit/delete events | Attempted to edit another user's event - denied | Pass |
| Unauthenticated users redirected | Accessed protected URLs while logged out | Pass |

---

## Validator Testing

### Python - CI Linter
All Python files were passed through the [CI Python Linter](https://pep8ci.herokuapp.com/) with no errors found.

Files tested:
- `club/views.py`
- `club/models.py`
- `club/urls.py`
- `club/forms.py`
- `runclubhub/urls.py`
- `runclubhub/settings.py`

### HTML - W3C Validator
All HTML templates were tested using the [W3C HTML Validator](https://validator.w3.org/) with no errors found.

Pages tested:
- Home page
- Events page
- Add Event page
- Edit Event page
- Delete Event page
- Discussion page
- Login page
- Register page

### CSS - Jigsaw Validator
The custom CSS file was tested using the [W3C CSS Validator (Jigsaw)](https://jigsaw.w3.org/css-validator/) with no errors found.

---

## Browser Testing

| Browser | Result |
|---|---|
| Google Chrome | All features working correctly |
| Safari | All features working correctly |
| Firefox | All features working correctly |

---

## Responsiveness Testing

The site was tested on the following screen sizes using Chrome DevTools:

| Device | Screen Size | Result |
|---|---|---|
| iPhone SE | 375px | Pass |
| iPhone 14 | 390px | Pass |
| iPad | 768px | Pass |
| Desktop | 1280px+ | Pass |

---

## Bugs

### Fixed Bugs

| Bug | Fix |
|---|---|
| Login form not submitting | Template was missing method="POST" and csrf_token. Fixed by rewriting the login template with Django's AuthenticationForm |
| Register page showing overwhelming help text | Fixed by rendering each field manually instead of using form.as_p |
| Flash messages not rendering | Fixed by adding MESSAGE_TAGS configuration to settings.py |
| @login_required redirecting to wrong URL | Fixed by adding LOGIN_URL = '/login/' to settings.py |
| Existing events breaking after adding created_by field | Fixed by setting null=True and blank=True on the created_by ForeignKey field |

### Unfixed Bugs

There are no known unfixed bugs at this time.

