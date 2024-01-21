# MyCar API - *Get Updates on Cars*

[View code here](https://github.com/belovedpearl/mycar_drfapi)

![Presentation](screenshots/live_/presentation)


[View live site here](https://mycardrfapi-d64556077ed4.herokuapp.com/)

---

**Table of Contents:**

---

 * [Scope](#scope)  
 * [Agile Project Management](#agile-project-management)
 * [User Stories](#user-stories)
 * [Features](#features)
 
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

![Kanban Board](screenshots/mama's_kitchen_details_desktop&laptop.webp)(screenshot of kanban board)



---

# User Stories

Users here refers to the developer or the superuser that have access to the backend site as the project is majorly an API to store data from the frontend.
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

As a User, I can upvote a vote so that I can express positive remarks about a car post.

As a User, I can see upvotes list on the api so that I can see all upvotes created on the api.

As a User, I can remove my upvote so that I can change my mind about a car post.

As a User, I cannot add an upvote to a post when I already downvoted the same post.

## Downvotes

As a User, I can downvote a post so that I can express nagative impression about a car post.

As a User, I can see downvotes list on the api so that I can see all downvotes created on the api.

As a User, I can remove my downvote so that I can change my mind about a car post.

As a User, I cannot add an downvote to a post when I already upvoted the same post.

## Followers

As a User, I can follow other users so that I can get updated with their posts.

As a User, I can delete my follow so that I can change my mind about following another user.

## Search and Filter

As a User, I can search posts with keywords like (model, make, name) so that I can get posts I am intrested in on time.

As a User, I can filter posts by category (body_types) so that I can view car posts relating to a particular category of interest.

---

# Features

---
This section discusses the features and the different endpoints on project 'My Car', the choices made.

## Homepage

On first visit to the API site, you are directed to the Root Route homepage. The home page consist of a welcome message to the API. This can be accessed via [live site](https://mycardrfapi-d64556077ed4.herokuapp.com/).

![Homepage Picture](screenshots/live_site/footer.webp)

## Profiles Data

This can be accessed via [profile list](https://mycardrfapi-d64556077ed4.herokuapp.com/profiles/). It contains a list of all registered profiles on the API created on successful user registration. A model is defined to determine the structure of required profile data inheriting from django model.Model class rendered with ProfileList inheriting from django generics.ListAPIView.
A function is added to automatically create a new profile when a new user is created using the [post_save](https://docs.djangoproject.com/en/5.0/topics/signals/) signals

<details>
<summary>Sceeenshot of Profile Data page on the live site</summary>
    <img src="" width="80%">
</details>

## Posts Data

This can be accessed via [post list](https://mycardrfapi-d64556077ed4.herokuapp.com/posts). This stores up a list of all posts on the API. Users are able to create a new post, update their posts and delete their posts. A model is also defined to determine the post structure using the django model.Model class and rendered using the PostsList view inheriting from [generics.ListCreateAPIView](https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview).

<details>
<summary>Sceeenshot of Posts Data page on the live site</summary>
    <img src="" width="80%">
</details>

## Reviews

This can be accessed via [review list](https://mycardrfapi-d64556077ed4.herokuapp.com/reviews/). This contains a list of all reviews that users have provided on the API. Each review is linked to a post. Users can add, edit and delete their reviews as desired.

<details>
<summary>Sceeenshot of Reviews Data page on the live site</summary>
    <img src="" width="80%">
</details>

## Upvotes

This can be accessed via [upvotes list](https://mycardrfapi-d64556077ed4.herokuapp.com/upvotes/). This contains a list of all upvotes that users have provided on the API. Each upvote is linked to a post and each upvote is identified by a unique id. Users can add, view and delete their upvotes as desired. Users cannot add a upvote if they already have a downvote on a post, also users are prevenyed from creating multiple upvotes on a post.

<details>
<summary>Sceeenshot of Upvotes page on the live site</summary>
    <img src="" width="80%">
</details>

## Downvote

This can be accessed via [downvote list](https://mycardrfapi-d64556077ed4.herokuapp.com/downvotes/). This contains a list of all downvotes that users have provided on the API. Each downvote is linked to a post and each downvote is identified by a unique id. Users can add, view and delete their downvotes as desired using the django views [this](https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview) and [this](https://www.django-rest-framework.org/api-guide/generic-views/#retrievedestroyapiview). Users cannot add a downvote if they already have an upvote on a post, also users are prevented from creating multiple downvote on a post.

<details>
<summary>Sceeenshot of Downvotes page on the live site</summary>
    <img src="" width="80%">
</details>

## Followers

This can be accessed via [followers list](https://mycardrfapi-d64556077ed4.herokuapp.com/followers/). This contains a list of all follows that users have created on the API. Authenticated users can view the followers list, create a follow and delete a follow using (this)[https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview] and (this)[https://www.django-rest-framework.org/api-guide/generic-views/#retrievedestroyapiview] view. Users are prevented from creating multiple follow for a profile. Each created follow is linked to a profile and can be identified by a unique id.

<details>
<summary>Sceeenshot of Followers list on the live site</summary>
    <img src="" width="80%">
</details>

