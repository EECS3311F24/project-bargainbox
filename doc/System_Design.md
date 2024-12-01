# System Design Document- Bargain Box (EECS 3311)

Course: EECS 3311  

Professor: Ilir Dema

TA: Basim

Team members: Arjun Grewal, Annie Jhamb, Jasmin Slootweg, Michael Favret, Quoc Trong Dao  

GitHub Repository: [BargainBox Project](https://github.com/EECS3311F24/project-bargainbox)  

---

## Table of Contents

1. [Introduction](#1-introduction-and-inspiration)
2. [System Overview](#2-system-overview)
3. [Architecture Description](#3-architecture-description)
4. [System Interaction](#4-system-interaction)
5. [Features Implemented](#5-features-implemented)
6. [Django App Structure](#6-django-app-structure)
7. [Components and Responsibilities](#7-components-and-responsibilities)
8. [Links](#8-links)

---


## 1. Introduction and Inspiration

The **BargainBox** project is a Django-based web application designed to provide a platform for users to share and discover deals. The repository structure and development processes follow best practices for maintainability and scalability. 

The inspiration of this project stemmed from the need of a user-friendly and interactive platform for 
users to buy and sell used/new goods. 


## 2. System Overview

BargainBox is built using the Django web framework, leveraging a modular design that divides functionality into dedicated apps. These apps correspond to core features, such as user authentication, post management, and user profile handling.


## 3. Architecture Description

The system architecture adopts the Model-View-Template (MVT) pattern inherent to Django. Each app within the project consists of the following:
- Models: Representing the database schema.
- Views: Handling business logic and user interactions.
- Templates: Rendering HTML for the user interface.

## 4. System Interaction

The system interaction is designed around HTTP requests and responses facilitated by Django's routing system. Users interact with the platform via a web browser, performing operations such as:
- Creating, editing, and deleting posts.
- Registering, logging in, and updating profiles.
- Browsing deals.

## 5. Features Implemented

### Sprint 0 
- Project planning
- Documentation
- Brainstormed ideas

### Sprint 1
- User authentication: A registration feature to create new accounts.
- Login and Logout: A login and logout system for account access.
- User profile management: A user profile that registered users can view and update

### Sprint 2
- Create post: create/post a new listing  
- Edit post functionality.
- Delete post functionality.
- System interaction improvements.
- View my listings.
- View all listings on the homepage.
- Search for listings by title and/or location.
- View my profile.
- Edit/Delete my profile.
- Updated CSS features. 

## Sprint 3 
- Bookmark/ Delete bookmark a listing.
- View 10 listings per page.
- View a seller's profile
- Reset passsword.
- Updated CSS features. 


## 6. Django App Structure

The project consists of the following Django apps:

- **bargain_box**: Core application logic.
- **home**: Handles landing page and deal browsing.
- **user_authentication**: User login and registration.
- **user_posts**: Handles posts created by users.
- **user_profile**: User account and profile management.
- **user_registration**: Helps user register into the system. 
- **users**: Manages user-specific operations.


## 7. Components and Responsibilities

- **Views**: Handle requests and return appropriate responses.
- **Templates**: Ensure a responsive and user-friendly interface.
- **URLs**: Map HTTP requests to appropriate views.

## 8. Links 
[View Sprint 0 Folder](https://github.com/EECS3311F24/project-bargainbox/tree/main/doc/sprint0)

[View Sprint 1 Folder](https://github.com/EECS3311F24/project-bargainbox/tree/main/doc/sprint1)

[View Sprint 2 Folder](https://github.com/EECS3311F24/project-bargainbox/tree/main/doc/sprint2)

[View Sprint 3 Folder](https://github.com/EECS3311F24/project-bargainbox/tree/main/doc/sprint3)
