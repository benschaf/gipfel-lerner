# Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

In this section, you need to convince the assessors that you have conducted enough testing to legitimately believe that the site works well.
Essentially, in this part, you should go over all of your project's features, and ensure that they all work as intended,
with the project providing an easy and straightforward way for the users to achieve their goals.

Feature-by-Feature Testing:

Go through each feature of your portfolio site and detail the testing process for each.

Explain the functionality and demonstrate how it aligns with the intended purpose. This could include:

- Navigation: Ensuring smooth transitions between pages, links directing to the correct destinations.
- Responsive Design: Checking for compatibility across various devices and screen sizes.
- Portfolio Display: Verifying that projects are properly showcased with accurate descriptions, images, and links.
- Contact Form: Testing the form submission process, ensuring the user receives a confirmation, and you receive the message.

User Experience Testing:

- Usability Testing: Have users (or simulated users) interact with the site and provide feedback. Document any issues encountered and the resolutions implemented.
- Accessibility Testing: Confirm compliance with accessibility standards (e.g., screen reader compatibility, proper alt text for images, keyboard navigation).

Compatibility Testing:

- Browser Compatibility: Testing on different browsers (Chrome, Firefox, Safari, Edge, etc.) to ensure consistent performance.
- Device Compatibility: Ensuring functionality across various devices (desktops, laptops, tablets, and mobile phones).
- Performance Testing (optional):
	- Speed and Load Testing: Tools like PageSpeed Insights or GTmetrix to check page load times and optimize where necessary.
	- Scalability Testing: Assess how the site handles increased traffic or usage.

Regression Testing:

After implementing fixes or updates, ensure that previous features and functionalities still work as intended. This prevents new changes from breaking existing features.

Documentation and Logs:

Maintain records of testing procedures, results, and any bugs encountered along with their resolutions. This helps demonstrate a systematic approach to testing and problem-solving.
User Feedback Incorporation:

If applicable, mention how user feedback has been taken into account and implemented to enhance the user experience.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML deployed source code. In the table below, the results are labeled by template file that would render the respective page. The results are validated using the live deployed version of the project.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| booking | cancel_session.html | ![screenshot](documentation/validation_html_cancel_session.png) | |
| booking | payment.html | ![screenshot](documentation/validation_html_payment.png) | |
| booking | payment_create.html | ![screenshot](documentation/validation_html_payment_create.png) | |
| booking | payment_success.html | ![screenshot](documentation/validation_html_payment_success.png) | |
| booking | schedule_success.html | ![screenshot](documentation/validation_html_schedule_success.png) | |
| core | about.html | ![screenshot](documentation/validation_html_about.png) | |
| core | faq.html | ![screenshot](documentation/validation_html_faq.png) | |
| core | index.html | ![screenshot](documentation/validation_html_index.png) | |
| templates | 404.html | ![screenshot](documentation/validation_html_404.png) | |
| templates | 500.html | ![screenshot](documentation/validation_html_500.png) | |
| templates | base_manage.html | ![screenshot](documentation/validation_html_base_manage.png) | |
| templates | usersession_list.html | ![screenshot](documentation/validation_html_usersession_list.png) | |
| tutor_market | add_tutor.html | ![screenshot](documentation/validation_html_add_tutor.png) | |
| tutor_market | calendly_information.html | ![screenshot](documentation/validation_html_calendly_information.png) | |
| tutor_market | edit_tutor.html | ![screenshot](documentation/validation_html_edit_tutor.png) | |
| tutor_market | student_dashboard.html | ![screenshot](documentation/validation_html_student_dashboard.png) | |
| tutor_market | tutor_confirm_delete.html | ![screenshot](documentation/validation_html_tutor_confirm_delete.png) | |
| tutor_market | tutor_dashboard.html | ![screenshot](documentation/validation_html_tutor_dashboard.png) | |
| tutor_market | tutor_detail.html | ![screenshot](documentation/validation_html_tutor_detail.png) | |
| tutor_market | tutor_list.html | ![screenshot](documentation/validation_html_tutor_list.png) | |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

![jigsaw badge](http://jigsaw.w3.org/css-validator/images/vcss-blue)

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | base.css | ![screenshot](documentation/validation_css_base_css.png) | |
| static | custom_bootstrap.css | ![screenshot](documentation/validation_css_custom_bootstrap_css.png) | |

The warnings are due to the vendor prefixes that are used in the CSS file. I added the prefixes using the [Autoprefixer](https://autoprefixer.github.io) tool. The prefixes are necessary for the CSS to work on all browsers.

There were no other issues with the CSS file.

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) via its command-line interface to validate all of my JavaScript files. for this I installed the jshint package as a dev dependency using the command `npm install jshint --save-dev`. After this I created a `.jshintrc` file in the `static/js` directory of the project with the following content in order to enable ES6 syntax:

```json
{
    "esversion": 6
}
```

I then ran the following command to validate all of my JavaScript files: `npx jshint <directory>/<filename.js>`:

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| booking | [payment.js](booking/static/booking/js/payment.js) | ![screenshot](documentation/validation_js_payment_js.png) | |
| booking | [payment_create.js](booking/static/booking/js/payment_create.js) | ![screenshot](documentation/validation_js_payment_create_js.png) | |
| core | [index.js](core/static/core/js/index.js) | ![screenshot](documentation/validation_js_index_js.png) | |
| static | [base.js](static/js/base.js) | ![screenshot](documentation/validation_js_base_js.png) | |
| tutor_market | [tutor_detail.js](tutor_market/static/tutor_market/js/tutor_detail.js) | ![screenshot](documentation/validation_js_tutor_detail_js.png) | |
| tutor_market | [tutor_list.js](tutor_market/static/tutor_market/js/tutor_list.js) | ![screenshot](documentation/validation_js_tutor_list_js.png) | |

There were no additional issues with the JavaScript files.

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

Files that are unchanged from the Django template have been excluded from the validation as they are known to be valid.

| Directory | File | PEP8 CI | Screenshot |
| --- | --- | --- | --- |
| booking | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/booking/admin.py) | ![screenshot](documentation/validation_py_admin_py.png) |
| booking | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/booking/forms.py) | ![screenshot](documentation/validation_py_forms_py.png) |
| booking | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/booking/models.py) | ![screenshot](documentation/validation_py_models_py.png) |
| booking | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/booking/urls.py) | ![screenshot](documentation/validation_py_urls_py.png) |
| booking | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/booking/views.py) | ![screenshot](documentation/validation_py_views_py.png) |
| booking | webhook_handler.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/booking/webhook_handler.py) | ![screenshot](documentation/validation_py_webhook_handler_py.png) |
| booking | webhooks.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/booking/webhooks.py) | ![screenshot](documentation/validation_py_webhooks_py.png) |
| calendly | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/calendly/urls.py) | ![screenshot](documentation/validation_py_urls_py.png) |
| calendly | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/calendly/views.py) | ![screenshot](documentation/validation_py_views_py.png) |
| root | copy-credits.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/copy-credits.py) | ![screenshot](documentation/validation_py_copy-credits_py.png) |
| core | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/core/admin.py) | ![screenshot](documentation/validation_py_admin_py.png) |
| core | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/core/models.py) | ![screenshot](documentation/validation_py_models_py.png) |
| core | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/core/urls.py) | ![screenshot](documentation/validation_py_urls_py.png) |
| core | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/core/views.py) | ![screenshot](documentation/validation_py_views_py.png) |
| root | custom_storages.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/custom_storages.py) | ![screenshot](documentation/validation_py_custom_storages_py.png) |
| gipfel_tutor | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/gipfel_tutor/settings.py) | ![screenshot](documentation/validation_py_settings_py.png) |
| gipfel_tutor | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/gipfel_tutor/urls.py) | ![screenshot](documentation/validation_py_urls_py.png) |
| tutor_market | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/tutor_market/forms.py) | ![screenshot](documentation/validation_py_forms_py.png) |
| tutor_market | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/tutor_market/models.py) | ![screenshot](documentation/validation_py_models_py.png) |
| tutor_market | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/tutor_market/urls.py) | ![screenshot](documentation/validation_py_urls_py.png) |
| tutor_market | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/benschaf/gipfel-tutor/main/tutor_market/views.py) | ![screenshot](documentation/validation_py_views_py.png) |

Test Files were validated, too:

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |

Additionaly to the final testing, pycodestyle was used frequently to test python files locally.

By running the command `pycodestyle --exclude=.vscode/*,*/migrations/* .` in the terminal, I was able to check for any PEP8 violations in all of my Python files. The `--exclude` flag was used to exclude the `.vscode` and `migrations` directories from the test as they are not written by me or automatically generated by Django.

There were no issues with the Python files.

## Browser Compatibility

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss testing the live/deployed site on various browsers.

Consider testing AT LEAST 3 different browsers, if available on your system.

You DO NOT need to use all of the browsers below, just pick any 3 (minimum).

Recommended browsers to consider:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)

**IMPORTANT**: You must provide screenshots of the tested browsers, to "prove" that you've actually tested them.

Please note, there are services out there that can test multiple browser compatibilities at the same time.
Some of these are paid services, but some are free.
If you use these, you must provide a link to the source used for attribution, and multiple screenshots of the results.

Sample browser testing documentation:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I've tested my deployed project manually on multiple browsers to check for compatibility issues. I've tested the project on the latest versions of the following browsers:

- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)

See the table below for the compatibility results:

| Browser | Landing | tutor list | tutor detail | tutor dashboard | payment | student dashboard | schedule success | payment success | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browser-chrome-landing.png) | ![screenshot](documentation/browser-chrome-tutor_list.png) | ![screenshot](documentation/browser-chrome-tutor_detail.png) | ![screenshot](documentation/browser-chrome-tutor_dashboard.png) | ![screenshot](documentation/browser-chrome-payment.png) | ![screenshot](documentation/browser-chrome-student_dashboard.png) | ![screenshot](documentation/browser-chrome-schedule_success.png) | ![screenshot](documentation/browser-chrome-payment_success.png) | Works as expected |
| Firefox | ![screenshot](documentation/browser-firefox-landing.png) | ![screenshot](documentation/browser-firefox-tutor_list.png) | ![screenshot](documentation/browser-firefox-tutor_detail.png) | ![screenshot](documentation/browser-firefox-tutor_dashboard.png) | ![screenshot](documentation/browser-firefox-payment.png) | ![screenshot](documentation/browser-firefox-student_dashboard.png) | ![screenshot](documentation/browser-firefox-schedule_success.png) | ![screenshot](documentation/browser-firefox-payment_success.png) | Works as expected |
| Edge | ![screenshot](documentation/browser-edge-landing.png) | ![screenshot](documentation/browser-edge-tutor_list.png) | ![screenshot](documentation/browser-edge-tutor_detail.png) | ![screenshot](documentation/browser-edge-tutor_dashboard.png) | ![screenshot](documentation/browser-edge-payment.png) | ![screenshot](documentation/browser-edge-student_dashboard.png) | ![screenshot](documentation/browser-edge-schedule_success.png) | ![screenshot](documentation/browser-edge-payment_success.png) | Works as expected |
| Safari | ![screenshot](documentation/browser-safari-landing.png) | ![screenshot](documentation/browser-safari-tutor_list.png) | ![screenshot](documentation/browser-safari-tutor_detail.png) | ![screenshot](documentation/browser-safari-tutor_dashboard.png) | ![screenshot](documentation/browser-safari-payment.png) | ![screenshot](documentation/browser-safari-student_dashboard.png) | ![screenshot](documentation/browser-safari-schedule_success.png) | ![screenshot](documentation/browser-safari-payment_success.png) | Works as expected |

There were no compatibility issues on any of the browsers tested.

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues. I've used the Chrome Developer Tools to simulate the devices. I have also tested the project on a physical Google Pixel 6 device.

| Device | Landing | tutor list | tutor detail | tutor dashboard | payment | student dashboard | schedule success | payment success | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools: iPhone 12 Pro) | ![screenshot](documentation/responsive-mobile-landing.png) | ![screenshot](documentation/responsive-mobile-tutor_list.png) | ![screenshot](documentation/responsive-mobile-tutor_detail.png) | ![screenshot](documentation/responsive-mobile-tutor_dashboard.png) | ![screenshot](documentation/responsive-mobile-payment.png) | ![screenshot](documentation/responsive-mobile-student_dashboard.png) | ![screenshot](documentation/responsive-mobile-schedule_success.png) | ![screenshot](documentation/responsive-mobile-payment_success.png) | Works as expected |
| Tablet (DevTools: iPad Air) | ![screenshot](documentation/responsive-tablet-landing.png) | ![screenshot](documentation/responsive-tablet-tutor_list.png) | ![screenshot](documentation/responsive-tablet-tutor_detail.png) | ![screenshot](documentation/responsive-tablet-tutor_dashboard.png) | ![screenshot](documentation/responsive-tablet-payment.png) | ![screenshot](documentation/responsive-tablet-student_dashboard.png) | ![screenshot](documentation/responsive-tablet-schedule_success.png) | ![screenshot](documentation/responsive-tablet-payment_success.png) | Works as expected |
| Desktop (1920 x 1080) | ![screenshot](documentation/responsive-desktop-landing.png) | ![screenshot](documentation/responsive-desktop-tutor_list.png) | ![screenshot](documentation/responsive-desktop-tutor_detail.png) | ![screenshot](documentation/responsive-desktop-tutor_dashboard.png) | ![screenshot](documentation/responsive-desktop-payment.png) | ![screenshot](documentation/responsive-desktop-student_dashboard.png) | ![screenshot](documentation/responsive-desktop-schedule_success.png) | ![screenshot](documentation/responsive-desktop-payment_success.png) | Works as expected |
| Google Pixel 6 | ![screenshot](documentation/responsive-pixel-landing.png) | ![screenshot](documentation/responsive-pixel-tutor_list.png) | ![screenshot](documentation/responsive-pixel-tutor_detail.png) | ![screenshot](documentation/responsive-pixel-tutor_dashboard.png) | ![screenshot](documentation/responsive-pixel-payment.png) | ![screenshot](documentation/responsive-pixel-student_dashboard.png) | ![screenshot](documentation/responsive-pixel-schedule_success.png) | ![screenshot](documentation/responsive-pixel-payment_success.png) | Works as expected |

> [!IMPORTANT]
> Tables have x-overflow on mobile. they do scroll though so they can be considered as working as intended.

There were no additional responsiveness issues on any of the devices tested.

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool in the Chrome Developer Tools to mainly check for accessibility and best practices but also to check for performance and SEO.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Landing | ![screenshot](documentation/lighthouse-landing-mobile.png) | ![screenshot](documentation/lighthouse-landing-desktop.png) | Some minor warnings |
| tutor list | ![screenshot](documentation/lighthouse-tutor_list-mobile.png) | ![screenshot](documentation/lighthouse-tutor_list-desktop.png) | Some minor warnings |
| tutor detail | ![screenshot](documentation/lighthouse-tutor_detail-mobile.png) | ![screenshot](documentation/lighthouse-tutor_detail-desktop.png) | Some minor warnings |
| tutor dashboard | ![screenshot](documentation/lighthouse-tutor_dashboard-mobile.png) | ![screenshot](documentation/lighthouse-tutor_dashboard-desktop.png) | Some minor warnings |
| payment | ![screenshot](documentation/lighthouse-payment-mobile.png) | ![screenshot](documentation/lighthouse-payment-desktop.png) | Some minor warnings |
| student dashboard | ![screenshot](documentation/lighthouse-student_dashboard-mobile.png) | ![screenshot](documentation/lighthouse-student_dashboard-desktop.png) | Some minor warnings |
| schedule success | ![screenshot](documentation/lighthouse-schedule_success-mobile.png) | ![screenshot](documentation/lighthouse-schedule_success-desktop.png) | Some minor warnings |
| payment success | ![screenshot](documentation/lighthouse-payment_success-mobile.png) | ![screenshot](documentation/lighthouse-payment_success-desktop.png) | Some minor warnings |

## Defensive Programming

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature01.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature02.png) |
| About | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature03.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature04.png) |
| Gallery | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature05.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature06.png) |
| Contact | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature07.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature08.png) |
| repeat for all remaining pages | x | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Another way of performing defensive testing is a simple Pass/Fail for each test.
The assessors prefer the above method, with the full test explained, but this is also acceptable in most cases.

When in doubt, use the above method instead, and delete the table below.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| repeat for all remaining pages | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## User Story Testing

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature09.png) |
| repeat for all remaining user stories | x |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### JavaScript (Jest Testing)

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I have used the [Jest](https://jestjs.io) JavaScript testing framework to test the application functionality.

In order to work with Jest, I first had to initialize NPM.

- `npm init`
- Hit `enter` for all options, except for **test command:**, just type `jest`.

Add Jest to a list called **Dev Dependencies** in a dev environment:

- `npm install --save-dev jest`

**IMPORTANT**: Initial configurations

When creating test files, the name of the file needs to be `file-name.test.js` in order for Jest to properly work.

Without the following, Jest won't properly run the tests:

- `npm install -D jest-environment-jsdom`

Due to a change in Jest's default configuration, you'll need to add the following code to the top of the `.test.js` file:

```js
/**
 * @jest-environment jsdom
 */

const { test, expect } = require("@jest/globals");
const { function1, function2, function3, etc. } = require("../script-name");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("index.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});
```

Remember to adjust the `fs.readFileSync()` to the specific file you'd like you test.
The example above is testing the `index.html` file.

Finally, at the bottom of the script file where your primary scripts are written, include the following at the bottom of the file.
Make sure to include the name of all of your functions that are being tested in the `.test.js` file.

```js
if (typeof module !== "undefined") module.exports = {
    function1, function2, function3, etc.
};
```

Now that these steps have been undertaken, further tests can be written, and be expected to fail initially.
Write JS code that can get the tests to pass as part of the Red-Green refactor process.

Once ready, to run the tests, use this command:

- `npm test`

**NOTE**: To obtain a coverage report, use the following command:

- `npm test --coverage`

Below are the results from the tests that I've written for this application:

| Test Suites | Tests | Screenshot |
| --- | --- | --- |
| 1 passed | 16 passed | ![screenshot](documentation/tests/js-test-coverage.png) |
| x | x | repeat for all remaining tests |

#### Jest Test Issues

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this section to list any known issues you ran into while writing your Jest tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

### Python (Unit Testing)

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

`pip3 install coverage`

`pip3 freeze --local > requirements.txt`

`coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/tests/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/tests/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/tests/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/tests/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/tests/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/tests/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/tests/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/tests/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/tests/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/tests/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/benschaf/gipfel-tutor/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Abenschaf%2Fgipfel-tutor%20label%3Abug&label=bugs)](https://github.com/benschaf/gipfel-tutor/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/benschaf/gipfel-tutor/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/benschaf/gipfel-tutor/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/benschaf/gipfel-tutor/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/benschaf/gipfel-tutor/issues/3) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/benschaf/gipfel-tutor)](https://github.com/benschaf/gipfel-tutor/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/benschaf/gipfel-tutor)](https://github.com/benschaf/gipfel-tutor/issues?q=is%3Aissue+is%3Aclosed)

Any remaining open issues can be tracked [here](https://github.com/benschaf/gipfel-tutor/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/benschaf/gipfel-tutor/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/benschaf/gipfel-tutor/issues/5) | Open |

## Unfixed Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

> [!NOTE]
> There are no remaining bugs that I am aware of.
