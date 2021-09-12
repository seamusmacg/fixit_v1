# Manual Testing 

## Functionality 

###  Links and Buttons

| Component | Intended Function | Works as Intended? | Fix |
| -------------- | ------------------- | ---------------- | --- |
|**Home Link** | Take user to Home page | Yes | N/A |
|**FixIt Title Link** | Take user to Home page | Yes | N/A |
|**About Us Link** | Take user to the About Us section | Yes | N/A |
|**Account Link** | Show user dropdown of sign up, login, manage profile | Yes | N/A |
|**Sign Up Link** | Take user to sign up page | Yes | N/A |
|**Login Link** | Take user to login page | Yes | N/A |
|**Allauth template Links** | Confirm users in sign up process, confirm email etc. | Yes | N/A |
|**Manage profile Link** | Take user to login page | Yes | N/A |
|**Cart Link** | Take user to the Cart page | Yes | N/A |
|**Contact Link** | Take user to the Contact page | Yes | N/A |
|**Profile Link** | Take user to the Profile page | Yes | N/A |
|**Products Link** | Display product options in dropdown | Yes | N/A |
|**Departments Link** | Display department links in dropdown | Yes | N/A |
|**Sort by Price Link** | Take user to products page sorted by price | Yes | N/A |
|**Sort by Rating Link** | Take user to products page sorted by rating | Yes | N/A |
|**Sort by Category Link** | Take user to products page sorted by category | Yes | N/A |
|**All Products Link** | Take user to products page | Yes | N/A |
|**Departments Electrical Link** | Take user to products page showing only electrical products | Yes | N/A |
|**Departments Gardening Link** | Take user to products page showing only gardening products | Yes | N/A |
|**Departments Bathroom Link** | Take user to products page showing only bathroom products | Yes | N/A |
|**Departments Tools Link** | Take user to products page showing only tool products | Yes | N/A |
|**Shop Now** | Take user to the products page | Yes | N/A |
|**Sort Products Link** | Display dropdown of sorting options | Yes | N/A |
|**Sort by Price Link (Low to high)** | Take user to products page sorted by lowest price to high | Yes | N/A |
|**Sort by Price Link (High to low)** | Take user to products page sorted by highest price to low | Yes | N/A |
|**Sort by Rating Link (Low to high)** | Take user to products page sorted by rating lowest price to high | Yes | N/A |
|**Sort by Rating Link (High to low)** | Take user to products page sorted by rating highest price to low | Yes | N/A |
|**Sort by Category Link (A-Z)** | Take user to products page sorted by category A-Z | Yes | N/A |
|**Sort by Category Link (Z-A)** | Take user to products page sorted by category Z-A | Yes | N/A |
|**Sort by Name Link (A-Z)** | Take user to products page sorted by name A-Z | Yes | N/A |
|**Sort by Name Link (Z-A)** | Take user to products page sorted by name Z-A | Yes | N/A |
|**Product Card Image Link)** | Take user to product info page | Yes | N/A |
|**Product Card Category Link)** | Take user to products page sorted by category | Yes | N/A |
|**Product Card Product Name Link)** | Take user to product info page | Yes | N/A |
|**Product Info category link**| Take user to the products page sorted by selected category| Yes | N/A |
|**Product Info Add to Cart Button**| Add selected product to cart | Yes | N/A |
|**Product Info Back to Products link**| Take user back to products page | Yes | N/A |
|**Shopping cart Remove From Cart button** | Remove product from user's cart | Yes | N/A |
|**Shopping cart Checkout button** | Take user to the checkout page | Yes | N/A |
|**Shopping cart Back To Products Link** | Take user to products page | Yes | N/A |
|**Checkout Adjust Bag** | Take user to cart page | Yes | N/A |
|**Checkout Complete Order Button** | Display success page or error if error occurs | Yes | N/A |
|**Back To Home Link with Home Icon** | Take user to home page | Yes | N/A |
|**Contact Send Button** | Submit form and return success page to user | Yes | N/A |
|**Search Button** | Submit query and return products page with the products containing query string in product name or return an error message | Yes | N/A |



### Hover/Focus/Click Effects 

| Component | Intended Function | Works as Intended? | Fix |
| -------------- | ------------------- | ---------------- | --- |
| **Links in Navbar** | Apply light pink background color on hover | Yes | N/A |
| **Shop Now Button** | Apply light grey background on hover | Yes | N/A |
| **Department Buttons** | Apply lighter background colour on hover | Yes | N/A |
| **Footer Links** | Apply underline on hover | Yes | N/A |
| **Submit Buttons** | Apply lighter background color on hover | Yes | N/A |
| **Sort Products** | Apply lighter background color on hover | Yes | N/A |
| **Remove from Cart Button** | Apply lighter background color on hover | Yes | N/A |
| **Back to Products Button** | Apply light grey background color on hover | Yes | N/A |
| **Search Button**| Apply dark background on hover | Yes | N/A |
| **Login/Register Checkbox**| Blue default check when checked | Yes | N/A |



## Usability 

Usability tests were carried out based on user stories as outlined in the README.md file. 

### User Story #1

>- As a user, I want to find and purchase home/DIY related products and have them delivered to my address. 

The user is presented with a link to the products page (Shop Now Button) immediately on landing on the home page. 

Callout Section: 

!["Callout Section with link to products page"](https://github.com/seamusmacg/fixit_v1/blob/master/mockups/callout.PNG)

Catalogue Section: 

!["List of products shown to user"](https://github.com/seamusmacg/fixit_v1/blob/master/mockups/products.PNG)


### User Story #2

>-  As a user, I would like create a profile (delivery details) that I can reuse when I return to the site.

Each registered user's profile is saved with the details they enter at checkout - this can be edited and updated in the profile page. 

!["Profile page"](https://github.com/seamusmacg/fixit_v1/blob/master/mockups/profile.PNG)



## Responsiveness

The application was tested for responsiveness on multiple devices and browser using Developer Tools. Media queries and Bootstrap were used to keep the device responsive across different devices.

| Component | Intended Result | Works as intended? | Fix |
| --------- | --------------- | ------------------ | --- |
| Text | Should be readable and clear for each screen size | Yes | N/A |
| Images | Should be readable and clear for each screen size and not stretched/distorted | Yes | N/A |
| Icons | Maintain ratio at smaller sizes and not be stretched/distorted | Yes | N/A |
| Tables | Maintain ratio and structure at smaller sizes | Yes | N/A |
| Layout | Sections should be structured properly with proper spacing between features | Yes | N/A |
| Functionality | Buttons should work across screen sizes | Yes | N/A |

## Performance Testing 

I ran the [Lighthouse](https://developers.google.com/web/tools/lighthouse/) testing tool for both mobile and desktop to check the quality and performance of the site pages. The site received relatively good ratings in performance, accessibility, Best Practices and SEO ranging from 89 - 90. 

Example Report:
!["Lighthouse Report"](https://github.com/seamusmacg/fixit_v1/blob/master/mockups/lighthouse.PNG)

## Heroku

All the same tests applied in the local environment were also successfully applied on the hosted site (Heroku) without any problems.






