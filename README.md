# Vero Perfume

Vero Perfume is a full stack web application. The site is an e-commerce online shop where sells fine fragrance and perfumes. It provides a smooth online shopping experience to the end users / customers. 

User is able to sign up an account, log in / log out to the account, update account profile, add products to the shopping cart and remove it from the cart, update product item quantity in the cart, delete the item from the cart. Signed in user is able to add or delete product reviews and ratings. Signed in user is able to add or delete the product to the wishlist. 

The site processes online orders, provides online secured payment method Stripe and fast delivery service. Signed in user is able to checkout and pay for the order. The site is accessible across the devices tested using different browsers. The site sends out marketing newsletters directly to customers and has a Facebook page to promote the products. 

The following card number can be used to checkout an order:

4242 4242 4242 4242 - 04/24 242 42424.

Deployed live site: [Vero Perfume](https://veroperfume.herokuapp.com/)

![Screen views](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/screen-view1.png)


# Table of Content

- [UX](#ux)
    + [Epics & User Stories](#epics---user-stories)
      - [Epic 1 - Django Admin](#epic-1---django-admin)
      - [Epic 2 - Home & Contact app](#epic-2---home---contact-app)
      - [Epic 3 - Products app](#epic-3---products-app)
      - [Epic 4 - Cart app](#epic-4---cart-app)
      - [Epic 5 - Profiles app](#epic-5---profiles-app)
      - [Epic 6 - Checkout app](#epic-6---checkout-app)
  * [Wireframes](#wireframes)
    + [Desktop](#desktop)
    + [Mobile](#mobile)
  * [Design Choice](#design-choice)
    + [Color Scheme](#color-scheme)
  * [Agile Project Management](#agile-project-management)
    + [Project in progress](#project-in-progress)
    + [Project done](#project-done)
    + [Database ERD](#database-erd)
      - [Models](#models)
    + [Business Model](#business-model)
      - [Marketing](#marketing)
      - [Search Engine Optimisation (SEO)](#search-engine-optimisation--seo-)
      - [Mailchimp newsletter subscription](#mailchimp-newsletter-subscription)
- [Exisiting Features](#exisiting-features)
  * [Home Page](#home-page)
      - [Home page desktop](#home-page-desktop)
      - [Home page mobile](#home-page-mobile)
  * [Products Page](#products-page)
  * [Product Details Page](#product-details-page)
  * [Shopping Cart Page](#shopping-cart-page)
  * [Checkout Page](#checkout-page)
  * [User account & Profile page](#user-account---profile-page)
      - [Account sign up](#account-sign-up)
      - [Verify email address](#verify-email-address)
      - [Confirmation email](#confirmation-email)
      - [Confirma email page](#confirma-email-page)
      - [Sign up confirmed](#sign-up-confirmed)
      - [Account sign out](#account-sign-out)
      - [Reset account password](#reset-account-password)
      - [Reset password feedback](#reset-password-feedback)
      - [Account profile](#account-profile)
  * [Wishlist page](#wishlist-page)
  * [Admin Product management page](#admin-product-management-page)
  * [Contact us page](#contact-us-page)
  * [Policy page](#policy-page)
  * [404 page](#404-page)
  * [Django admin panel](#django-admin-panel)
  * [Future developments](#future-developments)
- [Technologies Used](#technologies-used)
  * [Languages & Frameworks](#languages---frameworks)
  * [Others Programs](#others-programs)
- [Testing](#testing)
- [Deployment](#deployment)
  * [Heroku App](#heroku-app)
    + [Set up](#set-up)
    + [Steps to deploy Vero Perfume app to Heroku](#steps-to-deploy-vero-perfume-app-to-heroku)
  * [Amazon Web Services S3](#amazon-web-services-s3)
  * [Clone Project](#clone-project)
  * [Fork Project](#fork-project)
- [Credit](#credit)
  * [Content](#content)
  * [Media](#media)
  * [Code](#code)
- [Acknowledgement](#acknowledgement)


# UX

### Epics & User Stories

* #### Epic 1 - Django Admin 
    |  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
    | --------------- | -------------- | --------- | --------| -------------|
    | [#1](https://github.com/VeronicaLourens/vero-perfume/issues/1) Admin CRUD | As a shop owner  | I want to navigate the admin panel so that I can create, read, update and delete data on the site. | Django admin | Must Have |
    | [#2](https://github.com/VeronicaLourens/vero-perfume/issues/2) Admin add, update and delete product | As a shop owner  |  I want to add, update and delete product so that I can easily add new product or delete unavailable product on the site as well as update product information.| Django admin | Must Have |
    | [#3](https://github.com/VeronicaLourens/vero-perfume/issues/3) Admin edit product | As a shop owner  |  I want to edit the product so that I can update the product information.| Django admin | Must Have |
    | [#4](https://github.com/VeronicaLourens/vero-perfume/issues/4)  Admin manage reviews | As a shop owner  |  I want to manage the customer review so that I can filter out and approve the reviews that user wants to post on the site.| Django admin | Must Have |
    | [#5](https://github.com/VeronicaLourens/vero-perfume/issues/5)  Admin receive payment| As a shop owner  |  I want to receive payment from customers so that I can enjoy doing business.| Django admin | Must Have |
    | [#6](https://github.com/VeronicaLourens/vero-perfume/issues/6)  Send newsletter| As a shop owner  |  I want to send the newsletters out so that I can promote the products to customer with updates for more business.| Django admin | Should Have |

[Back to top](#vero-perfume)

* #### Epic 2 - Home & Contact app
    |  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
    | --------------- | -------------- | --------- | --------| -------------|
    | [#7](https://github.com/VeronicaLourens/vero-perfume/issues/7)  Navigate the site| As a shopper  |   I want to navigate the site easily so that I know what products the site sells to see if I am interested or not.| home | Must Have |
    | [#8](https://github.com/VeronicaLourens/vero-perfume/issues/8) Access the site | As a shopper  | I want to access the site easily so that I can view the site on any media screens using different browsers.| home | Must Have |
    | [#18](https://github.com/VeronicaLourens/vero-perfume/issues/18) View messages | As a shopper  |  I want to view messages so that I know my activities when updating my shopping cart or make a payment. | home | Should Have |
    | [#31](https://github.com/VeronicaLourens/vero-perfume/issues/31)  Access social media / Facebook page| As a shopper  |  I want to access the shop's social media platform so that I can follow the shop and get updates instantly. | home | Could Have |
    | [#32](https://github.com/VeronicaLourens/vero-perfume/issues/32) Contact site owner | As a shopper  | I want to make contact to the site owner so that I can contact the owner for any questions.  | Contact | Should Have |
    | [#33](https://github.com/VeronicaLourens/vero-perfume/issues/33) Advertise shop / product | As a shop owner  | I want to advertise my shop and product so that I can have more customers to buy my products.  | home | Could Have |

[Back to top](#vero-perfume)

* #### Epic 3 - Products app
    |  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
    | --------------- | -------------- | --------- | --------| -------------|
    | [#9](https://github.com/VeronicaLourens/vero-perfume/issues/9)  View product list| As a shopper  |  I want to view the list of products so that I know what product the site sells. | product | Must Have |
    | [#10](https://github.com/VeronicaLourens/vero-perfume/issues/10) View product details | As a shopper  |  I want to view the product details so that I can have enough information about the individual product before I purchase. | home | Must Have |
    | [#11](https://github.com/VeronicaLourens/vero-perfume/issues/11)  Filter and view search product result| As a shopper  |  I want to filter products so that I can quickly find the products I am looking for. | products | Should Have |
    | [#12](https://github.com/VeronicaLourens/vero-perfume/issues/12) Sort products by a specific category  | As a shopper  |  I want to find the best priced or best rated product in a specific category so that I can easily find what I want. | products | Should Have |
    | [#30](https://github.com/VeronicaLourens/vero-perfume/issues/30) Post / delete review and rate a product | As a registered shopper  | I want to post, delete review or rate a product / shop so that I can share my opinion to the others.  | products | Could Have |
    | [#35](https://github.com/VeronicaLourens/vero-perfume/issues/35) View and select product size | As a shopper  |  I want to view and select the product size so that I can buy the product with the size and the price as I wish.| products | Should Have |

[Back to top](#vero-perfume)

* #### Epic 4 - Cart app
    |  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
    | --------------- | -------------- | --------- | --------| -------------|
    | [#14](https://github.com/VeronicaLourens/vero-perfume/issues/14)  Add / delete product in the shopping cart| As a shopper  |  I want to add or delete products from the shopping cart so that I know what products and the amount of products I would buy. | cart | Must Have |
    | [#15](https://github.com/VeronicaLourens/vero-perfume/issues/15) View the total product in the shopping cart | As a shopper  |  I want to view the products in my shopping cart so that I know what I buy and the total cost for the products. | cart | Should Have |
    | [#16](https://github.com/VeronicaLourens/vero-perfume/issues/16)  View policy documents| As a shopper  | I want to view the site's documents so that I know the site's terms and conditions when purchasing the product.  | home | Should Have |
    | [#17](https://github.com/VeronicaLourens/vero-perfume/issues/17) Update quantity in the shopping cart | As a shopper  | I want to update the product quantity in my shopping cart so that I can easily add or delete the same product in my shopping cart.  | cart | Should Have |

[Back to top](#vero-perfume)

* #### Epic 5 - Profiles app
    |  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
    | --------------- | -------------- | --------- | --------| -------------|
    | [#13](https://github.com/VeronicaLourens/vero-perfume/issues/13) Add / delete product to wishlist | As a shopper  |  I want to add / delete product to my wish list so that I can easily select the products to purchase. | products | Should Have |
    | [#19](https://github.com/VeronicaLourens/vero-perfume/issues/19)  Register an account| As a shopper  | I want to register an account so that I can manage my activities on the site.  | profiles | Must Have |
    | [#20](https://github.com/VeronicaLourens/vero-perfume/issues/20) Login / log out | As a registered shopper  |   I want to login and logout so that I can access my account and manage my purchase on the site. | profiles | Must Have |
    | [#21](https://github.com/VeronicaLourens/vero-perfume/issues/21)  Edit / delete account profile| As a registered shopper  | I want to edit or delete account so that I can personalize my own account profile or delete my account as I wish.  | profiles | Must Have |
    | [#22](https://github.com/VeronicaLourens/vero-perfume/issues/22) Verify email address | As a shopper  | I want to verify my email address so that I can be sure the security of my account and purchase on the site.  | profiles | Must Have |
    | [#23](https://github.com/VeronicaLourens/vero-perfume/issues/23) Receive feedback | As a  registered shopper  |  I want to receive feedback so that I can verify my activities on the site. | profiles | Should Have |
    | [#24](https://github.com/VeronicaLourens/vero-perfume/issues/24) Reset account password | As a  registered shopper  | I want to reset my account password so that I can be sure that I can access my account again in case I forgot the password.  | profiles | Should Have |
    | [#25](https://github.com/VeronicaLourens/vero-perfume/issues/25) Subscribe newsletter | As a  registered shopper  |   I want to receive newsletters so that I receive regular updates about the products. | home | Could Have |
    | [#26](https://github.com/VeronicaLourens/vero-perfume/issues/26) Unsubscribe newsletter  | As a  registered shopper  | I want to unsubscribe newsletters so that I can no longer receiving regular newsletters.  | home | Could Have |
    | [#27](https://github.com/VeronicaLourens/vero-perfume/issues/27) View purchase history | As a shopper  | I want to view my purchase history so that I can see what I have bought in the past.  | profiles | Should Have |

[Back to top](#vero-perfume)

* #### Epic 6 - Checkout app
    |  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
    | --------------- | -------------- | --------- | --------| -------------|
    | [#28](https://github.com/VeronicaLourens/vero-perfume/issues/28) Checkout and pay  | As a registered shopper  | I want to check out and pay online so that I can complete the purchase.  | checkout | Must Have |
    | [#29](https://github.com/VeronicaLourens/vero-perfume/issues/29) Receive order confirmation | As a registered shopper  |   I want to receive confirmation after paying so that I know whether my purchase is successful or not. | checkout | Must Have |
    | [#34](https://github.com/VeronicaLourens/vero-perfume/issues/34)  Process online orders| As a shop owner | I want to process orders online so that I can sell products online  | checkout | Must Have |


[Back to top](#vero-perfume)

## Wireframes

I used ```Balsamiq``` to create basic site structure to visualize the site’s potential features which helps me to understand better what needs to be done for the project. The end result might slightly different due to the project development.

* ### Desktop

    * Home page
    ![Home page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/desktop/home.png)

    * <details><summary>Sign up page</summary>

        ![Sign up page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/desktop/signup.png)

     </detials>

    * <details><summary>Login page</summary>

        ![Login page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/desktop/login.png)

    </detials>

    * <details><summary>Profile page</summary>

        ![Profile page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/desktop/profile.png)

    </detials>

    * <details><summary>Product page</summary>

        ![Product page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/desktop/product.png)

    </detials>

    * <details><summary>Product detail page</summary>

        ![Product detailpage](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/desktop/product-detail.png)

    </detials>

    * <details><summary>Shopping cart page</summary>

        ![Shopping car page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/desktop/shopping-bag.png)

    </detials>

    * <details><summary>Checkout page</summary>

        ![Checkout page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/desktop/checkout.png)

    </detials>

    * <details><summary>Order cinfirmation page</summary>

        ![Order confirmation page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/desktop/order-confirmation.png)

    </detials>

[Back to top](#vero-perfume)

* ### Mobile

    * Home page
    ![Home page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/mobile/home.png)

    * <details><summary>Sign up page</summary>

        ![Sign up page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/mobile/signup.png)

     </detials>

    * <details><summary>Login page</summary>

        ![Login page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/mobile/login.png)

    </detials>

    * <details><summary>Profile page</summary>

        ![Profile page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/mobile/profile.png)

    </detials>

    * <details><summary>Product page</summary>

        ![Product page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/mobile/product.png)

    </detials>

    * <details><summary>Product detail page</summary>

        ![Product detailpage](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/mobile/product-detail.png)

    </detials>

    * <details><summary>Shopping cart page</summary>

        ![Shopping car page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/mobile/shopping-bag.png)

    </detials>

    * <details><summary>Checkout page</summary>

        ![Checkout page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/mobile/checkout.png)

    </detials>

    * <details><summary>Order cinfirmation page</summary>

        ![Order confirmation page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/wireframes/mobile/order-confirmation.png)

    </detials>

[Back to top](#vero-perfume)

## Design Choice

The site uses white background with high quality colorful images in a carousel sideshow for the landing page. The site is intuitive with great color contrast which is very user friendly. The project is designed for potentially being used in a real e-commerce online web shop that can be used for both the shopper and the site owner. The application was created using Django MVC structure.

### Color Scheme

I have chosen the white color for the site's background and using purple and blue colors for the buttons.
    ![Color theme](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/color-theme.png) 

[Back to top](#vero-perfume)

## Agile Project Management

I used GitHub Agile project management tool to create user stories using issues and planned the user stories into three different stages using Kanban board with three columns that are ```To do```, ```In progress``` and ```Done```. The user stories are labeled with **MoSCoW** techniques to prioritize the project’s tasks.

### Project in progress

![Agile](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/agile.png)

### Project done

![Future development](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/agile-done.png)

### Database ERD

I used ```Lucidchart``` to create the project's database schema models which helps me to unserstand the relationship between the models. Heroku Postgres database and the SQLite are used for the project.

![ERD](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/ERD.png)

#### Models
* **User** - It is used for user information and purchase history.
* **Django User** - It is the Django built-in User model.
* **Product** - It is used for the product information.
* **Catagory** - It is used for the category of the products.
* **Brand** - It is used for the product's brand.
* **OrderLineItem** - It is used for combining the product with the order.
* **Order** - It is used for the order placed by the user when processing online purchase.
* **Review** - It is used for the customer to review the product / shop.
* **Wishlist** - It is used for the shopper to save a product on their wishlist for easy access.
### Business Model
The Vero Perfume application is a B2C business model that it does the business directly with the end customer. Customer is able to search the product on the site, complete the order, make a payment through secured payment system and receive goods in the end.
* #### Marketing
    Vero Perfume has a Facebook page for reaching all the customers instantly. Shop owner is able to post any updates or promotions to gather sales. The Facebook page provides a great effective way of communicating with shoppers.

    I created ```Vero Perfume Facebook page```. However, the page was only for the education purpose of the e-commerce project and it's not a real business page. Therefore, I made a screenshot of the Facebook page and deleted it afterwards in order to avoid any problems under Facebook's rules. The Facebook link in the footer opens the link to Facebook but not the actual ```Vero Perfume Facebook page```. Here is the one but deleted page.

    ![Vero Perfume Facebook page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/vero-fackbook.png)

[Back to top](#vero-perfume)

* #### Search Engine Optimisation (SEO)
    I added two meta tags with names of keywords and description on the page head, and I generated robots.txt and sitemap.xml to allow Google and search engines bot crawling.

* #### Mailchimp newsletter subscription
    Vero Perfume sends out regular newsletters and user can subscribe using email address. This is a great way for store owner to reach out existing and potential customers with any updates or promotions.

    ![Newsletter](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/newsletter.png)


# Exisiting Features

Vero Perfume application contains total 25 pages including the popup modals.

All of pages have the same navigation menu and the same footer. The dynamic navigatoin menu provides an easy way of browsing all pages with dropdown lists. Vero Perfume logo image is on the top left, a search bar in the middle, account and wishlist and shopping cart on the right.

The search bar provides a quick way of searching for the products. The site provides sorting and filtering functionalities on the products page to search for the products.

The footer contains a mailchimp newsletter subscription form on the left, the Facebook page, contact us and policy clickable links on the right, the copyright and disclaimer on the bottom.

## Home Page
The site's landing page with carousel images to show that the online shop sells perfume.

* #### Home page desktop

    ![Home page desktop](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/landing-page.png)

* #### Home page mobile

    ![Home page mobile](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/home-m.png)

[Back to top](#vero-perfume)

## Products Page
Products page contains a list of different perfumes available on the site. Every product has name, price, brand tag, gender and star ratings. Store owner is able to add products, edit and delete products on the site.

* General user views the page.

    ![Products page](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/products.png)

* Store owner views the page with add button on the top left corner, edit and delete links
    
    ![Products page](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/products-admin.png)


[Back to top](#vero-perfume)

* Store owner deletes product modal

  

    ![Product details 1](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/admin-delete-product-modal.png)

  

[Back to top](#vero-perfume)

## Product Details Page
Product details page contains image, name, brand tag, star ratings, size, quantity form, description, back and add to cart buttons, wishlist icon link and product reviews.

* General user views the page with product reviews.

    ![Product details with reviews](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/g-detail.png)

[Back to top](#vero-perfume)    

* General user views the page without product reviews.
    

    ![Product details no reviews](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/g-detail-n.png)

    

* Signed in user views the page with product reviews and post a review form. Signed in user is able to delete own review with a delete link.
    

    ![Product details 1](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/s-detail.png)

    
* Store owner views the page with edit, delete, product reviews and post a review form.

    ![Product details 1](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/adm-detail.png)

   

* Delete reviews modal

   

    ![Product details 1](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/delete-reviews-modal.png)

    

* Product details mobile

    ![product details mobile](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/products-mobile.png)

[Back to top](#vero-perfume)

## Shopping Cart Page

User is able to add product to the cart, update the product quantity and remove the product from the cart as user wishes.

* Add product to the shopping cart-1

    ![Add to cart](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/ad-cart.png)

* Add product to the shopping cart-2

    ![Add product to cart](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/add-product-to-cart.png)
   
[Back to top](#vero-perfume)

* Shopping cart overview desktop

    ![Shopping cart](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/shopping-cart-total.png)

* Shopping cart overview mobile

    ![Shopping cart mobile](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/cart-m.png)

[Back to top](#vero-perfume)

* Update shopping cart

    ![Update shopping cart](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/cart-update.png)

   

[Back to top](#vero-perfume)

* Remove product to shopping cart

    ![Remove product](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/cart-delete-item.png)

    

[Back to top](#vero-perfume)

## Checkout Page

Checkout page contains a delivery details form and payment card authorization form for user to fill in for completing the order. There is an order summary where user can clearly see the items and total amount of the order. The site uses the Stripe payment method to process the eletronic money transfer.

* Checkout page desktop

    ![Checkout](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/checkout.png)

* Checkout page mobile

    ![Checkout mobile](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/checkout-m.png)


* Stripe

    ![Stripe](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/stripe1.png)

   

* Checkout success page / order confirmation

    ![Checkout](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/checkout-success.png)

[Back to top](#vero-perfume)

* Order details from profile page

    ![Checkout](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/checkout-success-from-profile.png)

    

* Order confirmation email to the user

    I used my Gmail account and the ```Gmail SMTP server``` to send emails to the user when the user complete the online orders.

    ![Email confirmation](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/gmail-order.png)

   

[Back to top](#vero-perfume)

## User account & Profile page

User signs up an account with filling in the personal details the sign up form. Then Vero Perfume sends an email to the user with a link asking the user to verify the email address. The user's account is completed once the user click the confirm button. And the user is redirected to the sign in page.


* #### Account sign up

    ![Sign up](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/account-sign-up.png)

* #### Verify email address

    ![Confirmation email](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/verify-email.png)

[Back to top](#vero-perfume)

* #### Confirmation email

    ![Email with link](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/verify-email-link.png)

* #### Confirma email page

    ![Confirmation](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/verify-email-confirm.png)

[Back to top](#vero-perfume)

* #### Sign up confirmed

    ![Sign up confirmed](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/verify-signup-confirm.png)


* #### Account sign out

    ![Sign out](https://veroperfume.s3.eu-west-2.amazonaws.com/media/images/sign-out.png)


* #### Reset account password

    ![Reset password](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/password-reset.png)

[Back to top](#vero-perfume)

* #### Reset password feedback

    ![Feedback](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/password-reset-fb.png)

* #### Account profile

    ![Profile](https://veroperfume.s3.eu-west-2.amazonaws.com/media/images/profile.png)

   

[Back to top](#vero-perfume)

## Wishlist page
Logged in user is able to add and remove the product to the wishlist. There is a link to the product's detail page if user wishes to view the product details. The error message shows up if the item exist in the wishlist.

* Wishlist overview
    ![Wishlist](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/wishlist-total.png)

* Add product to wishlist
    ![Add to wishlist](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/wishlist-add.png)

* Remove product from wishlist
    ![Remove from wishlist](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/wishlist-remove.png)

* wishlist error
    ![Add error](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/wishlist-error.png)

## Admin Product management page
Store owner is able to add, delete and edit the product on the site.

* Admin add product

    ![Add product](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/admin-add-product.png)

   

* Store owner is able to edit the product through the form
    <details><summary>Edit product form</summary>

    ![Edit product](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/products-admin-edit.png)

    </detials>

* Admin delete product

    ![Delete product](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/admin-delete-product.png)

    

[Back to top](#vero-perfume)

## Contact us page
User is able to contact store owner via the contact us form in the footer.

![Contact us](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/contact-us.png)

[Back to top](#vero-perfume)

## Policy page
Vero perfume has a detailed privacy policy to let user know the policies.

* 

    ![Policy](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/policy.png)

    

[Back to top](#vero-perfume)

## 404 page
User is redirected to the ```404 page``` when accessing to any non-existing page. There is a message to user with a ```Return to Home``` button.

![404](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/404.png)

## Django admin panel
Admin / store owner is albe to manage the site's data in the admin panel. Admin can add, edit and delete products, brands, categories, add or delete users, reviews, wishlists, see the messages received from the contact form, receives the completed online orders and the payment user made.

* Admin account panel
![Admin](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/admin1.png)

[Back to top](#vero-perfume)

* Admin delete user
![Delete user](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/admin-delete-user.png)

[Back to top](#vero-perfume)

* Admin views the list of products
![Products](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/admin-product.png)

[Back to top](#vero-perfume)

* Admin views the list of orders
![Orders](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/admin-orders.png)

[Back to top](#vero-perfume)

* Admin views the order details
![Order details](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/admin-order-details.png)

[Back to top](#vero-perfume)

## Future developments

* Send out newsletters can be added to the application;
* Unsubscribe newsletter feature can be added;
* Inventory tracking system can be implemented;
* Store owner can receive the payment;
* Shipping methods and package tracking can be added to the application;


# Technologies Used
## Languages & Frameworks
* [HTML5]() - used to create site.
* [CSS]() -used to add individual styling.
* [JavaScript]() - used to add interactive features.
* [Python]() - used to add backend functionality.
* [Django]() - used to build the project.
* [Bootstrap]() - used to style the websie.


## Others Programs
* [Heroku]() - used to deploy and host the project's live site.
* [Heroku PostgreSQL]()  - used to connect the project to the database.
* [GitHub Git]() - used to host the project's code and version control.
* [GitPod]() - used to write and push the code for the project.
* [Balsamiq]() - used to create project's wireframes.
* [Chrome Dev Tools]() - used to debug and light house testing.
* [Adobe Color]() - used to extract the color theme.
* [W3C Markup Validation Service]() - used to validate the HTML code.
* [W3C CSS Validation Service]() - used to validate CSS code.
* [Am I Responsive]() - used to generate the responsive preview screens.
* [Responsive Design Checker]() - used to check responsiveness.
* [Lucidchart]() - used to create the database ER diagram.
* [Font Awesome]() - used to download the icons.
* [Google Fonts]() - used to style the text.
* [Compressor.io]() - used to compress the images and screenshots.
* [Facebook]() - used to create site's Facebook marketing page.
* [Stripe]() - used to process the online payment with webhooks.
* [AWS Bucket]() - used to host static files.
* [Sitemap]() - used to generate the sitemap.xml
* [Privacypolicygenerator.info]() - used to generate the size's privacy policy

[Back to top](#vero-perfume)

# Testing

View the site's testing documentation here [TESTING.md](TESTING.md)

[Back to top](#vero-perfume)

# Deployment

The project has been deployed to **Heroku** in the early stage of the proejct development just after creating the site's basic functionalities with the base and basic home page. Created **Procfile** and set up environment variables in my project development environment that helped to successfully deploy the project to Heroku.

## Heroku App

* ### Set up

1. I used Code Institute GitPod full template to set up an environment to created the project. Installed Django and required packages / libraries using commands in GitPod terminal.

    * ```pip3 install Django==3.2 gunicorn```

    * ```pip3 install dj_database_url psycopg2```

    * ```pip3 install dj3-cloudinary-storage```

    * ```pip3 freeze --local > requirements.txt```

2. Create Procfile

    ![Profile](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/procfile.png)

3. Attach Heroku Postgres

    Navigate to the ```Resources``` tab to attach Heroku Postgres datablse.

    ![Heroku Postgres](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/heroku1.png)

4. Set up Config Vars in Heroku

    UNavigate to the ```Settings``` tab to set up the Config Vars.

    ![Configvars](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/configvars.png)

* ### Steps to deploy Vero Perfume app to Heroku


    1. Login to my Heroku account and click ```Create new app```;
    2. Give my app a name **veroperfume** and select Europe and click ```Create app``` button;
    3. Go to the **Resource** tab and attach ```Heroku Postgres``` to ```veroperfume app```;
    4. Go to the **Settings** tab and set up **Config Vars** with important data;
    5. Add buildpack ```heroku/python```;
    6. Go to the **Deploy** tab ```Deployment method```, click the **GitHub** icon and the button ```Connect to GitHub```;
    7. Select my GitHub repo ```vero-perfume``` and choose the branch ```main```;
    8. Click ```Enable Automatic Deploys``` and ```Deploy branch```;
    9. The application was deployed successfully after a few minutes.

    10. Heroku deployment screenshot.

        ![Heroku deployment](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/heroku-deployment.png)

[Back to top](#vero-perfume)

## Amazon Web Services S3

The project's static and media files are stored at the cloud-based storage **AWS S3 Bucket**. 

1. Create an account at [AWS Amazon](https://aws.amazon.com/);
2. Create a S3 bucket, go to IAM to create a group and user, manually set the bucket settings;
3. Set up CORS configuration and generate the policy;
4. Add the AWS keys to Heroku config vars and connect AWS to my Django project in the project's deployment environment;
5. Create folders to host the files and images;


[Back to top](#vero-perfume)
## Clone Project

Steps to clone the project from GitHub as following:

* On my GitHub ```vero-perfume``` repository page, click the ```Code``` tab next to the green Gitpod button;

* In the Clone board, click the icon on the right side of the URL under ```HTTPS``` to copy the given URL;

* Go to my local IDE VS Studio Code and click ```Clone Git Repository```.

  
* Paste the copied project's URL to the search bar, then click enter to select a local repository location for the project.

* Select a repository to complete the clone process.

    ![Clone project](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/clone.png)

[Back to top](#vero-perfume)

## Fork Project

To fork Vero Perfume's repository:
* Go to repository ```vero-perfume``` in my Github account;
* Click the tab ```"Fork"``` on the top right of Githtb page;

    ![Fork](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/fork.png)

* Then the repository's copy would be in your Github.

# Credit

[Back to top](#vero-perfume)
## Content

* Vero Perfume project was inspired by [Code Institute]()'s walk through project ```Boutique Ado```. The code for setting up the e-commerce project, product page, shopping cart, the Stripe payment system as well as the JS code are taken and adapted from the tutorial materials.

* I use [Kaggle](https://www.kaggle.com/) to get some of product images and other information.
* I couldn't find the perfume images from the famous brands on the free image website so that I use the official websites to get the product images and other information. Credit to [Gucci](https://www.gucci.com/us/en/ca/beauty/fragrances/fragrances-for-women-c-fragrances-for-women), [Hugo Boss](https://www.hugoboss.com/fragrances-men/),  [DIOR](https://www.dior.com/nl_nl/beauty/geuren/damesgeur/alle-producten), [Chloé](https://www.chloe.com/nl/fragrance_cod46568417bo.html).

[Back to top](#vero-perfume)
## Media

* The carousel images and card images are from [Unsplash]().


## Code

* The code in ```product.js``` is from [How to display content depending on dropdown menue user selection](https://stackoverflow.com/questions/18115916/how-to-display-content-depending-on-dropdown-menue-user-selection)

* The CSS code for the total count of the shopping cart is adapted from [How to put the number at top right corner of cart icon?](https://stackoverflow.com/questions/51304169/how-to-put-the-number-at-top-right-corner-of-cart-icon)

* The Wishlist code was inspired and taken from ```CI Slack``` channel where fellow coders shared the tips and tricks.

* I learned how to implement the contact form for site users to contact the shop owner on Youtube [Code With Stein](https://www.youtube.com/watch?v=dnhEnF7_RyM)

[Back to top](#vero-perfume)
# Acknowledgement

Whilst I have tried to deviate as much as possible, I have taken the certain code from the walk through e-commerce project ```Boutique Ado``` at Code Institute which I learn how to build the e-commerce website for a real world application.

I relied upon the support from Code Institue online [tutors](), mentor [Precious Ijege](), [Slack]() community and my [families](). Great thanks to all of those who support my learning journey.

I use ```Django``` documentation, ```W3schools```, ```YouTube``` and ```Stack Overflow``` for general references throughout the project. I watched the tutorial videos on Youtube to gain extra knowledge about Django framework.

[Vero Perfume](https://veroperfume.herokuapp.com/) website is intended for education purpose of completing the Portfolio Project 5 E-commerce project for the Diploma of Full Stack Software Development course at [Code Institue]().

[Back to top](#vero-perfume)
