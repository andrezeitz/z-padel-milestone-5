# Z Padel
Z Padel is a B2C business selling padel equipment to the avarge padel tennis player. We have products from all the major padel brands so the user is able to find the correct equipment. We sell everything from rackets to cloth and have a lot of different sizes to fit everyone.

This website can not be used as a template for a business since it's a project for educational purposes.

Live website: [Z Padel](https://z-padel.herokuapp.com/)

## Table of Contents

* [UX (User Experience)](#ux-user-experience)
  * [User Stories](#user-stories)
  * [Site Owner Goals](#site-owner-goals)
* [Design](#design)
  * [Fonts](#fonts)
  * [Colors](#colors)
  * [Wireframe](#wireframe)
* [Technologies](#technologies)
  * [Languages](#languages)
  * [Frameworks and Tools](#frameworks-and-tools)
  * [Contrast Checker](#contrast-checker)
* [Features](#features)
* [Testing](#testing)
  * [Code Validation](#code-validation)
  * [HTML](#html)
  * [CSS](#css)
  * [Python](#python)
  * [Different Screen Size](#different-screen-size)
* [Issues found during site development](#issues-found-during-site-development)
* [Deployment](#deployment)
  * [Cloning](#cloning)
* [Credits](#credits)

## UX (User Experience)

### User Stories

* As a shopper
  * I can view a different kind of products so that I can select something to buy
  * I can see individual product details so that I can take a closer look on price, information, pictures and different sizes
  * I can easy see how much the current shoppingbag will cost so that I can see if I can afford everything
  * I can select size and quantity of product so that I can choose the correct size and how many I want to buy
  * I can see what I have in my shoppingbag so that I can see how much I will spend on my purchase
  * I can change the quantity of individual items in my bag so that I can easy make a change to the products before checkout
  * I can enter my credit card so that I can pay for my items
  * I can get an order confirmation after purchase is successful so that I can see so everything is correct
  * I can get a email confirmation on my purchase so that I can know that my order was completed successful

* As a user
  * I can register for an account so that I can have a personal account
  * I can login and out of my account so that I can access my private account
  * I can recover my password if i forget it so that I can get back in to my account
  * I can have a personalized profile so that I can see my old order history
  * I can search for different products so that I can find what I'm looking for
  * I can choose a specific category of product so that I can easily find the best product in that category

### Site Owner Goals
* As a site owner
  * I can add a product so that I can update with new items
  * I can edit a product so that I can change product price, descriptions and other criteria
  * I can delete a product so that I can remove it from the store and it will no longer be able to purchase
  * I can get an order confirmation when someone is making a purchase

* I planned the project [here](https://github.com/andrezeitz/z-padel/projects/1)

## Design

### Fonts
I have chosen Lato for the headers as it is easy to read and has sufficient contrast to the main body font. Roboto for all other text.

### Colors
The site features complementary Blue Crayola Forest Green Web, Pacific Blue, white and black to create a good contrast and improve readability.

The colors chosen are:


### Wireframe

#### Desktop

<img width="698" alt="WEB" src="https://user-images.githubusercontent.com/85236391/147922980-ef5683d9-9647-4777-9a3e-68ec68b2da39.png">

#### Mobile

<img width="696" alt="MOBILE" src="https://user-images.githubusercontent.com/85236391/147923016-761bbe79-8b11-4963-b383-79cc32be64f2.png">

## Technologies

### Languages
* HTML
* CSS
* Python

### Frameworks and Tools
* [GitHub](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [Django](https://www.djangoproject.com/)
* [Heroku](https://www.heroku.com/home)
* [Postgres](https://www.postgresql.org/)
* [Google Fonts](https://fonts.google.com/)
* [Font Awesome](https://fontawesome.com/)
* [W3C HTML Validation](https://validator.w3.org/)
* [H3C CSS Validation](https://jigsaw.w3.org/css-validator/validator.html.en)
* [http://pep8online.com/](http://pep8online.com/)
* [Am I responsive](http://ami.responsivedesign.is/)
* [WebAim](https://webaim.org/resources/contrastchecker/)

### Contrast Checker
All colors was checked in a contrast checker and pass the test.


## Features
The website has the following features:
### Navigation bar

### Home

### Products

### Cart

### Checkout

### Checkout Success

### Account

### Footer
The footer contains the opening hours and contact information about the company.


## Testing


### Code Validation

### HTML
The W3C Markup Validation Service was used to validate the HTML page of the project. No errors or warnings to show.

##### Home Page


### CSS
The W3C CSS Validation Service was used to validate the CSS file used for the project. No errors or warnings to show.



### Python
The PEP8 Online Check was used to validate all Python code. No errors or warnings to show



### Different Screen Size
The site is optimized for all screen sizes and tested with a Macbook Pro 13" and iPhone 13 Pro.
I use media queries to make everything look and feel good on mobile devices.

### Issues found during site development
1. I had a problem to get the slug-field to work properly.

##### Solution:

2. 

## Deployment
1. On the home screen click on create new app button
2. Enter a name for the project and select your region to the correct region
3. On the next screen select settings
4. Go to config vars and click reveal config vars
5. Switch to the program file and where you are keeping your credentials copy these and then on Heroku enter a name for the key and paste the code into the config vars value box and click add
6. Now scroll down to buildPacks and click add build packs
7. First select python and click save changes
8. Click back into build packs and choose node.js and click save again
9. Ensure that the Python build pack is at the top of the list you are able to drag and drop if you need to rearrange
10. Now select deploy
11. From the deployment method select GitHub
12. Then click on connect to Github button that appears
13. Click into the search box and search for the project name
14. Once located select connect
15. Then click deploy branch, this will then be shown in the box below
16. You can the click view to show the app in a browser

The program is set to be deployed automatically after each push from gitpod.

I also set up a Postgres database with Heroku.
1. Click on Resources in your Heroku app.
2. In the add-ons field search for Heroku Postgres and press submit.

### Cloning
How to clone this repository.

* On GitHub go to the main page of the Repository.
* Above the list of files click the code button with the drop-down arrow.
* To clone the repository using HTTPS, under "Clone with HTTPS", click on the clipboard.
* Open the Git Bash terminal.
* Change the current working directory to the location where you want the cloned directory.
* Type git clone, and then paste the URL you copied earlier from step 3.
* Press Enter to create your local clone.

## Credits
