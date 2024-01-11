# MyCar API - *Get Updates on Cars*

[View code here](https://github.com/belovedpearl/mycar_drfapi)

---

**Table of Contents:**

---

 * [Scope](#scope)  
 * [Agile Project Management](#agile-project-management)
 * [User Stories](#user-stories)
 
* [Technology Used](#technology-used)
    * [Languages](#languages)
    * [Python Modules and Packages Used](#python-modules-packages-used)
* [Framework and Tools](#frameworks-and-tools)
* [Development and Deployment](#development-and-deployment)
* [How to Fork](#how-to-fork)
* [How to Clone](#how-to-clone)
* [Testing](#testing)
* [Tools](#tools)
* [Credits](#credits)
* [Acknowledgement](#acknowledgement)

---
# Scope
---

The scope of this project is to build an application programming interface (API) using python Django Rest framework which will be used with a REACT frontend to promote discussions on different cars.

MyCar API provides a backend database to create, view, edit and delete user's related posts, reviews and votes. A user can publish a  car post, including detailed content, an image, and other neccessary information required to make the post.

The API also includes search and filter logic to improve user experience, and make it easier for users to find car posts of different interest.

Key features will include:

**Profile Creation:** This will be handled by signal which will allow automatic creation of prifile on new user addition.

**Login/Logout Functions:** Users will be able to login and logout from the API

**Uniform Interface:** Endpoints for different resources will be unique from the other to allow for network protocols like DELETE, PUT, GET for different http methods.

**User Authentication:** The api will use the Django AllAuth library to enable user account creation and login functionality. Once registered and logged in.

**Post Management:** The API will manage posts from users in a way that it is made available on request in JSON format.

**Post Engagement Records:** From the frontend, users can submit different expressions about cars, the API stores up the different records.

**Deletion:** Registered users will have the ability to delete their contributions to the platform and removed from the API as they wish (i.e posts, upvotes, downvotes, comments).

**Update Contributions:** The API will allow users to update posts and comments contributed by users and thereby updating the same on the platform.

By implementing these features, 'MyCar' aims to foster an engaging community for Car enthusiast.

View the live API [here](https://mycardrfapi-d64556077ed4.herokuapp.com/)

---

# Agile Project Management
---

This backend project was managed using agile methodologies by using different user stories to manage and build the project to give the final outcome. A kanban board was setup in github projects, it was utilised as a management tool to help in the development process.

The Kanban board can be viewed [here](https://github.com/users/belovedpearl/projects/8)


(screenshot of kanban board)

---

# User Stories

Users here refers to the developer or the superuser taht have access to the backend site as the project is majorly an API to store data from the frontend.
Users story also illustrate how frontend users are able to interact with the API.

Developers users stories are summarised with the different endpoints exposed below;

## Profiles

As a user, I can view a list of all profiles so that I can see all the profiles that have been created on the API

As a user, I can view the details of one profile so that I can access more information about the individual profile.

As a user, I can edit my profile when logged in so that I can update my personal information.

## Posts

As a user, I can view a list of all posts so that I can see all posts available.

As a user, I can view a post details so that I can access more details about the post including its reviews.

As a user, I can create a new post so that this post will be added to the posts list available.

As a user, I can update a post that I created so that I can change any incorrect information on the post

As a user, I can delete a post that I created so that I can remove the posts from the API.

## Reviews

As a user, I can add a review to a post so that I can link my review to a post thereby expressing my view about the post.

As a user, I can view a list of all reviews so that I can see all reviews created for different posts on the API.

As a user, I can access a single review by id so that I can delete this update the review.

As a user, I can edit a review that I created so that I can amend any incorrect information passed accross.

As a user, I can delete a review I created so that I can remove the review from the API.

## Upvotes

