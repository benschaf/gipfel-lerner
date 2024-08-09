# GIPFEL TUTOR

[Experience our live website here!](https://gipfel-tutor-768a610dc54f.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/benschaf/gipfel-tutor)](https://github.com/benschaf/gipfel-tutor/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/benschaf/gipfel-tutor)](https://github.com/benschaf/gipfel-tutor/commits/main)
[![GitHub issues](https://img.shields.io/github/issues/benschaf/gipfel-tutor)](https://github.com/benschaf/gipfel-tutor/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/benschaf/gipfel-tutor)](https://github.com/benschaf/gipfel-tutor/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub repo size](https://img.shields.io/github/repo-size/benschaf/gipfel-tutor)](https://github.com/benschaf/gipfel-tutor)
[![Python version](https://img.shields.io/badge/python-3.12.2-blue?logo=python)](https://www.python.org/downloads/release/python-3121/)
[![npm version](https://img.shields.io/badge/npm-8.1.0-blue?logo=npm)](https://www.npmjs.com/package/npm)
[![Heroku](https://img.shields.io/badge/heroku-eco-purple?logo=heroku)](#)

🛑🛑🛑🛑🛑🛑🛑🛑🛑START OF NOTES (to be deleted)

GitHub now supports CALLOUTS in Markdown files.
There are some callouts already embedded in this application for you.
However, if you feel that you want to add more, there are certain ones you can use.

NOTE: the preview for callouts isn't yet supported in Gitpod/Codeanywhere/VSCode/etc.
You'll have to commit/push the changes to GitHub to see it in action.

> [!NOTE]
> BLUE: Highlights information that users should take into account, even when skimming.

> [!TIP]
> GREEN: Optional information to help a user be more successful.

> [!IMPORTANT]
> PURPLE: Crucial information necessary for users to succeed.

> [!WARNING]
> YELLOW: Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> RED: Negative potential consequences of an action.

Source: https://github.com/orgs/community/discussions/16925

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

Welcome to Gipfel Tutor, the pinnacle of personalized tutoring for Swiss students! Our Django-powered marketplace pairs you with the perfect tutor to conquer your academic peaks. Quick, simple, and effective — scale new heights in learning with us!


![screenshot](documentation/mockup.png)

source: [amiresponsive](https://ui.dev/amiresponsive?url=https://gipfel-tutor-768a610dc54f.herokuapp.com)

> [!NOTE]
> **Our Mission**:
>
> "Connect learners with a highly suitable tutor for their specific **needs** and **preferences**, within **48 hours*."

**Better Matching system**:
    The platform offers a sophisticated matching system that leverages detailed tutor profiles. Tutors are required to provide a comprehensive description of their experience, subjects they want to teach, and teaching values (via tags they can select). Additionally, students can filter their search using relevant tags associated with the tutor's expertise. A star rating system further helps students find a tutor that closely aligns with their needs.

## UX

The design process for Gipfel Tutor was guided by the principles of **simplicity**, **clarity**, and **efficiency**. The site's **minimalist** aesthetic ensures that users can easily navigate the
AAAAAAÄÄÄÄBLA BLA BLA IMPROVEp

### Colour Scheme

The colour scheme follows a **bright and engaging** palette that is both **professional** and **friendly**. It suits the **educational** theme of the site and is designed to appeal to a younger student and tutor demographic.

- Selective Yellow: `#FFB703` used for Primary emphasis.
- UT Orange: `#FB8500` used for secondary emphasis.
- Sky blue: `#8ECAE6` used for light emphasis.
- Blue Green: `#219EBC` used for darker emphasis.
- Prussian Blue: `#023047` used for dark bakgrounds.

I used [coolors.co](https://coolors.co/8ecae6-219ebc-023047-ffb703-fb8500) to generate my colour palette.

![screenshot](documentation/coolors.png)

I've used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

**File**: [base.css](static/css/base.css)
```css
:root {
    --my-blue-green: #219EBC;
    --my-prussian-blue: #023047;
    --my-ut-oragne: #FB8500;
    --my-font-serif: "Noto serif", Arial, serif;
}
```

Additionally I've adapted the bootstrap variables to match the colour scheme. This was done according to [a blogpost by bootstrap](https://blog.getbootstrap.com/2022/05/16/using-bootstrap-css-vars/).

**File**: [custom_bootstrap.css](static/css/custom_bootstrap.css)
```css
:root,
[data-bs-theme=light] {

  /* Custom Styles */
  --bs-black: #0f0f0f;

  --bs-light: #f2f2f2;
  --bs-light-rgb: 242, 242, 242;

  --bs-body-bg: #fff;
  --bs-body-bg-rgb: 255, 255, 255;

  --bs-primary: #FFB703;
  --bs-primary-rgb: 255, 183, 3;
  --bs-primary-shaded: #FFC533;

  --bs-secondary: #8ecae6;
  --bs-secondary-rgb: 142, 202, 230;
  --bs-secondary-shaded: #ABD8ED;

  --bs-dark: #023047;
  --bs-dark-rgb: 2, 48, 71;
  --bs-dark-shaded: #034363;

  --bs-btn-light: #C3EAFD;
  --bs-btn-light-rgb: 195, 234, 253;
  --bs-btn-light-shaded: #9CDCFC;

  --bs-success: #198754;
  --bs-success-rgb: 25, 135, 84;
  --bs-success-shaded: #2CAE6A;

  --bs-border-style: none;
  --bs-border-radius: 1.125rem;
  --bs-border-radius-lg: 2rem;

  --bs-font-sans-serif: "Noto Sans", "Liberation Sans", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";

  ...
}
```

### Typography


- [Noto Sans](https://fonts.google.com/specimen/Noto+Sans) was used for body text to ensure readability, accessibility, and familiarity.
- [Noto Serif](https://fonts.google.com/specimen/Noto+Serif) was used for titles and headings to provide a contrast with the sans-serif body text.
- [Font Awesome](https://fontawesome.com) was used for all icons on the site, providing a consistent and professional look.

## User Stories

The user stories are based on the user personas (To be found at the bottom of the document under **Design Thinking Process**) and the features of the app. They are written from the perspective of the user and describe the actions they can take on the site.

Each user story is followed by a set of acceptance criteria that must be met for the story to be considered complete.


> [!IMPORTANT]
> Make sure to also check out the [User Story Map](https://github.com/users/benschaf/projects/12/views/3) which was used extensively during the development process. It provides a more visual representation of the user stories and shows them **grouped by epics** along with their **priority** and **status**.

### Viewing and navigation

| User Story | Acceptance Criteria |
| --- | --- |
| As a **first time visitor**, I want to be able to understand the purpose of the site so that I can decide if I want to sign up. | 1. The homepage should clearly explain the purpose of the site. <br> 2. The homepage should have a call-to-action button to sign up. |
| As a **student**, I want to be able to view a list of tutors so that I can choose the best tutor for my needs. | 1. The site should have a page that lists all available tutors. <br> 2. Each tutor should have at least their profile picture, name, and hourly rate displayed.<br> 3. There should be obvious "book trial lesson" CTA Buttons. |
| _NOT MVP:_ As a **student**, I want to be able to like and save tutors so that I can easily find them later. | |

### Searching, filtering, and sorting

| User Story | Acceptance Criteria |
| --- | --- |
| As a **student**, I want to be able to filter tutors based on teaching experience and ratings so that I can choose a highly qualified tutor. | 1. The site should have a filter option to select tutors based on preference tags. <br> 2. The site should have a filter option to select tutors based taught subjects. |
| As a **student**, I want to be able to sort tutors based on hourly rates and ratings so that I can find an affordable and highly rated tutor. | 1. The site should have a sorting option to sort tutors based on hourly rates. <br> 2. The site should have a sorting option to sort tutors based on ratings. |
| As a **student**, I want to be able to search for tutors based on their name, description, subject expertise, and teaching values so that I can find a tutor that closely aligns with my needs. | 1. The search bar should have the ability to search for tutors by their name. <br> 2. The search bar should have the ability to search for tutors based on their description. <br> 3. The search bar should have the ability to search for tutors based on their subject expertise. <br> 4. The search bar should have the ability to search for tutors based on their teaching values. Those Values should be implemented using Tags the tutors can pick from. (limited amount of picks to ensure diversity) |

### Registration and user Accounts

| User Story | Acceptance Criteria |
| --- | --- |
| As a **user**, I want to be able to create either a student or tutor account so that I can access the platform. | 1. The platform should provide an option to create a student or tutor account. |
| As a **user**, I want to be able to log in and log out of my account so that I can access my profile and bookings. | 1. The platform should have a login functionality.<br>2. The platform should have a logout functionality. |
| As a **user**, I want to be able to reset my password in case I forget it so that I can regain access to my account. | 1. The platform should provide a password reset option. |
| As a **user**, I want to receive a confirmation email after registering so that I can verify my account. | 1. The platform should send a confirmation email upon successful registration.<br>2. The email should enable account email verification |
| As a **student**, I want to be able to see my booking history, upcoming lessons, payment details, and my liked tutors so that I can manage my account. | 1. The student's account should display booking history.<br>2. The student's account should display upcoming lessons.<br>3. The student's account should display payment details.<br>4. The student's account should display liked tutors. |
| As a **tutor**, I want to be able to see my booking history, upcoming lessons, bank details, and my currently booked students so that I can manage my account. | 1. The tutor's account should display booking history.<br>2. The tutor's account should display upcoming lessons.<br>3. The tutor's account should display bank details.<br>4. The tutor's account should display currently booked students. |

### Tutor profiles

| User Story | Acceptance Criteria |
| --- | --- |
| As a **student**, I want to be able to view detailed tutor profiles so that I can learn more about the tutor's experience and teaching values. | 1. Each tutor should have a detailed profile page with at least their name, profile picture, hourly rate, description, and teaching values(implemented using Tags they can pick from). <br> 2. The profile page should also display the tutor's ratings and reviews. |
| As a **tutor**, I want to be able to create a detailed tutor profile so that students can learn more about me. | 1. The platform should provide a feature to create a detailed tutor profile.<br>2. There should be some form of enhanced Text editing tools. |
| As a **tutor**, I want to be able to set my availability and hourly rates so that students can book lessons with me. | 1. The tutor should be able to set their availability.<br>2. The tutor should be able to set their hourly rates. |
| As a **tutor**, I want to be able to receive booking requests from students so that I can confirm lessons. | 1. The tutor should receive booking requests from students.<br>2. He should be able to answer to the requests. |
| As a **student**, I want to be able to leave a review and rating for a tutor after a lesson so that other students can benefit from my experience. | 1. The student should have the option to leave a review for a tutor after a lesson.<br>2. The student should have the option to leave a rating for a tutor after a lesson. |

### Booking and scheduling

| User Story | Acceptance Criteria |
| --- | --- |
| As a **student**, I want to be able to schedule regular lessons with a tutor so that I can improve my academic performance. | 1. The student should be able to schedule regular lessons with a tutor. |
| As a **student**, I want to be able to pay for lessons online so that I can easily book and confirm lessons. | 1. The student should have the option to pay for lessons online. |
| As a **student**, I want to be notified of successful or failed payments so that I can keep track of my bookings. | 1. The student should receive notifications for successful payments.<br>2. The student should receive notifications for failed payments. |
| _NOT MVP:_ As a **student**, I want to be able to book a trial lesson with a tutor so that I can see if the tutor is a good fit for me. |

### Admin

| User Story | Acceptance Criteria |
| --- | --- |
| As an **admin**, I want to be able to add, edit, and delete tutors so that I can manage the platform. | 1. The admin should have the ability to add tutors.<br>2. The admin should have the ability to edit tutors.<br>3. The admin should have the ability to delete tutors. |
| As an **admin**, I want to be able to view and manage user accounts so that I can ensure the security of the platform. | 1. The admin should have the ability to view user accounts.<br>2. The admin should have the ability to manage user accounts. |
| As a **Site Owner**, I want the site to Employ Search Engine Optimisation (SEO) techniques to improve audience reach. (Compare LO3 in Code Institute Project Requirements) | 1. The site should employ SEO techniques to improve audience reach. |
| _NOT MVP:_ As an **admin**, I want to be able to view and manage bookings and payments so that I can ensure the smooth operation of the platform. |

### Marketing and Business Strategy

| User Story | Acceptance Criteria |
| --- | --- |
| As a **Site Owner**, I want to have a Facebook Business Page to promote the site and attract more users. (Compare LO5 in Code Institute Project Requirements) | 1. The Site Owner should have a Facebook Business Page to promote the site. |
| As a **Site Owner**, I want to provide a Newsletter to keep site visitors informed about new features and updates. (Compare LO5 in Code Institute Project Requirements) | 1. The Site Owner should provide a Newsletter to keep site visitors informed. |
| As a **Site Owner**, I want to have a documentation of the ecommerce business model. (Compare LO6 in Code Institute Project Requirements) | 1. The Site Owner should have documentation of the ecommerce business model. |

## Wireframes

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑 START OF NOTES (to be deleted)

In this section, display your wireframe screenshots using a Markdown `table`.
Instructions on how to do Markdown `tables` start on line #213 on this site: https://pandao.github.io/editor.md/en.html

Alternatively, dropdowns are a way to condense several wireframes into a collapsible menu to save space.
Dropdowns in Markdown are considered some of the only acceptable HTML components that are allowed for assessment purposes.

⚠️ **IMPORTANT**! ⚠️ **IMPORTANT**! ⚠️ **IMPORTANT**! ⚠️
The example below uses the `details` and `summary` code elements.
However, for these scripts to work, I've had to add spaces within the `< >` elements.

You MUST remove these spaces for it to work properly on your own README/TESTING files.
Remove the spaces within the `< >` brackets for the `details` and `summary` code elements,
for the Mobile, Tablet, and Desktop wireframes.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [draw.io](https://balsamiq.com/wireframes) to design my site wireframes.

View the [original draw.io file](https://drive.google.com/file/d/1OUjOdhZI-Dq6OR5pPkPgPQIQ4jyU9k51/view?usp=sharing) of the wireframes. (click on the "Open with" button and select "draw.io")

<details>
<summary>Click to expand wireframes</summary>
| Page | Mobile Wireframe | Tablet Wireframe | Desktop Wireframe |
| --- | --- | --- | --- |
| Landing Page | ![screenshot](documentation/wireframe-landing-mobile.png) | ![screenshot](documentation/wireframe-landing-tablet.png) | ![screenshot](documentation/wireframe-landing-desktop.png) |
| Tutor List | ![screenshot](documentation/wireframe-list-mobile.png) | ![screenshot](documentation/wireframe-list-tablet.png) | ![screenshot](documentation/wireframe-list-desktop.png) |
| Tutor Detail | ![screenshot](documentation/wireframe-detail-mobile.png) | ![screenshot](documentation/wireframe-detail-tablet.png) | ![screenshot](documentation/wireframe-detail-desktop.png) |
| Schedule / Payment Success | ![screenshot](documentation/wireframe-schedule-mobile.png) | ![screenshot](documentation/wireframe-schedule-tablet.png) | ![screenshot](documentation/wireframe-schedule-desktop.png) |
| Payment (Checkout) | ![screenshot](documentation/wireframe-payment-mobile.png) | ![screenshot](documentation/wireframe-payment-tablet.png) | ![screenshot](documentation/wireframe-payment-desktop.png) |
| Student Dashboard | ![screenshot](documentation/wireframe-student-dashboard-mobile.png) | ![screenshot](documentation/wireframe-student-dashboard-tablet.png) | ![screenshot](documentation/wireframe-student-dashboard-desktop.png) |
| Tutor Dashboard | ![screenshot](documentation/wireframe-tutor-dashboard-mobile.png) | ![screenshot](documentation/wireframe-tutor-dashboard-tablet.png) | ![screenshot](documentation/wireframe-tutor-dashboard-desktop.png) |
| Single Forms (Allauth forms / Tutor Profile forms) | ![screenshot](documentation/wireframe-forms-mobile.png) | ![screenshot](documentation/wireframe-forms-tablet.png) | ![screenshot](documentation/wireframe-forms-desktop.png) |
| FAQ | ![screenshot](documentation/wireframe-faq-mobile.png) | ![screenshot](documentation/wireframe-faq-tablet.png) | ![screenshot](documentation/wireframe-faq-desktop.png) |
| About | ![screenshot](documentation/wireframe-about-mobile.png) | ![screenshot](documentation/wireframe-about-tablet.png) | ![screenshot](documentation/wireframe-about-desktop.png) |
| Calendly Information | ![screenshot](documentation/wireframe-calendly-mobile.png) | ![screenshot](documentation/wireframe-calendly-tablet.png) | ![screenshot](documentation/wireframe-calendly-desktop.png) |
</summary>


## Features

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑 START OF NOTES (to be deleted)

In this section, you should go over the different parts of your project,
and describe each in a sentence or so.

You will need to explain what value each of the features provides for the user,
focusing on who this website is for, what it is that they want to achieve,
and how your project is the best way to help them achieve these things.

For some/all of your features, you may choose to reference the specific project files that implement them.

IMPORTANT: Remember to always include a screenshot of each individual feature!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

### Existing Features

- **YOUR-TITLE-FOR-FEATURE-#1**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/features/feature01.png)

- **YOUR-TITLE-FOR-FEATURE-#2**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/features/feature02.png)

- **YOUR-TITLE-FOR-FEATURE-#3**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/features/feature03.png)

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑 START OF NOTES (to be deleted)

Repeat as necessary for as many features as your site contains.

Hint: the more, the merrier!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

### Future Features

- Feedback on singular lessons
- Chat system for students and tutors

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑 START OF NOTES (to be deleted)

Do you have additional ideas that you'd like to include on your project in the future?
Fantastic! List them here!
It's always great to have plans for future improvements!
Consider adding any helpful links or notes to help remind you in the future, if you revisit the project in a couple years.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- YOUR-TITLE-FOR-FUTURE-FEATURE-#1
    - Any additional notes about this feature.
- YOUR-TITLE-FOR-FUTURE-FEATURE-#2
    - Any additional notes about this feature.
- YOUR-TITLE-FOR-FUTURE-FEATURE-#3
    - Any additional notes about this feature.

## Tools & Technologies Used

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑 START OF NOTES (to be deleted)

In this section, you should explain the various tools and technologies used to develop the project.
Make sure to put a link (where applicable) to the source, and explain what each was used for.
Some examples have been provided, but this is just a sample only, your project might've used others.
Feel free to delete any unused items below as necessary.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- ⚠️⚠️ REQUIRED <-- delete me ⚠️⚠️
- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- ⚠️⚠️ CHOOSE ONLY ONE <-- delete me ⚠️⚠️
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![Codeanywhere](https://img.shields.io/badge/Codeanywhere-grey?logo=ebox&logoColor=7F3F98)](https://codeanywhere.com) used as a cloud-based IDE for development.
- [![VSCode](https://img.shields.io/badge/VSCode-grey?logo=visualstudiocode&logoColor=007ACC)](https://code.visualstudio.com) used as my local IDE for development.
- ⚠️⚠️ CHOOSE ALL APPLICABLE <-- delete me ⚠️⚠️
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.
- [![jQuery](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) used for user interaction on the site.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- ⚠️⚠️ CHOOSE ONLY ONE <-- delete me ⚠️⚠️
- [![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-grey?logo=githubpages&logoColor=222222)](https://pages.github.com) used for hosting the deployed front-end site.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- ⚠️⚠️ CHOOSE ONLY ONE (if applicable) <-- delete me ⚠️⚠️
- [![Bootstrap](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Materialize](https://img.shields.io/badge/Materialize-grey?logo=materialdesign&logoColor=F5A5A8)](https://materializecss.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- ⚠️⚠️ CHOOSE ALL APPLICABLE <-- delete me ⚠️⚠️
- [![Google Sheets](https://img.shields.io/badge/Google_Sheets-grey?logo=googlesheets&logoColor=34A853)](https://docs.google.com/spreadsheets) used for storing data from my Python app.
- [![Jest](https://img.shields.io/badge/Jest-grey?logo=jest&logoColor=c21325)](https://jestjs.io) used for automated JavaScript testing.
- [![Flask](https://img.shields.io/badge/Flask-grey?logo=flask&logoColor=000000)](https://flask.palletsprojects.com) used as the Python framework for the site.
- [![MongoDB](https://img.shields.io/badge/MongoDB-grey?logo=mongodb&logoColor=47A248)](https://www.mongodb.com) used as the non-relational database management with Flask.
- [![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-grey?logo=sqlalchemy&logoColor=D71F00)](https://www.sqlalchemy.org) used as the relational database management with Flask.
- [![Django](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) used as the Python framework for the site.
- [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) used as the relational database management.
- [![PostgreSQL by Code Institute](https://img.shields.io/badge/PostgreSQL_by_Code_Institute-grey?logo=okta&logoColor=F05223)](https://dbs.ci-dbs.net) used as the Postgres database from Code Institute.
- [![ElephantSQL](https://img.shields.io/badge/ElephantSQL-grey?logo=postgresql&logoColor=36A6E2)](https://www.elephantsql.com) used as the Postgres database.
- [![Cloudinary](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) used for online static file storage.
- [![WhiteNoise](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) used for serving static files with Heroku.
- [![Stripe](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) used for online secure payments of ecommerce products/services.
- [![Gmail API](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) used for sending emails in my application.
- [![MailChimp](https://img.shields.io/badge/MailChimp-grey?logo=mailchimp&logoColor=FFE01B)](https://mailchimp.com) used for sending newsletter subscriptions.
- [![AWS S3](https://img.shields.io/badge/AWS_S3-grey?logo=amazons3&logoColor=569A31)](https://aws.amazon.com/s3) used for online static file storage.
- [![Balsamiq](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) used for creating wireframes.
- [![Figma](https://img.shields.io/badge/Figma-grey?logo=figma&logoColor=F24E1E)](https://www.figma.com) used for creating wireframes.
- [![Canva](https://img.shields.io/badge/Canva-grey?logo=canva&logoColor=00C4CC)](https://www.canva.com/p/canvawireframes) used for creating wireframes.
- [![Google Maps API](https://img.shields.io/badge/Google_Maps_API-grey?logo=googlemaps&logoColor=4285F4)](https://developers.google.com/maps) used as an interactive map on my site.
- [![Leaflet](https://img.shields.io/badge/Leaflet-grey?logo=leaflet&logoColor=199900)](https://leafletjs.com) used as a free open-source interactive map on my site.
- [![Font Awesome](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) used for the icons.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.

- ![calendly_api](https://img.shields.io/badge/-Calendly%20API-1A1A1A?style=flat&logo=calendly)
- ![django template support](https://img.shields.io/badge/-Django%20Template%20Support-092E20?style=flat&logo=django) used to format the template .html files
- ![djlint](https://img.shields.io/badge/-DjLint-092E20?style=flat&logo=django) used to lint and format the Django code
- ![django vscode extension](https://img.shields.io/badge/-Django%20VSCode%20Extension-092E20?style=flat&logo=django) used to provide Django support in VSCode

## User Journey Flowchart
[flowchart link](https://drive.google.com/file/d/1k-WFUWeaEafaomXcuk4rCSmGXS4WIFbf/view?usp=sharing)

## Database Design

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models.
Understanding the relationships between different tables can save time later in the project.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑 START OF NOTES (to be deleted)

Using your defined models (one example below), create an ERD with the relationships identified.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

```python
class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
```

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑 START OF NOTES (to be deleted)

A couple recommendations for building free ERDs:
- [Draw.io](https://draw.io)
- [Lucidchart](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning)

A more comprehensive ERD can be auto-generated once you're
at the end of your development stages, just before you submit.
Follow the steps below to obtain a thorough ERD that you can include.
Feel free to leave the steps in the README for future use to yourself.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

### Initial ERD

[dbdiagram link](https://dbdiagram.io/d/ERD_tutor_service-667c0ec99939893dae536ebe)

### Final ERD

I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:
- In the terminal: `sudo apt update`
- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
- then type `Y` to proceed
- then: `pip3 install django-extensions pygraphviz`
- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- back in the terminal: `python3 manage.py graph_models -a -o erd.png`
- dragged the new `erd.png` file into my `documentation/` folder
- removed `'django_extensions',` from my `INSTALLED_APPS`
- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

![erd](documentation/erd.png)
source: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)


## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/benschaf/gipfel-tutor/projects) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑 START OF NOTES (to be deleted)

Consider adding a basic screenshot of your Projects Board.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://github.com/benschaf/gipfel-tutor/issues) served as an another Agile tool.
There, I used my own **User Story Template** to manage user stories.

It also helped with milestone iterations on a weekly basis.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑 START OF NOTES (to be deleted)

Consider adding a screenshot of your Open and Closed Issues.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- [Open Issues](https://github.com/benschaf/gipfel-tutor/issues) [![GitHub issues](https://img.shields.io/github/issues/benschaf/gipfel-tutor)](https://github.com/benschaf/gipfel-tutor/issues)

    ![screenshot](documentation/gh-issues-open.png)

- [Closed Issues](https://github.com/benschaf/gipfel-tutor/issues?q=is%3Aissue+is%3Aclosed) [![GitHub closed issues](https://img.shields.io/github/issues-closed/benschaf/gipfel-tutor)](https://github.com/benschaf/gipfel-tutor/issues?q=is%3Aissue+is%3Aclosed)

    ![screenshot](documentation/gh-issues-closed.png)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

## Ecommerce Business Model

This site sells goods to individual customers, and therefore follows a `Business to Customer` model.
It is of the simplest **B2C** forms, as it focuses on individual transactions, and doesn't need anything
such as monthly/annual subscriptions.

It is still in its early development stages, although it already has a newsletter, and links for social media marketing.

Social media can potentially build a community of users around the business, and boost site visitor numbers,
especially when using larger platforms such a Facebook.

A newsletter list can be used by the business to send regular messages to site users.
For example, what items are on special offer, new items in stock,
updates to business hours, notifications of events, and much more!

## Search Engine Optimization (SEO) & Social Media Marketing

### Keywords

I've identified some appropriate keywords to align with my site, that should help users
when searching online to find my page easily from a search engine.
This included a series of the following keyword types

- Short-tail (head terms) keywords
- Long-tail keywords

I also played around with [Word Tracker](https://www.wordtracker.com) a bit
to check the frequency of some of my site's primary keywords (only until the free trial expired).

### Sitemap

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) to generate a sitemap.xml file.
This was generated using my deployed site URL: https://gipfel-tutor-768a610dc54f.herokuapp.com

After it finished crawling the entire site, it created a
[sitemap.xml](sitemap.xml) which I've downloaded and included in the repository.

### Robots

I've created the [robots.txt](robots.txt) file at the root-level.
Inside, I've included the default settings:

```
User-agent: *
Disallow:
Sitemap: https://gipfel-tutor-768a610dc54f.herokuapp.com/sitemap.xml
```

Further links for future implementation:
- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)

### Social Media Marketing

Creating a strong social base (with participation) and linking that to the business site can help drive sales.
Using more popular providers with a wider user base, such as Facebook, typically maximizes site views.

I've created a facebook business page for the site, and linked it to the site's footer.
[Facebook Business Page](https://www.facebook.com/profile.php?id=61563566265782)
![Facebook Business Page](documentation/images/marketing-facebook.png)

### Newsletter Marketing

I have incorporate a newsletter sign-up form on my application, to allow users to supply their
email address if they are interested in learning more.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑 START OF NOTES (to be deleted)

Option 1 (MailChimp):
- Sign up for a Mailchimp account
- This allows up to 2,500 subscription email sends per month
- Incorporate the code and scripts into your project like in the CI lessons.

Option 2 (Django):
- Create a custom newsletter app in your project, with a custom model.
- This method satisfies two assessment criteria:
    - include a newsletter
    - one of your custom models
- It doesn't need anything except the "email" on the model.
- Example:
    ```python
    class Newsletter(models.Model):
    email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return self.email
    ```
- Consider using the same `send_mail()` functionality used on the `webhook_handler.py` file.
    - You can trigger an email sent out to subscribed users when new products are added to the site!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Business and Costumer Goals

The business goals of the app are to provide a platform where students can find tutors for their specific needs and preferences. The app aims to set itself apart from other tutoring platforms by providing a better matching system that leverages detailed tutor profiles, ratings, and reviews. The app also aims to provide a seamless user experience for both students and tutors, with features such as detailed tutor profiles, booking requests, and online payments.

Maybe formulate project goals and map them to user stories - but this seems unnecessary at the moment.


## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

**IMPORTANT:**

- ⚠️ DO NOT update the environment variables to your own! These should NOT be included in this file; just demo values! ⚠️
- ⚠️ DO NOT update the environment variables to your own! These should NOT be included in this file; just demo values! ⚠️
- ⚠️ DO NOT update the environment variables to your own! These should NOT be included in this file; just demo values! ⚠️

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

The live deployed application can be found deployed on [Heroku](https://gipfel-tutor-768a610dc54f.herokuapp.com).

### PostgreSQL Database

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net).

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Signed-in to the CI LMS using my email address.
- An email was sent to me with my new Postgres Database.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method
> if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

### Amazon AWS

This project uses [AWS](https://aws.amazon.com) to store media and static files online, due to the fact that Heroku doesn't persist this type of data.

Once you've created an AWS account and logged-in, follow these series of steps to get your project connected.
Make sure you're on the **AWS Management Console** page.

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

	```shell
	[
		{
			"AllowedHeaders": [
				"Authorization"
			],
			"AllowedMethods": [
				"GET"
			],
			"AllowedOrigins": [
				"*"
			],
			"ExposeHeaders": []
		}
	]
	```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
	- Policy Type: **S3 Bucket Policy**
	- Effect: **Allow**
	- Principal: `*`
	- Actions: **GetObject**
	- Amazon Resource Name (ARN): **paste-your-ARN-here**
	- Click **Add Statement**
	- Click **Generate Policy**
	- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Id": "Policy1234567890",
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "Stmt1234567890",
					"Action": [
						"s3:GetObject"
					],
					"Effect": "Allow",
					"Resource": "arn:aws:s3:::your-bucket-name/*"
					"Principal": "*",
				}
			]
		}
		```

	- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click **Save**.
- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
	- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
	- Suggested Name: `group-gipfel-tutor` (group + the project name)
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
	- Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
	- You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.

		```shell
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": [
						"arn:aws:s3:::your-bucket-name",
						"arn:aws:s3:::your-bucket-name/*"
					]
				}
			]
		}
		```

	- Click **Review Policy**.
	- Suggested Name: `policy-gipfel-tutor` (policy + the project name)
	- Provide a description:
		- "Access to S3 Bucket for gipfel-tutor static files."
	- Click **Create Policy**.
- From **User Groups**, click your "group-gipfel-tutor".
- Click **Attach Policy**.
- Search for the policy you've just created ("policy-gipfel-tutor") and select it, then **Attach Policy**.
- From **User Groups**, click **Add User**.
	- Suggested Name: `user-gipfel-tutor` (user + the project name)
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `group-gipfel-tutor`
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
	- **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
	- This contains the user's **Access key ID** and **Secret access key**.
	- `AWS_ACCESS_KEY_ID` = **Access key ID**
	- `AWS_SECRET_ACCESS_KEY` = **Secret access key**

#### Final AWS Setup

- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click **Upload**.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://gipfel-tutor-768a610dc54f.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (verify your password and account)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
	- Any custom name, such as "Django" or gipfel-tutor
- You'll be provided with a 16-character password (API key).
	- Save this somewhere locally, as you cannot access this key again later!
	- `EMAIL_HOST_PASS` = user's 16-character API key
	- `EMAIL_HOST_USER` = user's own personal Gmail email address

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | user's own value |
| `AWS_SECRET_ACCESS_KEY` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user's own value |
| `EMAIL_HOST_USER` | user's own value |
| `SECRET_KEY` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |
| `USE_AWS` | True |

Heroku needs three additional files in order to deploy properly.

- requirements.txt
- Procfile
- runtime.txt

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

The **runtime.txt** file needs to know which Python version you're using:
1. type: `python3 --version` in the terminal.
2. in the **runtime.txt** file, add your Python version:
	- `python-3.9.19`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "user's own value")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("EMAIL_HOST_PASS", "user's own value")
os.environ.setdefault("EMAIL_HOST_USER", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user's own value")
os.environ.setdefault("STRIPE_SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_WH_SECRET", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/benschaf/gipfel-tutor)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/benschaf/gipfel-tutor.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/benschaf/gipfel-tutor)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/benschaf/gipfel-tutor)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss any differences between the local version you've developed, and the live deployment site on Heroku.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Credits

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

In this section you need to reference where you got your content, media, and extra help from.
It is common practice to use code from other repositories and tutorials,
however, it is important to be very specific about these sources to avoid plagiarism.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

### Content

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to provide attribution links to any borrowed code snippets, elements, or resources.
A few examples have been provided below to give you some ideas.

Ideally, you should provide an actual link to every resource used, not just a generic link to the main site!

⚠️⚠️ EXAMPLE LINKS - REPLACE WITH YOUR OWN ⚠️⚠️

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | version control | "How to Write a Git Commit Message" |
| [W3Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp) | entire site | responsive HTML/CSS/JS navbar |
| [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp) | contact page | interactive pop-up (modal) |
| [W3Schools](https://www.w3schools.com/css/css3_variables.asp) | entire site | how to use CSS :root variables |
| [Flexbox Froggy](https://flexboxfroggy.com/) | entire site | modern responsive layouts |
| [Grid Garden](https://cssgridgarden.com) | entire site | modern responsive layouts |
| [StackOverflow](https://stackoverflow.com/a/2450976) | quiz page | Fisher-Yates/Knuth shuffle in JS |
| [YouTube](https://www.youtube.com/watch?v=YL1F4dCUlLc) | leaderboard | using `localStorage()` in JS for high scores |
| [YouTube](https://www.youtube.com/watch?v=u51Zjlnui4Y) | PP3 terminal | tutorial for adding color to the Python terminal |
| [strftime](https://strftime.org) | CRUD functionality | helpful tool to format date/time from string |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |

### Media

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to provide attribution links to any images, videos, or audio files borrowed from online.
A few examples have been provided below to give you some ideas.

If you're the owner (or a close acquaintance) of all media files, then make sure to specify this.
Let the assessors know that you have explicit rights to use the media files within your project.

Ideally, you should provide an actual link to every media file used, not just a generic link to the main site!
The list below is by no means exhaustive. Within the Code Institute Slack community, you can find more "free media" links
by sending yourself the following command: `!freemedia`.

⚠️⚠️ EXAMPLE LINKS - REPLACE WITH YOUR OWN ⚠️⚠️

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pexels](https://www.pexels.com) | entire site | image | favicon on all pages |
| [Lorem Picsum](https://picsum.photos) | home page | image | hero image background |
| [Unsplash](https://unsplash.com) | product page | image | sample of fake products |
| [Pixabay](https://pixabay.com) | gallery page | image | group of photos for gallery |
| [Wallhere](https://wallhere.com) | footer | image | background wallpaper image in the footer |
| [This Person Does Not Exist](https://thispersondoesnotexist.com) | testimonials | image | headshots of fake testimonial images |
| [Audio Micro](https://www.audiomicro.com/free-sound-effects) | game page | audio | free audio files to generate the game sounds |
| [Videvo](https://www.videvo.net/) | home page | video | background video on the hero section |
| [TinyPNG](https://tinypng.com) | entire site | image | tool for image compression |

### Acknowledgements

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to provide attribution to any supports that helped, encouraged, or supported you throughout the development stages of this project.
A few examples have been provided below to give you some ideas.

⚠️⚠️ EXAMPLES ONLY - REPLACE WITH YOUR OWN ⚠️⚠️

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my partner (John/Jane), for believing in me, and allowing me to make this transition into software development.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.


## Design Thinking Process

### Empathize

For this stage, I created 4 user personas to represent the different types of users that would interact with the app.

For each persona, I considered their "5 Cs" (circumstances, constraints, context, criteria, and compensating behaviors) related to online tutoring. This helped me understand the needs and motivations of the users.

## Target Audience

The target audience for the app is primary and secondary school and gymnasium students in Switzerland (or their parents, especially in the case of primary students). The app is also aimed at university students who are looking to become tutors and earn extra income.

The user personas are:

1. **Lara** - A 14 year old student who is struggling with math and needs a tutor to help her understand the concepts better.

2. **Jonas** - A 17 year old student who is preparing for his final exams and needs a tutor to help him with exam preparation.

3. **Sophie** - The Mother of a 9 year old student who is looking for a tutor to help her child with homework and assignments.

4. **David** - A 20 year old university student who is looking to make some extra money by tutoring students in his area of expertise.

5 C's for each persona:

1. **Lara**
- **Circumstances** - Lara is a secondary school student who is struggling with math. She needs a tutor to help her overcome her fear of math and build confidence in her abilities.
- **Challenges** - Lara finds it difficult to grasp complex mathematical concepts and struggles with problem-solving techniques.
- **Context** - Lara is looking for a tutor who can provide personalized guidance and support to help her improve her math skills.
- **Criteria** - Lara is seeking a tutor who is patient, understanding, and skilled at breaking down complex concepts into simpler terms.
- **Compensating Behaviors** - Lara has been relying on online tutorials and videos, but she believes that a dedicated tutor can provide the individual attention she needs to excel in math.

2. **Jonas**
- **Circumstances** - Jonas is a high school student who is preparing for his final exams. He needs a tutor to help him develop effective study strategies and improve his exam performance.
- **Challenges** - Jonas struggles with time management and organizing study materials effectively for his exams.
- **Context** - Jonas is looking for a tutor who can provide structured study plans, practice exams, and effective revision techniques. He is also in a hurry to find a tutor as his exams are approaching.
- **Criteria** - Jonas is seeking a tutor who is experienced, knowledgeable, and can help him develop effective study habits and exam-taking strategies.
- **Compensating Behaviors** - Jonas has been using online study resources, but he believes that a tutor can provide personalized guidance and feedback to help him achieve better results in his exams.

3. **Sophie**
- **Circumstances** - Sophie is the mother of a 9-year-old student who is struggling with homework and assignments. She needs a tutor to provide additional support and guidance to her child.
- **Challenges** - Sophie's child finds it challenging to focus on homework and often gets overwhelmed with complex assignments.
- **Context** - Sophie is looking for a tutor who can create a structured learning environment, provide engaging activities, and offer personalized attention to her child's learning needs.
- **Criteria** - Sophie is seeking a tutor who is patient, creative, and experienced in teaching young children.
- **Compensating Behaviors** - Sophie has been trying to help her child with online resources, but she believes that a tutor can provide the necessary guidance and support to improve her child's academic performance.

4. **David**
- **Circumstances** - David is a 20-year-old university student who wants to become a tutor to share his expertise and earn extra income.
- **Challenges** - David faces difficulties in finding students who are interested in his area of expertise and matching his availability with their schedules.
- **Context** - David is looking for a platform that can connect him with students who need help in his specific field of expertise.
- **Criteria** - David is seeking a platform that provides a wide reach, efficient scheduling, and a secure payment system for his tutoring services.
- **Compensating Behaviors** - David has been exploring online tutoring platforms, but he believes that a dedicated platform can help him find more students and streamline the tutoring process.

### Define

Considering all the user Personas, I created a problem statement that would guide the design of the app.

The problem statement is:

"How might we create a platform that connects students with a highly suitable tutor for their specific needs and preferences, within 48 hours."

### Ideate

Considering the problem statement and the user personas, I brainstormed ideas for the app. I considered the features that would be most important to the users.

The Features are already sorted by priority although these priorities are subject to change, especially once the user stories are created.

1. **Lara**:
    - **p1** - Search for tutors based on subject and teaching values.
    - **p1** - View detailed tutor profiles with ratings and reviews.
    - **p2** - Book a trial lesson with a tutor - so she can see if the tutor is a good fit.

2. **Jonas**:
    - **p3** - Search for tutors based on subject and experiecne with a specific exam.
    - **p2** - Get in contact with a tutor to discuss study plans and exam strategies.
    - **p1** - Schedule regular lessons with a tutor to prepare for exams.

3. **Sophie**:
    - **p1** - Search for tutors based on subject and experience with young children.
    - **p1** - View tutor profiles with information on teaching values and activities.
    - **p1** - Schedule lessons with a tutor to help her child with homework and assignments.

4. **David**:
    - **p1** - Create a tutor profile with information on expertise and teaching values.
    - **p1** - Set availability and hourly rates for tutoring services.
    - **p1** - Receive booking requests from students and confirm lessons.

### Prototype

After ideating I created wireframes and content for the prototype of the site which is of course this repository.

Check out the full prototype including wireframes, user stories, and the working site by browsing around the readme and the repository. Also check out [the website](#) itself.

### Test

The prototype of the site was tested manually and progamatically to ensure that it is working as intended. Testing in the sense of design thinking has not been very extensive yet. This will be done in the future.



## UX

### Colour Scheme
I used a subtle green and white colour scheme to reflect the eco-friendly nature of the app. Coolors was used to generate the [colour palette](https://coolors.co/25a55f-2a2a2a-1c7b47-e6e6e6-57d992).

![screenshot](documentation/coolors-tonne.png)

⤴️ Screenshot of the colour palette from Coolors

- `--pigment-green: #25a55f` - used for primary buttons and highlights
- `--emerald: #57d992` - used for secondary buttons and highlights
- `--dark-spring-green: #1c7b47` - used for darker highlights
- `--jet: #2a2a2a` - used for bright backgrounds
- `--platinum: #e6e6e6` - used for light buttons

In order to have easier access to my colour scheme within my code i used CSS `:root` variables. These also include transparent versions of the colours for backgrounds.

```css
:root {
    --primary-color: #25a55f;
    --secondary-color: #57d992;
    --darker-secondary-color: #1c7b47;
    --primary-transparent-background: #25a55f45;
    --secondary-transparent-background: #1c7b47db;
    --dark-background: #2a2a2a;
    --light-background: #e6e6e6;
}
```

### Typography

- [Josefin Sans](https://fonts.google.com/specimen/Josefin+Sans) was used for all titles and subheadings. It's a modern, elegant font that stands out, complementing the otherwise minimalistic colour scheme and design.

- [Lato](https://fonts.google.com/specimen/Lato) was used for body and all other text. It's a clean, easy-to-read font that ensures a smooth user experience.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## Wireframes

## User Stories

Check out the [User Story Map](https://github.com/users/benschaf/projects/9/views/2) created for this project using Github Projects. It includes all user stories and makes them easier to manage as they are grouped by Epic and MoSCoW priority. Meaningful accepance criteria were added to each user story in order to make development more goal focused.

![screenshot](documentation/user-story-map.png)

⤴️ Screenshot of the User Story Map

### MoSCoW Prioritization: Must Have
Listed below are only the user stories that were prioritized as **Must Have**.

For all user stories and especially to see the acceptance criteria for each story listed below, please refer to the [User Story Map](https://github.com/users/benschaf/projects/9/views/2) instead. Note that MoSCoW prioritization of the user stories is frozen at the beginning of the last iteration to give more insight in the development process.

#### Epic: Landing Page optimization

* [#3](https://github.com/benschaf/waste-schedule/issues/3) As a user, I want an intuitive landing page that explains the app’s purpose and features clearly, so that I can quickly understand how to use it.
* [#13](https://github.com/benschaf/waste-schedule/issues/13) As a user I can instantly find relevant information for my area when visiting the website so that I can get right into setting up the reminders I came for

#### Epic: Picking a Schedule

* [#5](https://github.com/benschaf/waste-schedule/issues/5) As a user, I want to be able to browse waste collection schedules for my area without logging in, so that I can explore available options easily.
* [#6](https://github.com/benschaf/waste-schedule/issues/6) As a user, I want to only have to log in, when I want to subscribe to a schedule or make a schedule so that I can explore as much of the site without being distracted by a log in screen.
* [#14](https://github.com/benschaf/waste-schedule/issues/14) As a user I can click on a specific waste collection schedule from the search results and view detailed information about that schedule so that I can confirm that it's helpful for me
* [#15](https://github.com/benschaf/waste-schedule/issues/15) As a user, I can subscribe to waste collection schedules so that I receive timely reminders for upcoming collection events.

#### Epic: Managing and recieving reminders

* [#17](https://github.com/benschaf/waste-schedule/issues/17) As a user I can view a dashboard that provides relevant information on my subscribed schedules so that I can stay organized and have an overview of what I subscribed to.

#### Epic: Upload waste collection Schedules

* [#10](https://github.com/benschaf/waste-schedule/issues/10) As a user, I want to upload my community’s waste collection schedule, so that others can benefit from accurate information.

#### Epic: Rate and Comment on waste collection Schedules

* [#12](https://github.com/benschaf/waste-schedule/issues/12) As a user, I want to verify the accuracy of uploaded schedules by comparing them with official waste calendars or images, so that I can trust the data.
* [#11](https://github.com/benschaf/waste-schedule/issues/11) As a user, I want to rate and provide feedback on uploaded schedules to help the community, so that we collectively improve waste management.
* [#18](https://github.com/benschaf/waste-schedule/issues/18) As a user who commented on a schedule I can edit or delete my comment so that I can refine or retract my feedback.
* [#19](https://github.com/benschaf/waste-schedule/issues/19) As a user I can like or express appreciation for a specific waste collection schedule so that I can acknowledge well-maintained schedules.

### Flowchart
The following flowchart depicts possible user journeys in the waste management app. The app tries to let the user do as much as possible without having to sign up or log in. The user is only prompted to sign up when they want to subscribe to a schedule or create a new one. The flowchart also shows the user journey for the schedule builder and the dashboard.

![screenshot](documentation/flowchart.png)

⤴️ Flowchart of the user journey

## Features

### Existing Features

#### Inviting landing Page

When first visiting the site, users are greeted with a clean, modern and inviting landing page. It includes a hero image, a brief description of the site, and a call-to-action form to get started.

The landing page is designed to be simple and user-friendly, providing a quick overview of the site's purpose and functionality. It encourages users to explore the site further and get started with their waste management journey.

![screenshot](documentation/feature-landing.png)

⤴️ Screenshot of the landing page

relevant project files: [index.html](core/templates/core/index.html)

#### Navigation Bar with the most important links

The navigation bar is fixed at the top of the page, ensuring easy access to the most important links. It includes the logo (which is a link to the homepage), links to the schedule list, the schedule builder, the dashboard and login/register.

The navigation bar is designed to be simple and intuitive, providing quick access to the site's main features. It is responsive and collapses into a hamburger menu on smaller screens using the Bootstrap framework.

![screenshot](documentation/feature-navbar.png)

⤴️ Screenshot of the navigation bar

Some custom Javascript code was used to change the navigation bar's opacity once scrolling down the page. This was done to make the hero section of the landing page cleaner and more focused.

relevant project files: [base.html](templates/base.html), [index.js](static/js/index.js)

#### Footer with social media links

The footer includes links to the site's social media profiles, such as Facebook, Twitter, and Instagram. It also includes a link to the About page and displays a copyright notice.

The footer is designed to be simple and unobtrusive, providing additional information and links for users who are interested.

![screenshot](documentation/feature-footer.png)

⤴️ Screenshot of the footer

relevant project files: [base.html](templates/base.html)

#### About Page

The About page provides a brief overview of the site's purpose and the creator. It also identifies the site as a Code Institute student project.

The About page is designed to be informative, providing users with background information. It helps to establish trust and credibility with users, ensuring they feel comfortable using the site.

![screenshot](documentation/feature-about.png)

⤴️ Screenshot of the about page

relevant project files: [about.html](core/templates/core/about.html)

#### Schedule Search Bar and List

The schedule search bar allows users to search for their postcode and receive a list of waste collection schedules. The search bar is displayed prominently as the CTA (Call to Action) on the Landing page and in the Schedule List page.

Once the user has entered their postcode, they are presented with a list set of schedule cards that match their search criteria. From here, they can already like and/or subscribe to a schedule.

The schedule list has enabled pagination, so that the user can easily navigate through the list of schedules.

The search bar and list are designed to be simple and intuitive, providing users with a quick and easy way to find the information they need.

![screenshot](documentation/feature-search.png)

⤴️ Screenshot of the search bar and schedule list

A custom form validator using a regex pattern was used to ensure that the user enters a valid postcode and gets appropriate feedback if they don't.

```html
<div class="form-floating">
    <input type="text" id="postcodeInput" class="form-control rounded-corners"
        placeholder="Search by postcode" aria-label="Search by postcode"
        aria-describedby="button-addon2" pattern="^\d{5}$"
        title="Please enter a 5 digit postcode (only German postcodes are supported)" required>
    <label for="postcodeInput">Search by postcode</label>
</div>
```

relevant project files: [schedule_list.html](wasteschedules/templates/wasteschedules/schedule_list.html), [index.js](static/js/index.js)

#### Schedule Detail View

When a user clicks on a schedule card, they are taken to the schedule detail view. Here, they can see all the details of the schedule, including the waste types, collection days, title, location and description. They can also like and subscribe to the schedule.

Below the schedule details is a list of user comments, allowing users to share their thoughts and experiences with the schedule.

For the schedule as well as for each comment, the owner of the item can edit or delete it.

The schedule detail view is designed to be informative and engaging, providing users with all the information and possibilites to take action they need in one place.

![screenshot](documentation/feature-detail.png)

⤴️ Screenshot of a schedule detail view

relevant project files: [schedule_detail.html](wasteschedules/templates/wasteschedules/schedule_detail.html), [comments.js](static/js/comments.js), [only_schedule.js](static/js/only_schedule.js)

#### Basic superuser functionality

Besides the regular built in Django superuser functionality, I have added a custom superuser functionality that allows the superuser to delete or edit any schedule. This can be done while viewing any schedule detail page as a superuser.

This feature is very rudimentary and only allows the superuser to delete or edit schedules. It does not include any kind of moderation or approval process for schedules and there is no feedback to the owner of the schedule when a superuser deletes or edits a schedule.

relevant project files: [schedule_detail.html](wasteschedules/templates/wasteschedules/schedule_detail.html)

#### User Likes, Subscriptions, and Comments

Users can like and subscribe to schedules, as well as leave comments. This allows them to interact with the site and the community, providing feedback and sharing their experiences.

A like is a simple way for users to show their appreciation for a schedule. Other users can see how many likes a schedule has received - thereby indicating its popularity and reliability.

Subscribing to a schedule means that the user will be able to set up notifications for this schedule. A subscribed to schedule will be displayed on the user's dashboard. Subscriptions also contribute to indicate the reliability of a schedule.

Subscriptions and likes can be added and removed by the owner via the schedule list and schedule detail pages.

Comments allow users to share their thoughts and experiences on a schedule. They can ask questions, provide feedback, or share additional information. Comments are displayed below the schedule details and can be edited or deleted by the owner. Comments can be added, edited and deleted via the schedule detail page.

The like, subscribe and comment features are designed to encourage user interaction and engagement, creating a sense of community and trust.

![screenshot](documentation/feature-comments.png)

⤴️ Screenshot of the comments section and the like and subscribe buttons

relevant project files: [comments.js](static/js/comments.js), [schedule_detail.html](wasteschedules/templates/wasteschedules/schedule_detail.html), [schedule_list.html](wasteschedules/templates/wasteschedules/schedule_list.html), [dashboard.html](wasteschedules/templates/wasteschedules/dashboard.html)


#### Schedule Builder

The schedule builder allows users to create a new waste collection schedule. They can add waste types, collection days, and any additional notes. Once the schedule is created, it is added to the database and can be viewed by other users.

The schedule builder is split up into 3 steps:
### Schedule Builder
The schedule builder allows users to create a new waste collection schedule. It consists of three steps:

1. **Location Form:** Here the user can enter their postcode. If a schedule for this postcode already exists, the user is notified.

2. **Schedule Title / Description / Image Form:** Here the user can enter a title and description for the schedule. They can also upload an image to help validate the schedule.

3. **Collection Events Calendar Form:** Here the user can add collection events to the schedule. They can select the waste type and the collection day directly from a calendar. The calendar is implemented using the [FullCalendar](https://fullcalendar.io/) library. The user can add recurring events, such as weekly or monthly collections, as well as one-time events. The deletion of recurring events is not yet implemented because the FullCalendar library doesn't support it natively. Singular events and all events that are part of the same recurrence can be deleted. Compare [Issue #32](https://github.com/benschaf/waste-schedule/issues/32).

The schedule builder is designed to be intuitive and user-friendly, providing a step-by-step process for creating a new schedule. It allows users to contribute to the site and share their knowledge with the community. And it even includes a step-by-step progress bar!

| Location Form | Schedule Title / Description / Image Form | Collection Events Calendar Form |
| --- | --- | --- |
| ![screenshot](documentation/feature-builder1.png) | ![screenshot](documentation/feature-builder2.png) | ![screenshot](documentation/feature-builder3.png) |

relevant project files: [location_form.html](schedulebuilder/templates/schedulebuilder/location_form.html), [schedule_form.html](schedulebuilder/templates/schedulebuilder/schedule_form.html), [calendar.html](schedulebuilder/templates/schedulebuilder/calendar.html), [edit_calendar.js](static/js/edit_calendar.js)

#### Dashboard

The dashboard is a user-specific page that displays all the schedules the user has created. It also displays any schedules the user has subscribed to.

From the dashboard, the user can edit or delete their schedules. It provides a quick overview and a general starting point for established users that are already familiar with the site.


![screenshot](documentation/feature-dashboard.png)

⤴️ Screenshot of the dashboard

relevant project files: [dashboard.html](wasteschedules/templates/wasteschedules/dashboard.html)

#### Schedule Export

Users can export their schedules to their calendar app via an ics file. This allows them to receive notifications and reminders directly on their phone or computer. When Downloading a Schedule, a modal containing instructions on how to import the schedule into a calendar app is displayed.

The export feature is designed to provide users with a convenient way to receive reminders for their waste collection days. It ensures that users don't miss any important events and helps them stay organized.

![screenshot](documentation/feature-export.png)

⤴️ Screenshot of the export modal

relevant project files: [dashboard.html](wasteschedules/templates/wasteschedules/dashboard.html), [dasboard.js](static/js/dashboard.js)

#### User Registration and Login

Users can register for an account on the site, providing a username and password. Once registered, they can log in to the site using their credentials. They also have the option to register and sign in using their Google account. This feature is implemented using the Django Allauth package as well as the Google OAuth2 API.

The site tries to prompt the user to register or log in only when it is necessary. This means that the user can do as much as possible without having to sign up or log in. Only when the user has to perform any kind of CRUD operation or if they want to see their dashboard, they are asked to sign up or log in. For an overview of the user flow, see the [flowchart](#flowchart).

| | |
| --- | --- |
| ![screenshot](documentation/feature-register.png) | screenshot |

⤴️ Screenshot of the registration page

relevant project files: find the adapted Allauth templates in the [templates/account](templates/account) folder.

#### Django messages

Django messages are used to provide feedback to the user. They are displayed at the top of the page and disappear after a few seconds. They are used to confirm successful actions, such as creating a schedule, as well as to provide error messages, such as when a user tries to access a page they are not authorized to view.

The messages are designed to be unobtrusive and informative, providing users with feedback on their actions and helping them navigate the site.

| | |
| --- | --- |
| ![screenshot](documentation/feature-messages.png) | screenshot |

⤴️ Screenshot of a success message

relevant project files: [base.html](templates/base.html)

#### Basic superuser functionality

#### Custom 404 and 500 error pages

Custom 404 and 500 error pages are displayed when a user tries to access a page that does not exist or if there is an internal server error. The pages are designed to be informative and user-friendly, providing users with feedback on what went wrong and how to proceed.

| 404 Error Page | 500 Error Page |
| --- | --- |
| ![screenshot](documentation/feature-404.png) | ![screenshot](documentation/feature-500.png) |

⤴️ Screenshots of the error pages

relevant project files: [404.html](templates/404.html), [500.html](templates/500.html)

#### Responsive Design

The site is fully responsive and optimized for all devices. It looks great on mobile, tablet, and desktop screens, ensuring a smooth user experience no matter the device. The responsive design was implemented using the Bootstrap CSS framework. Custom CSS was used to create a unique design that fits the site's theme.

relevant project files: all template files and [style.css](static/css/style.css) (for custom styles)

### Future Features

All Ideas for Future Features are organized as user Stories by Epic and MoSCoW priority in the [User Story Map](https://github.com/users/benschaf/projects/9/views/2) - check it out, there are some good ideas in there!

These are my three favorite ideas for future features:
- **[Issue #8](https://github.com/benschaf/waste-schedule/issues/8) User Notifications**: A feature that sends users actual real time notifications to remind them of their waste collection days. Sadly, this feature is not in the scope of this project because it cant really be implemented when using a free Heroku account that isn't able to keep the server running all the time.
- **[Issue #40](https://github.com/benschaf/waste-schedule/issues/40) Gamification and Household sharing**: A feature that allows members of a household to share their schedules and compete / collaborate with each other. This feature would also include a leaderboard and achievements.
- **[Issue #41](https://github.com/benschaf/waste-schedule/issues/41) Local Waste Collection Services**: A feature that allows users to find local waste collection services in their area, such as recycling centers, composting facilities, and hazardous waste disposal sites.


## Tools & Technologies Used
- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![Bootstrap](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Jest](https://img.shields.io/badge/Jest-grey?logo=jest&logoColor=c21325)](https://jestjs.io) used for automated JavaScript testing.
- [![Django](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) used as the Python framework for the site.
- [![Django Allauth](https://img.shields.io/badge/Django_Allauth-grey?logo=django&logoColor=092E20)](https://docs.allauth.org/en/latest/) used for user registration and login.
- [![Django Crispy Forms](https://img.shields.io/badge/Django_Crispy_Forms-grey?logo=django&logoColor=092E20)](https://django-crispy-forms.readthedocs.io) used to style Django forms.
- [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) used as the relational database management.
- [![PostgreSQL by Code Institute](https://img.shields.io/badge/PostgreSQL_by_Code_Institute-grey?logo=okta&logoColor=F05223)](https://dbs.ci-dbs.net) used as the Postgres database from Code Institute.
- [![Cloudinary](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) used for online static file storage of the schedule images.
- [![WhiteNoise](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) used for serving static files with Heroku.
- [![Font Awesome](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) used for the icons.
- [![Bing Copilot](https://img.shields.io/badge/Bing_Copilot-grey)](https://copilot.microsoft.com/) Used to explain and help debug things.
- [![coolors](https://img.shields.io/badge/Coolors-grey)](https://coolors.co) used to generate the colour palette.
- [![draw.io](https://img.shields.io/badge/draw.io-grey?logo=diagrams.net&logoColor=F0A60A)](https://draw.io) used to design the wireframes.
- [![pixlr](https://img.shields.io/badge/Pixlr-grey?logo=pixlr&logoColor=FF0000)](https://pixlr.com) used to edit images.
- [![autoprefixer](https://img.shields.io/badge/Autoprefixer-grey?logo=autoprefixer&logoColor=000000)](https://autoprefixer.github.io) used to add vendor prefixes to CSS.
- [![Markdown Link Check](https://img.shields.io/badge/Markdown_Link_Check-grey?logo=markdown&logoColor=000000)](https://github.com/tcort/markdown-link-check) used to check for broken links in the documentation files.
- [![FullCalendar](https://img.shields.io/badge/FullCalendar-grey?logo=fullcalendar&logoColor=000000)](https://fullcalendar.io) used for the calendar in the schedule builder.
- [![ics.py](https://img.shields.io/badge/ics.py-grey?logo=python&logoColor=3776AB)](https://icspy.readthedocs.io) used to generate ics files for the schedule export.
- [![rrule.js](https://img.shields.io/badge/rrule.js-grey?logo=rrule&logoColor=000000)](https://www.npmjs.com/package/rrule?activeTab=readmes) used to generate recurring events in the schedule builder and extend the FullCalendar library.

## Database Design
A relational database was used for this project. The database schema was designed using [dbdiagram.io](https://dbdiagram.io) before development began. The schema was then implemented using Django's built-in ORM. Throughout the development process, the schema was adjusted and updated as needed. The initial and the final version of the schema can be found below.

### Initial ERD
At the core of the database design is the `Schedule` model. This model represents a waste collection schedule and includes fields for the schedule title, description, and image. On the left side of the ERD view below are models that allow users to like, comment on, and subscribe to schedules. On the right side are models that handle individual collection events. They mostly adhere to the [RRule standard](https://github.com/jkbrzt/rrule), which allows for complex recurring events to be defined.

![screenshot](documentation/erd-initial.png)

⤴️ the initial ERD

Link to the [initial ERD](https://dbdiagram.io/e/66178e7003593b6b61bbb163/6618fa1203593b6b61d512e4)

### Final ERD
I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:
- In the terminal: `sudo apt update`
- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
- then type `Y` to proceed
- then: `pip3 install django-extensions pygraphviz`
- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- back in the terminal: `python3 manage.py graph_models -a -o erd.png`
- dragged the new `erd.png` file into my `documentation/` folder
- removed `'django_extensions',` from my `INSTALLED_APPS`
- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

![erd](documentation/erd.png)

⤴️ the final ERD

source for django ERD generation: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)

**Note about migration files:** While debugging the project, migration files were deleted and recreated which results in the `migrations` folders only containing one migration file each. The migration history can be recreated in older versions of the github repository. Thanks for John from the tutor team for the help with debugging my migrations! (see [commit ea26c6f](https://github.com/benschaf/waste-schedule/commit/ea26c6f6037916747e75c8918a234437f2f3ae20))

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/benschaf/waste-schedule/projects) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, a user story map was created, and issues were managed in an Agile way. User stories were created using a custom **User Story Template**.

User stories are grouped by Epic and MoSCoW priority. The epics were determined before development began as part of the design process. In depth information about the conception of the idea for the site and the User Stories can be found under the Design Thinking Progress section at the bottom of this file.

Throughout the development process, user stories were reevaluated after each iteration and adjusted accordingly. At this time, they are frozen at the beginning of the last iteration to give more insight into the development process.

![screenshot](documentation/user-story-map.png)

⤴️ Screenshot of the User Story Map

#### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization as custom project fields to my user stories within the project settings on GitHub.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

### GitHub Issues

[GitHub Issues](https://github.com/benschaf/waste-schedule/issues) served as an another Agile tool.

Github issues was mainly used to track bugs and smaller feature requests that weren't big enough to be considered a user story. They also contain the user stories which means that filtering is key to keep an overview over the issues.

- [Open Issues](https://github.com/benschaf/waste-schedule/issues) [![GitHub issues](https://img.shields.io/github/issues/benschaf/waste-schedule)](https://github.com/benschaf/waste-schedule/issues)

    ![screenshot](documentation/gh-issues-open.png)

    ⤴️ Screenshot of the open issues (this screenshot shows open issues of an earlier date to showcase the structure of the issues throughout development. The actual list of currently open issues can be found by following the link above.)

- [Closed Issues](https://github.com/benschaf/waste-schedule/issues?q=is%3Aissue+is%3Aclosed) [![GitHub closed issues](https://img.shields.io/github/issues-closed/benschaf/waste-schedule)](https://github.com/benschaf/waste-schedule/issues?q=is%3Aissue+is%3Aclosed)

    ![screenshot](documentation/gh-issues-closed.png)

    ⤴️ Screenshot of the closed issues (the same note as above applies here as well.)

## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment
The live deployed application can be found deployed on [Heroku](https://tonne-waste-reminders-a6836f2888b0.herokuapp.com/).

### PostgreSQL Database

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net).

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Signed-in to the CI LMS using my email address.
- An email was sent to me with my new Postgres Database.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `CLOUDINARY_API_KEY` | user's own value |
| `CLOUDINARY_API_SECRET` | user's own value |
| `CLOUDINARY_CLOUD_NAME` | user's own value |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs three additional files in order to deploy properly.

- requirements.txt
- Procfile
- runtime.txt

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

The **runtime.txt** file needs to know which Python version you're using:
1. type: `python3 --version` in the terminal.
2. in the **runtime.txt** file, add your Python version:
	- `python-3.9.18`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os
os.environ.setdefault("CLOUDINARY_API_KEY", "user's own value")
os.environ.setdefault("CLOUDINARY_API_SECRET", "user's own value")
os.environ.setdefault("CLOUDINARY_CLOUD_NAME", "user's own value")
os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures: `python3 manage.py loaddata db6.json`
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/benschaf/waste-schedule)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/benschaf/waste-schedule.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/benschaf/waste-schedule)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/benschaf/waste-schedule)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits

### Content

<!-- CREDITS_START -->
All the Credits and hyperlinks can be found in the respective files on the indicated lines.

Note that the list of credits below is automatically generated from the project files using the [copy-credits.py](copy-credits.py) script.
The script was written by me, with much help from the Microsoft Edge Copilot.
| File | Notes | Source |
| --- | --- | --- |
| [index.html: Line 21](https://github.com/benschaf/waste-schedule/blob/main/core/templates/core/index.html#L21) | manual input validation using regex pattern | [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation) |
| [index.html: Line 22](https://github.com/benschaf/waste-schedule/blob/main/core/templates/core/index.html#L22) | regex Pattern (generated using Bing AI) | [www.bing.com](https://www.bing.com/chat) |
| [test_views.py: Line 60](https://github.com/benschaf/waste-schedule/blob/main/schedulebuilder/test_views.py#L60) | getting django messages from response | [stackoverflow.com](https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages) |
| [views.py: Line 412](https://github.com/benschaf/waste-schedule/blob/main/schedulebuilder/views.py#L412) | update_or_create | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#update-or-create) |
| [views.py: Line 413](https://github.com/benschaf/waste-schedule/blob/main/schedulebuilder/views.py#L413) | dict.get() | [www.w3schools.com](https://www.w3schools.com/python/ref_dictionary_get.asp) |
| [views.py: Line 466](https://github.com/benschaf/waste-schedule/blob/main/schedulebuilder/views.py#L466) | get_kind_display() | [docs.djangoproject.com](https://docs.djangoproject.com/en/3.2/ref/models/instances/#django.db.models.Model.get_FOO_display) |
| [schedule_form.html: Line 41](https://github.com/benschaf/waste-schedule/blob/main/schedulebuilder/templates/schedulebuilder/schedule_form.html#L41) | uploading a file using a form | [www.w3schools.com](https://www.w3schools.com/tags/att_form_enctype.asp) |
| [style.css: Line 8](https://github.com/benschaf/waste-schedule/blob/main/static/css/style.css#L8) | using CSS root variables | [www.w3schools.com](https://www.w3schools.com/css/css3_variables.asp) |
| [style.css: Line 97](https://github.com/benschaf/waste-schedule/blob/main/static/css/style.css#L97) | keyframes | [stackoverflow.com](https://stackoverflow.com/questions/45330061/how-to-flash-a-div-only) |
| [style.css: Line 149](https://github.com/benschaf/waste-schedule/blob/main/static/css/style.css#L149) | Gradient text | [cssgradient.io](https://cssgradient.io/blog/css-gradient-text/) |
| [style.css: Line 235](https://github.com/benschaf/waste-schedule/blob/main/static/css/style.css#L235) | timeline CSS & HTML | [www.bootdey.com](https://www.bootdey.com/snippets/view/timeline-events) |
| [style.css: Line 350](https://github.com/benschaf/waste-schedule/blob/main/static/css/style.css#L350) | google button styling | [developers.google.com](https://developers.google.com/identity/branding-guidelines?hl=de) |
| [style.css: Line 394](https://github.com/benschaf/waste-schedule/blob/main/static/css/style.css#L394) | progress bar | [bbbootstrap.com](https://bbbootstrap.com/snippets/bootstrap-4-bootstrap-4-timeline-order-tracking-step-step-progress-bar-26897417) |
| [edit_calendar.js: Line 26](https://github.com/benschaf/waste-schedule/blob/main/static/js/edit_calendar.js#L26) | getWeekday | [www.w3schools.com](https://www.w3schools.com/jsref/jsref_getday.asp) |
| [edit_calendar.js: Line 68](https://github.com/benschaf/waste-schedule/blob/main/static/js/edit_calendar.js#L68) | selectedIndex | [www.w3schools.com](https://www.w3schools.com/jsref/prop_select_selectedindex.asp) |
| [edit_calendar.js: Line 155](https://github.com/benschaf/waste-schedule/blob/main/static/js/edit_calendar.js#L155) | query selector | [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector?retiredLocale=de) |
| [edit_calendar.js: Line 205](https://github.com/benschaf/waste-schedule/blob/main/static/js/edit_calendar.js#L205) | adding a year to a date | [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setFullYear) |
| [index.js: Line 1](https://github.com/benschaf/waste-schedule/blob/main/static/js/index.js#L1) | redirecting to a url in javascript | [stackoverflow.com](https://stackoverflow.com/questions/503093/how-can-i-make-a-redirect-page-in-jquery-javascript) |
| [script.js: Line 2](https://github.com/benschaf/waste-schedule/blob/main/static/js/script.js#L2) | popovers | [getbootstrap.com](https://getbootstrap.com/docs/5.2/components/popovers/#overview) |
| [script.js: Line 46](https://github.com/benschaf/waste-schedule/blob/main/static/js/script.js#L46) | the copyright notice update function goes to TravelTimN | [github.com](https://github.com/TravelTimN) |
| [404.html: Line 5](https://github.com/benschaf/waste-schedule/blob/main/templates/404.html#L5) | adding costum error pages | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/ref/views/) |
| [base.html: Line 55](https://github.com/benschaf/waste-schedule/blob/main/templates/base.html#L55) | getting view name from template | [stackoverflow.com](https://stackoverflow.com/questions/2491605/how-to-get-the-current-url-namespace-using-django) |
| [base.html: Line 99](https://github.com/benschaf/waste-schedule/blob/main/templates/base.html#L99) | django messages framework | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/) |
| [login.html: Line 29](https://github.com/benschaf/waste-schedule/blob/main/templates/account/login.html#L29) | google sign in button | [developers.google.com](https://developers.google.com/identity/branding-guidelines?hl=de) |
| [signup.html: Line 37](https://github.com/benschaf/waste-schedule/blob/main/templates/account/signup.html#L37) | social Login setup | [www.youtube.com](https://www.youtube.com/watch?v=yO6PP0vEOMc&ab_channel=AkamaiDevRel) |
| [signup.html: Line 38](https://github.com/benschaf/waste-schedule/blob/main/templates/account/signup.html#L38) | documentation for social Login setup | [docs.allauth.org](https://docs.allauth.org/en/latest/socialaccount/introduction.html) |
| [settings.py: Line 77](https://github.com/benschaf/waste-schedule/blob/main/tonne/settings.py#L77) | cloudinary saving using HTTPs (this is a link to the code institute internal Slack server) | [code-institute-room.slack.com](https://code-institute-room.slack.com/archives/C026PTF46F5/p1706622757171679) |
| [models.py: Line 10](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/models.py#L10) | RegexValidator class | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/ref/validators/#regexvalidator) |
| [models.py: Line 28](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/models.py#L28) | slugifiable regex (generated using Bing AI) | [www.bing.com](https://www.bing.com/chat) |
| [test_views.py: Line 7](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/test_views.py#L7) | django test assertions | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#assertions) |
| [test_views.py: Line 106](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/test_views.py#L106) | converting a QuerySet to a list | [stackoverflow.com](https://stackoverflow.com/questions/4424435/how-to-convert-a-django-queryset-to-a-list) |
| [test_views.py: Line 308](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/test_views.py#L308) | refreshing the object from the database | [stackoverflow.com](https://stackoverflow.com/questions/4377861/reload-django-object-from-database) |
| [test_views.py: Line 622](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/test_views.py#L622) | converting lists with different orders to sets to compare them | [www.digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-compare-two-lists-in-python) |
| [views.py: Line 23](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/views.py#L23) | class based views | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/ref/class-based-views/) |
| [views.py: Line 79](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/views.py#L79) | adding an annotation to each object in a list | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/topics/db/aggregation/) |
| [views.py: Line 82](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/views.py#L82) | passing only the id field value to the template | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#values-list) |
| [views.py: Line 108](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/views.py#L108) | additional context data in class based views | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/) |
| [views.py: Line 131](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/views.py#L131) | checking wether a queryset contains any items | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.exists) |
| [views.py: Line 132](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/views.py#L132) | authenticating the logged in user | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/topics/auth/default/#authentication-in-web-requests) |
| [views.py: Line 147](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/views.py#L147) | using the LoginRequiredMixin | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-loginrequiredmixin-mixin) |
| [views.py: Line 186](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/views.py#L186) | finding class based view methods | [www.brennantymrak.com](https://www.brennantymrak.com/articles/createviewdiagram) |
| [views.py: Line 196](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/views.py#L196) | edit view | [github.com](https://github.com/Code-Institute-Solutions/blog/tree/main/12_views_part_3/05_edit_delete) |
| [views.py: Line 324](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/views.py#L324) | creating an object | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/topics/db/queries/#creating-objects) |
| [views.py: Line 325](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/views.py#L325) | deleting an object | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/topics/db/queries/#deleting-objects) |
| [views.py: Line 435](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/views.py#L435) | ics.py library that helps to create ics files | [icspy.readthedocs.io](https://icspy.readthedocs.io/en/stable) |
| [views.py: Line 455](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/views.py#L455) | formatting a date object width strftime | [strftime.org](https://strftime.org/) |
| [views.py: Line 464](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/views.py#L464) | creating a download response | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/ref/request-response/#fileresponse-objects) |
| [schedule_detail.html: Line 147](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/templates/wasteschedules/schedule_detail.html#L147) | crispy forms | [github.com](https://github.com/Code-Institute-Solutions/blog/tree/main/12_views_part_3/01_posting_to_database) |
| [schedule_detail.html: Line 174](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/templates/wasteschedules/schedule_detail.html#L174) | modals | [getbootstrap.com](https://getbootstrap.com/docs/5.2/components/modal/) |
| [schedule_detail.html: Line 175](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/templates/wasteschedules/schedule_detail.html#L175) | passisng data attributes to js | [blog.webdevsimplified.com](https://blog.webdevsimplified.com/2020-10/javascript-data-attributes/) |
| [schedule_detail.html: Line 176](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/templates/wasteschedules/schedule_detail.html#L176) | passing the CSRF Token and using it in js | [stackoverflow.com](https://stackoverflow.com/questions/47527120/how-to-add-assign-csrf-token-in-the-html-submit-form) |
| [schedule_detail.html: Line 229](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/templates/wasteschedules/schedule_detail.html#L229) | sending JSON data to JavaScript | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatefilter-json_script) |
| [schedule_list.html: Line 12](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/templates/wasteschedules/schedule_list.html#L12) | manual input validation using a regex pattern | [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation) |
| [schedule_list.html: Line 67](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/templates/wasteschedules/schedule_list.html#L67) | popovers | [getbootstrap.com](https://getbootstrap.com/docs/5.2/components/popovers/#overview) |
| [schedule_list.html: Line 112](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/templates/wasteschedules/schedule_list.html#L112) | pagination with django | [docs.djangoproject.com](https://docs.djangoproject.com/en/5.0/topics/pagination/) |
| [schedule_list.html: Line 113](https://github.com/benschaf/waste-schedule/blob/main/wasteschedules/templates/wasteschedules/schedule_list.html#L113) | pagination styles | [getbootstrap.com](https://getbootstrap.com/docs/5.3/components/pagination/) |
<!-- CREDITS_END -->

Additionaly, [Chris Beams](https://chris.beams.io/posts/git-commit) article "How to Write a Git Commit Message" was used as a guideline for writing commit messages.

### Media

The tonne logo was drawn by me, adapting the design from a [vecteezy graphic](https://de.vecteezy.com/vektorkunst/571076-mulleimer-symbol).

Images for sample Waste Schedules featured in the fixtures were taken from the following websites and uploaded to Cloudinary as an example usecase in the project:
* [Landkreis Coburg](https://www.landkreis-coburg.de/73-0-Abfallwirtschaft.html)
* [Öhningen Waste Calendar](https://www.oehningen.de/fileadmin/redakteur/Abfallkalender_NEU_%C3%96hningen_2024.pdf)
* [Landkreis Schweinfurt](https://www.landkreis-schweinfurt.de/abfuhrkalender)
* [Pfarrweisach](https://awhas.de/service/abfuhrtermine/pfarrweisach/jahreskalender.html#calendar)

All images used in this project were generated using the [Copilot Designer](https://www.bing.com/images/create?cc=de)


### Acknowledgements

- Immense thanks go to my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance and their time with troubleshooting and debugging some project issues.
- I would like to thank my partner for her support and understanding during the development of this project.

---
---

## Design Thinking Process

> [!NOTE]
> This Section is added at the end of the README file to keep it clean and concise. Though it is not part of the usual README structure, it was added to provide a more detailed insight into the project's conception and development process.

The design thinking process was used to develop the idea for this project. The process consists of five stages: Empathise, Define, Ideate, Prototype, and Test. Each stage was used to understand the problem, generate ideas, and create a solution that meets the needs of the target audience.

### Emphatise
For this stage, I created 4 user personas to represent the different types of users that would interact with the app.

For each persona, I considered their "5 Cs" (circumstances, constraints, context, criteria, and compensating behaviors) related to waste management and waste management reminders. This helped me understand their needs and motivations better.

1. **Eco-Conscious Emma**:
    Emma is a young environmental enthusiast living in a bustling city like Berlin. She actively separates her waste into different bins, composts organic materials, and participates in local recycling programs. Emma is passionate about reducing her ecological footprint and encourages her neighbors to do the same. She would appreciate an app that provides real-time reminders for waste collection days, educates users about proper waste sorting, and offers tips on sustainable living.
    - **Circumstances**:
        - Emma faces the problem when she’s juggling work, social commitments, and her passion for environmental sustainability.
    - **Constraints**:
        - Her busy lifestyle often leads to forgetfulness about waste collection days.
        - Lack of clear information on local recycling centers and drop-off points.
    - **Context**:
        - Emma encounters this issue at home, especially during early mornings when she needs to take out her bins.
    - **Criteria**:
        - Solving this problem aligns with Emma’s values of reducing waste and contributing to a greener planet.
    - **Compensating Behaviors**:
        - Emma sets manual reminders on her phone but occasionally misses them due to her hectic schedule.

2. **Busy Bernd**:
    Bernd is a working professional in Munich. His busy schedule often leads to forgetfulness, and he occasionally misses waste collection days. He needs an app that sends notifications a day in advance, reminding him to take out his bins. Bernd also wants information on nearby recycling centers and drop-off points for hazardous waste. A feature that tracks his waste reduction progress would motivate him to be more diligent.
    - **Circumstances**:
        - Bernd’s demanding job and family responsibilities make it challenging for him to remember waste collection days.
    - **Constraints**:
        - Time constraints prevent him from researching local waste management rules thoroughly.
    - **Context**:
        - Bernd faces this issue at home, especially during evenings when he’s exhausted from work.
    - **Criteria**:
        - Solving this problem would reduce stress and prevent missed collections.
    - **Compensating Behaviors**:
        - Bernd relies on neighbors’ cues or waits until he hears the garbage truck to take out his bins.

3. **Senior Sigrid**:
    Sigrid, a retiree in Hamburg, values simplicity. She finds the current waste management system confusing and struggles with the various colored bins. Sigrid needs an app with clear instructions on waste separation, including visual cues. Additionally, a feature that connects her with local volunteers or services for assistance with heavy bins would be helpful.
    - **Circumstances**:
        - Sigrid’s age affects her memory, and she finds the waste separation process confusing.
    - **Constraints**:
        - Physical limitations prevent her from handling heavy bins easily.
    - **Context**:
        - Sigrid encounters this issue at home, especially when she needs to sort waste into different containers.
    - **Criteria**:
        - Solving this problem ensures Sigrid’s independence and reduces frustration.
    - **Compensating Behaviors**:
        - Sigrid asks her neighbor for help or leaves her bins outside for extended periods.

4. **Family-Focused Felix**:
    Felix lives in a suburban area near Frankfurt with his family. Managing waste for a household of four can be overwhelming. He wants an app that syncs with family members’ calendars, reminding everyone about collection days. Felix also seeks advice on minimizing waste, especially with kids in the house. Perhaps the app could gamify waste reduction to involve the whole family.
    - **Circumstances**:
        - Felix manages waste for his family, balancing work, parenting, and household chores.
    - **Constraints**:
        - Coordinating waste collection days among family members is challenging.
    - **Context**:
        - Felix faces this issue both at home and during family discussions.
    - **Criteria**:
        - Solving this problem streamlines family routines and teaches kids responsible waste management.
    - **Compensating Behaviors**:
        - Felix uses sticky notes or a shared calendar to remind everyone about bin days.

### Define
Considering all the user personas, I defined problem statements for each of them:

#### Problem statements:
1. **Eco-Conscious Emma**:
    - **Statement**: “I am Eco-Conscious Emma trying to reduce waste, but the lack of timely reminders due to my busy schedule makes me feel frustrated and guilty.”
    - **Statement**: “I am Eco-Conscious Emma trying to educate my neighbors about waste sorting, but the unclear rules due to insufficient information make me feel determined yet overwhelmed.”
2. **Busy Bernd**:
    - **Statement**: “I am Busy Bernd trying to remember waste collection days, but my forgetfulness due to a hectic work schedule makes me feel stressed and annoyed.”
    - **Statement**: “I am Busy Bernd trying to find local recycling centers, but the lack of time due to work commitments makes me feel overwhelmed and uninformed.”
3. **Senior Sigrid**:
    - **Statement**: “I am Senior Sigrid trying to sort waste, but the confusion due to age-related memory challenges makes me feel frustrated and helpless.”
    - **Statement**: “I am Senior Sigrid trying to handle heavy bins, but my physical limitations due to aging make me feel dependent and anxious.”
4. **Family-Focused Felix**:
    - **Statement**: “I am Family-Focused Felix trying to coordinate family waste routines, but the complexity due to managing a household makes me feel overwhelmed yet responsible.”
    - **Statement**: “I am Family-Focused Felix trying to involve kids in waste reduction, but the lack of guidance due to parenting challenges makes me feel determined and hopeful.”

**Overarching Problem Statement**: In a world grappling with stress and environmental challenges, our project aims to develop an integrated waste management solution that addresses the diverse needs of individuals — ranging from busy professionals and eco-conscious citizens to seniors and families. By providing a platform for community engagement, we strive to minimize the stress and confusion that accompany waste management, fostering a sense of responsibility and empowerment among communities. Our mission is to empower everyone, regardless of age or lifestyle, to actively participate in waste reduction, ultimately fostering a cleaner and greener planet.

### Ideate
Considering the problem statements, I brainstormed potential solutions that could address the needs of each user persona. Here are some ideas already with an added priority value (p1: high priority, p2: medium priority, p3: low priority):

1. **Eco-Conscious Emma**:
    - **Solution 1: Waste Collection Reminders**:
        - **p1** Implement a calendar view that highlights upcoming collection days and allows Emma to set preferences (e.g., reminders a day in advance).
        - **p1** Create a community platform within the app where users like Emma can voluntarily share their waste collection schedules.
        - **p1** Neighbors receive real-time reminders based on shared schedules, fostering a sense of community responsibility.
    - **Solution 2: Educational Resources**:
        - **p2** Include an educational section within the app. Provide clear guidelines on waste sorting, recycling, and composting. Use visual cues (infographics, images) to simplify the information.
        - **p3** Collaborate with local environmental organizations to curate content and host webinars on sustainable living.

2. **Busy Bernd**:
    - **Solution 1: Automated Notifications**:
        - **p1** Upon login, prompt Bernd to input his address and preferred notification settings. Send automated reminders via email or SMS a day before waste collection days.
        - **p1** Allow customization (e.g., specific time of day for reminders) to accommodate Bernd’s schedule.
    - **Solution 2: Nearby Services Locator**:
        - **p3** Integrate a map feature that displays nearby recycling centers, drop-off points, and hazardous waste disposal locations.
        - **p3** Include operating hours, contact information, and directions.

3. **Senior Sigrid**:
    - **Solution 1: Visual Guides**:
        - **p3** Develop an intuitive waste sorting guide with visual icons. Sigrid can easily identify which bin to use based on item categories (e.g., paper, plastic, glass).
        - **p3** Include voice instructions for accessibility.
    - **Solution 2: Assistance Network**:
        - **p3** Create a community feature where neighbors can offer assistance. Sigrid can request help with heavy bins or ask for clarification on waste separation.
        - **p2** Encourage local volunteers to participate.

4. **Family-Focused Felix**:
    - **Solution 1: Family Calendar Integration**:
        - **p2** Allow Felix to invite family members to join the app. Sync the app with their calendars to display waste collection days.
        - **p2** Enable notifications for all family members, ensuring everyone is aware.
    - **Solution 2: Waste Reduction Challenges**:
        - **p3** Gamify waste reduction within the family. Set monthly challenges (e.g., reduce plastic waste, compost more) and track progress.
        - **p3** Award virtual badges or points for achieving goals.

### Prototype
After ideating I created wireframes and content for the prototype of the site which is of course this repository.

Check out the full prototype including wireframes, user stories, and the working site by browsing around the readme and the repository. Also check out the [tonne website](https://tonne-waste-reminders-a6836f2888b0.herokuapp.com/) itself.

### Test
The prototype of the site was tested manually and progamatically to ensure that it is working as intended.
Testing in the sense of design thinking has not been very extensive yet. This will be done in the future.