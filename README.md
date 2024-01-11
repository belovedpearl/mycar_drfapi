# MyCar API - *Get Updates on Cars*

[View code here](https://github.com/belovedpearl/mycar_drfapi)

---

**Table of Contents:**

---

 * [Scope](#scope)  
 
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

Key features will include:

**Profile Creation:** This will be handled by signal which will allow automatic creation of prifile on new user addition.

**Login/Logout Functions:** Users will be able to login and logout from the API

**Uniform Interface:** Endpoints for different resources will be unique from the other to allow for network protocols like DELETE, PUT, GET for different http methods.

**User Authentication:** The api will use the Django AllAuth library to enable user account creation and login functionality. Once registered and logged in.

**Post Management:** The API will manage posts from users in a way that it is made available on request in JSON format.

**Post Engagement Records:** From the frontend, users can submit different expressions about cars, the API stores up the different records.

**Deletion:** Registered users will have the ability to delete their contributions to the platform and removed from the API as they wish (i.e posts, upvotes, downvotes, comments).

**Update Contributions:** The API will allow users to update posts and comments contributed by users and thereby updating the same on the platform.

By implementing these features, 'MyCar' aims to foster an engaging community for Car enthiast.