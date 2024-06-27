# Gipfel Tutor

[Experience our live website here!](#)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/benschaf/gipfel-tutor)](https://github.com/benschaf/gipfel-tutor/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/benschaf/gipfel-tutor)](https://github.com/benschaf/gipfel-tutor/commits/main)
[![GitHub issues](https://img.shields.io/github/issues/benschaf/gipfel-tutor)](https://github.com/benschaf/gipfel-tutor/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/benschaf/gipfel-tutor)](https://github.com/benschaf/gipfel-tutor/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub repo size](https://img.shields.io/github/repo-size/benschaf/gipfel-tutor)](https://github.com/benschaf/gipfel-tutor)
[![Python version](https://img.shields.io/badge/python-3.12.2-blue?logo=python)](https://www.python.org/downloads/release/python-3121/)
[![npm version](https://img.shields.io/badge/npm-8.1.0-blue?logo=npm)](https://www.npmjs.com/package/npm)
[![Heroku](https://img.shields.io/badge/heroku-eco-purple?logo=heroku)](#)

Welcome to Gipfel Tutor, the pinnacle of personalized tutoring for Swiss students! Our Django-powered marketplace pairs you with the perfect tutor to conquer your academic peaks. Quick, simple, and effective — scale new heights in learning with us!

> **Our Mission**:
>
> "Connect learners with a highly suitable tutor for their specific **needs** and **preferences**, within **48 hours*."

**Better Matching system**:
    The platform offers a sophisticated matching system that leverages detailed tutor profiles. Tutors are required to provide a comprehensive description of their experience, qualifications, and teaching valuess (via tags they can select). Additionally, students can filter their search using relevant tags associated with the tutor's expertise . A star rating system and experience metrics (number of lessons taught, years of experience) further help students find a tutor that closely aligns with their needs.

## UI/UX Design

## Database Design

[dbdiagram link](https://dbdiagram.io/d/ERD_tutor_service-667c0ec99939893dae536ebe)

## Tools and Technologies
- ![calendly_api](https://img.shields.io/badge/-Calendly%20API-1A1A1A?style=flat&logo=calendly)
> [!Note]
> I mainly want to use the simpler embed feature of Calendly. It would be really cool though to use the api v2 they provide mainly to enable searching tutors based on their avaliability. Also without using the api webhooks, smooth cancellations are basically impossible. (seems like future feature stuff)

## Marketing

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

## User Stories

The user stories are based on the user personas and the features of the app. They are written from the perspective of the user and describe the actions they can take on the site.

### Viewing and navigation

| User Story | Acceptance Criteria |
| --- | --- |
| As a **first time visitor**, I want to be able to understand the purpose of the site so that I can decide if I want to sign up. | 1. The homepage should clearly explain the purpose of the site. <br> 2. The homepage should have a call-to-action button to sign up. |
| As a **student**, I want to be able to view a list of tutors so that I can choose the best tutor for my needs. | 1. The site should have a page that lists all available tutors. <br> 2. Each tutor should have at least their profile picture, name, and hourly rate displayed. |
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

<!--
## Plain user Stories

### Viewing and navigation

- As a **first time visitor**, I want to be able to understand the purpose of the site so that I can decide if I want to sign up.
- As a **student**, I want to be able to view a list of tutors so that I can choose the best tutor for my needs.
- As a **student**, I want to be able to view detailed tutor profiles so that I can learn more about the tutor's experience and teaching values.

- NOT MVP As a **student**, I want to be able to like and save tutors so that I can easily find them later.

### Searching, filtering, and sorting

- As a **student**, I want to be able to filter tutors based on teaching experience and ratings so that I can choose a highly qualified tutor.
- As a **student**, I want to be able to sort tutors based on hourly rates and ratings so that I can find an affordable and highly rated tutor.
- As a **student**, I want to be able to search for tutors based on their name, description subject expertise and teaching values so that I can find a tutor that closely aligns with my needs.

### Registration and user Accounts

- As a **user**, I want to be able to create either a student or tutor account so that I can access the platform.
- As a **user**, I want to be able to log in and log out of my account so that I can access my profile and bookings.
- As a **user**, I want to be able to reset my password in case I forget it so that I can regain access to my account.
- As a **user**, I want to receive a confirmation email after registering so that I can verify my account.
- As a **student**, I want to be able to see my booking history, upcoming lessons, payment details and my liked tutors so that I can manage my account.
- As a **tutor**, I want to be able to see my booking history, upcoming lessons, bank details and my currently booked students so that I can manage my account.

### Tutor profiles

- As a **tutor**, I want to be able to create a detailed tutor profile so that students can learn more about me.
- As a **tutor**, I want to be able to set my availability and hourly rates so that students can book lessons with me.
- As a **tutor**, I want to be able to receive booking requests from students so that I can confirm lessons.
- As a **student**, I want to be able to leave a review and rating for a tutor after a lesson so that other students can benefit from my experience.

### Booking and scheduling

- As a **student**, I want to be able to schedule regular lessons with a tutor so that I can improve my academic performance.
- As a **student**, I want to be able to pay for lessons online so that I can easily book and confirm lessons.
- As a **student**, I want to be notified of successful or failed payments so that I can keep track of my bookings.

- NOT MVP As a **student**, I want to be able to book a trial lesson with a tutor so that I can see if the tutor is a good fit for me.
- NOT MVP As a **student**, I want to be able to cancel a lesson with a tutor so that I can reschedule if needed.
-  NOT MVP As a **student**, I want to get in contact with a tutor to discuss study plans and exam strategies so that I can improve my exam performance.

### Admin

- As an **admin**, I want to be able to add, edit, and delete tutors so that I can manage the platform.
- As an **admin**, I want to be able to view and manage user accounts so that I can ensure the security of the platform.
- As a **Site Owner**, I want the site to Employ Search Engine Optimisation (SEO) techniques to improve audience reach. (Compare LO3 in Code Institute Project Requirements)

- NOT MVP As an **admin**, I want to be able to view and manage bookings and payments so that I can ensure the smooth operation of the platform.

### Marketing and Business Strategy

- As a **Site Owner**, I want to have a Facebook Business Page to promote the site and attract more users. (Compare LO5 in Code Institute Project Requirements)
- As a **Site Owner**, I want to provide a Newsletter to keep site visitors informed about new features and updates. (Compare LO5 in Code Institute Project Requirements)
- As a **Site Owner**, I want to hava a documentation of the ecommerce business model. (Compare LO6 in Code Institute Project Requirements)
-->

### Future Features

- Feedback on singular lessons

## Business and Costumer Goals

The business goals of the app are to provide a platform where students can find tutors for their specific needs and preferences. The app aims to set itself apart from other tutoring platforms by providing a better matching system that leverages detailed tutor profiles, ratings, and reviews. The app also aims to provide a seamless user experience for both students and tutors, with features such as detailed tutor profiles, booking requests, and online payments.

Maybe formulate project goals and map them to user stories - but this seems unnecessary at the moment.