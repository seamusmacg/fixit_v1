# [FixIt DIY E-Commerce](https://fix-it.herokuapp.com/)

!["This application was tested for responsiveness on multiple devices"](https://github.com/seamusmacg/fixit_v1/blob/master/mockups/home-page.PNG)

---

## Table of Contents

- [Project Overview](#Project-Overview)
- [UX](#UX)
  * [Strategy](#Strategy)
    * [User Stories](#User-Stories)
  * [Scope/Features](#Scope-and-Features)
  * [Features](#Features)
  * [Structure](#Structure)
  * [Wireframes](#Wireframes)
  * [Colour](#Colour)
  * [Typography](#Typography)
- [Technologies Libraries and Frameworks](#Technologies-Libraries-and-Frameworks)
- [Resources and Tools](#Resources-and-Tools)
- [Testing](#Testing)
  * [Validation](#Validation)
  * [Manual Testing](#Manual-Testing)
- [Major Bugs](#Major-Bugs)
- [Database](#Database)
- [Deployment](#Deployment)
- [Credits](#Credits)

---

### Project Overview
FixIt is an online DIY E-commerce website that provides a selection of different DIY/home products that can be ordered and delivered to the user's address. FixIt is a full stack web application that is built primarily using the Django web framework and deployed using Heroku pages. The site contains a full user authentication system and blog application that allows user to create, edit and delete blogs/categories (This site is for education purposes only - no real payments are processed by the site).

## UX 

### Strategy

#### User Stories
- As a user, I want to find and purchase home/DIY related products and have them delivered to my address. 
- As a user, I would like create a profile (delivery details) that I can reuse when I return to the site.


### Scope and Features

### Features
- Home page - contains callout section which points to the products section (also drawing user's attention to sale) which is the main feature of the site. It also contains links to the various departments in the store and an About Section which explains the site and the business.
- Products page - the primary functionality of the site is presented here. All the products of the site are shown here with their category, name, rating, image and price displayed. User's can sort by price, rating, category and name.
- Department pages are just the products page sorted by category name
- Product Info page - also displays category, name, rating, image, price and includes the product description. Users can select a product with a quantity limit of 5. They can add this to their cart or proceed back to the products page. Links to the different departments are also displayed here under the product info. 
- Shopping Cart - the shopping cart page displays information about the products added to the cart by the user - including the products category, name, rating, image, price, quantity, product code, subtotal, cart total, delivery cost and overall cost. From here users can proceed to the checkout page (Checkout button). Users can also remove products from the cart if they wish.
- Checkout page - contains order summary table and form where users can fill out their personal details including card payment info (Using Stripe). Users can also adjust their bag at this stage if they wish.
- Checkout success page - if payment is successful users will receive a confirmation message that order was successful including a bill of the order. Confirmation email will also be sent to them at this stage.
- Profile page - Profile page contains user's details in a form which can be updated. It also contains a table with the user's order history.
- Authentication pages - login page for existing users and register page for new users. New users will receive a confirmation email when they register. 
- Contact page - contains a contact form where users can submit messages to admin, users will receive confirmation page if form is sent successfully.
- Blog pages - contains archive of blogs ordered by date, administrators can create new blogs with a title, body and category, administrators can create new categories as well. Both blogs and categories can be edited and deleted as well.
- Possible Future Features - Interactive support, chat bot, user rating system and product reviews.

### Structure 
The site is presented in a linear fashion with information presented on scrolling pages. The site is a minimum viable product which serves the basic needs of the user with a lot of room for future scaling in future releases. The site follows an intuitive design where key pieces are information are easily accessed by the user. It uses a familiar layout of navbar on top and footer on bottom that is easy to navigate and conforms to user expectations and standard practices.

### Wireframes

I used [Balsamiq](https://balsamiq.com) to create a wireframe for each event presented to the user. 

- [Home Page](https://github.com/seamusmacg/fixit_v1/blob/master/mockups/home-wireframe.png)
- [Products Page](https://github.com/seamusmacg/fixit_v1/blob/master/mockups/products-wireframe.png)
- [Authentication Pages](https://github.com/seamusmacg/fixit_v1/blob/master/mockups/authentication-wireframe.png)
- [Contact Page](https://github.com/seamusmacg/fixit_v1/blob/master/mockups/contact-wireframe.png)
- [Profile Page](https://github.com/seamusmacg/fixit_v1/blob/master/mockups/profile-wireframe.png)
- [Cart Page](https://github.com/seamusmacg/fixit_v1/blob/master/mockups/cart-wireframe.png)
- [Checkout Page](https://github.com/seamusmacg/fixit_v1/blob/master/mockups/checkout-wireframe.png)
- [Success Page](https://github.com/seamusmacg/fixit_v1/blob/master/mockups/success-wireframe.png)

I maintained a consistent structure across the pages with many pages sharing similar features. 

### Colour 

- ![#bababa](https://via.placeholder.com/15/00001/000000?text=+) `#bababa`
- ![#eebe58](https://via.placeholder.com/15/eebe58/000000?text=+) `#eebe58`
- ![#FF0000](https://via.placeholder.com/15/FF0000/000000?text=+) `#FF0000`
- ![#1D9157](https://via.placeholder.com/15/1D9157/000000?text=+) `#1D9157`
- ![#fc5647](https://via.placeholder.com/15/fc5647/000000?text=+) `#fc5647`
- ![#000000](https://via.placeholder.com/15/000000/000000?text=+) `#000000`
- ![#FFFFFF](https://via.placeholder.com/15/FFFFFF/000000?text=+) `#FFFFFF`
- ![#f7584a](https://via.placeholder.com/15/f7584a/000000?text=+) `#f7584a`
- ![#A39021](https://via.placeholder.com/15/A39021/000000?text=+) `#A39021`
- ![#666262](https://via.placeholder.com/15/666262/000000?text=+) `#666262`
- ![#807A7A](https://via.placeholder.com/15/807A7A/000000?text=+) `#807A7A`
- ![#d4af37](https://via.placeholder.com/15/d4af37/000000?text=+) `#d4af37`

The color theme I chose was inspired by this [bootstrap theme](https://themes.getbootstrap.com/preview/?theme_id=37702) which combines a combination of bright and dark colors placed against a light background that provides a good contrast. Overall this creates an aesthetically pleasing site for the user. 

Validation messages are displayed in the natural colours of green for success, red for errors and yellow for information.

### Typography

[Jost](https://fonts.google.com/specimen/Jost) - used for all elements on the site.

I chose this font as I thought its sharpness and narrowness added a professional design and look to the overall site.

## Technologies Libraries and Frameworks

- !["HTML5 Badge"](https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white) - [HTML 5](https://www.w3.org/TR/html52/)  is a markup language that was used to display the content of the site.
- !["CSS Badge"](https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white) - [CSS](https://www.w3.org/standards/webdesign/htmlcss.html) is a style sheet language used for presenting/styling the content of the site. 
- !["Javascript Badge"](https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) - [Javascript](https://www.javascript.com/) is a scripting language that was used to provide interactivity to the site.
- !["Jquery"](https://img.shields.io/badge/jquery%20-%230769AD.svg?&style=for-the-badge&logo=jquery&logoColor=white) - [Jquery](https://jquery.com/) is a Javascript library that was used for HTML DOM tree traversal and manipulation on the site.
- !["Google Fonts"](https://img.shields.io/badge/-Google%20Fonts-red?logo=Google) - [Google Fonts](https://fonts.google.com/) is a library of free licensed font families that was used to import the Jost font.
- !["Font Awesome Badge"](https://img.shields.io/badge/Font_Awesome-5.14-339AF0?logo=font-awesome) - [Font Awesome](https://fontawesome.com/) is a font and icon toolkit that was used to generate the icons used throughout the site. 
- !["Git Badge"](https://img.shields.io/badge/git%20-%23F05033.svg?&style=for-the-badge&logo=git&logoColor=white) - [Git](https://git-scm.com) is an open source distributed version control system that was used to track any changes made to the source code. 
- !["Github Badge"](https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white) - [Github](https://github.com/) is a platform for hosting software development and version control using Git. This was the remote depository used for the site. 
- !["Python Badge"](https://img.shields.io/badge/python-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white) - [Python](https://www.python.org/) is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. Python was used along with various libraries to access the database and present information to the user. 
- !["Heroku Badge"](https://img.shields.io/badge/heroku-%23430098.svg?&style=for-the-badge&logo=heroku&logoColor=white) - [Heroku](https://www.heroku.com/)  is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. Heroku was used for deploying and hosting the site.
- !["Django Badge"](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) - [Django](https://www.djangoproject.com/) Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source. Primary framework used for building the site. 
- !["Bootstrap Badge"](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white) - [Bootstrap](https://getbootstrap.com/) Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains CSS- and JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components. Used for styling and building front end structure.
- !["AWS Badge"](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white) - [Amazon AWS](https://aws.amazon.com/) Amazon Web Services, Inc. is a subsidiary of Amazon providing on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis. AWS was used to store/render static and media files.
- !["Stripe"](https://img.shields.io/badge/-Stripe-blue) - [Stripe](https://stripe.com/) - Stripe is a developer-oriented commerce company helping small and large companies accept web and mobile payments. Stripe was used for processing payments on the site. 

## Resources and Tools

- [VS Code](https://code.visualstudio.com/) - IDE used for writing and testing source code. 
- [W3C Markup Validation Service](https://validator.w3.org/) - Used for validating HTML source code. 
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used for validating CSS source code.
- [Jslint](http://jslint.com/) - code quality tool used to check whether source code complies with coding rules
- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) - Used to test the responsiveness of site on different screen sizes and also used for debugging and checking network activity
- [Balsamiq](https://balsamiq.com/) - Mockup application tool used to draw wireframes for the application. 
- [ami.responsivdesign.is](http://ami.responsivedesign.is) - Used to make a mockup of the application shown at the beginning of README.md file.
- [Lighthouse](https://developers.google.com/web/tools/lighthouse/) - Used to test the quality and performance of the application. 

## Testing

The application was built using [VS Code](https://code.visualstudio.com). Django was used to run the site on localhost and to conduct testing throughout the development process.

### Validation 

- I validated the HTML source code using the [HTML Validation Service](https://validator.w3.org). Main errors: 
1. Error: Element img is missing required attribute src - Image source was placed in CSS file as they were not properly rendering in src attribute.
2. Error: Element p not allowed as child of element span in this context - removed p element from span 
3. Error: Element div not allowed as child of element ul in this context - removed div element containing class dropdown-divider and replaced it with hr element
4. Error: Error: Duplicate ID navbarDropdown - numbered each id like navbarDropdown1 etc .. 
5. Error: Error: Element li not allowed as child of element div in this context - removed extra unnecessary ul element closing tag
- The CSS passed without any errors - [CSS Validation Service](https://jigsaw.w3.org/css-validator/)

### Manual Testing 

Testing was conducted on the finished application using Django in VS Code and with Chrome Developer Tools. I also tested the application on different browsers. A full report on the manual testing process that tests functionality, usability, responsiveness and performance is available [here](https://github.com/seamusmacg/fixit_v1/blob/master/TESTING.md).

## Major Bugs
- There was issues loading exported database to Heroku Postgres - fixed this by changing the encoding of JSON DB file to UTF-8
- Bug "Value too long for type character varying(20)" - Fixed this by slicing the length of the order number to 10 characters in length in the Order Model. 
- While trying to debug an error with the BlogPost model I deleted the blog table from the Postgres DB on Heroku - this prevented me from migrating the blog to Heroku. To fix this I deleted the Blog app and created a copy called Weblog and migrated that as a new app to Heroku. 

## Database
- On the local development environment a SQLite database was used. SQLite is a relational database management system contained in a C library. 
- On the production environment (Heroku) a Postgres database was used. PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance.

### Models
The site consists of seven models in total: 
- In **Products** app - the models are the **Products** and **Category** models which were used to display the products and respective categories to the user. The models are related by a foreign key field (Category)
- In **Profiles** app - the model is **Profile** which is used to create a user  profile containing such information as name, address etc.  
- In **Checkout** app - the models are the **Order** and **OrderItem** models which are used for gathering information about the user's order and for processing the order. The models are related by a foreign key field (Order)
- In **Weblog** app - the models are the **Category** and **Post** models which are used for creating blog entries with an associated category. The models are related by a foreign key field (Category). The main CRUD functionality of the site is in the Weblog app with administrators able to create, delete and edit blogs/categories. 

### DB Schema

>-  Schema of the database

!["DB Schema"](https://github.com/seamusmacg/fixit_v1/blob/master/mockups/db-schema.PNG)


## Deployment

The application was deployed through Heroku pages as follows:

1. Created a local repository (in Virtual Environment) on my local machine which included all the application files and directories. 
2. Initialized the repository through VS Code Source Control 
3. Created a repository on Github with same name. 
4. Staged and committed all the files with appropriate messages. Github repository was connected to Heroku and automatic deploys enabled. 
5. Manually deployed on Heroku. Heroku
Products and Categories were created from admin panel rather than from fixtures file so in order to successfully deploy to Heroku:
- Dumped data: python manage.py dumpdata > db.json
- Load data: python manage.py loaddata db.json
- Migrate DB to Heroku: heroku run python3 manage.py migrate
5. In Deploy section on Heroku, I retrieved the [live URL](https://fix-it.herokuapp.com/).
6. To run the project on your own machine: 
    - **Step 1**: Go to the repository - https://github.com/seamusmacg/fixit_v1
    - **Step 2**: Click "Code" and copy URL 
    - **Step 3**: Open a terminal or CLI on your machine.
    - **Step 4**: Navigate to the directory you wish to locate the repository. 
    - **Step 5**: Type 'git clone' and then paste the URL copied from above. 
    - **Step 6**: Press **Enter** and a clone of the repository will be created. 


## Credits
- [Bootstrap Theme](https://themes.getbootstrap.com/preview/?theme_id=37702) I used this Shopper E-Commerce template for inspiration and design/structural ideas
- [Unsplash](https://unsplash.com/) All images on the site including product images and background images sourced here
- [Django Documentation](https://docs.djangoproject.com/en/3.2/) - Used throughout project as reference 
- [Stripe Documentation](https://stripe.com/docs) - Used as reference when designing payment process
- [W3schools](https://www.w3schools.com/)
- [CSS-Tricks](https://css-tricks.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Udemy Django Course](https://www.udemy.com/course/python-django-2021-complete-course/) - Supplementary django course used for reference
- [Codemy Django Blog Tutorial](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) - Tutorial on creating blog using Django
- [First Blog Article](https://www.amfam.com/resources/articles/support-for-your-dream/why-diy-5-reasons-to-tackle-that-project) - Used text in blog titled "Why DIY? 5 Reasons to Tackle That Project" 
- [Second Blog Article](https://www.familyhandyman.com/project/how-to-fix-a-clogged-toilet/) - Used text in blog titled "How To Use a Plunger" 
- [Third Blog Article](https://www.aircoservice.com/2019/07/11/10-electrical-safety-tips-every-home-owner-should-know-airco-service/) - Used text in blog titled "10 Electrical Safety Tips" 
- [Fourth Blog Article](https://digthisdesign.net/diy-design/want-become-diy-expert-6-stratagies-success/) - Used text in blog titled "How to Become a DIY Expert" 
- [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/) - Used this Code Institute tutorial as the guide and how to for my own project 
- I would like to thank my mentor Adegbenga Adeye for all his guidance and help throughout the duration of this course
- I would like to thank the all the people at the Code Institute for all their help and encouragement throughout this difficult but rewarding course. 