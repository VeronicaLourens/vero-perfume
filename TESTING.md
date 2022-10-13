# TESTING

I have conducted both manual and partly automated testing for Vero Perfume application. 

# Table of Content


  * [Code Validation](#code-validation)
    + [W3C HTML validation report](#w3c-html-validation-report)
      - [Home page](#home-page)
      - [Product page](#product-page)
      - [Product details page](#product-details-page)
      - [Add product](#add-product)
      - [Cart page](#cart-page)
      - [Checkout page](#checkout-page)
      - [Profile page](#profile-page)
      - [Sign in page](#sign-in-page)
    + [W3C CSS validation report](#w3c-css-validation-report)
    + [Python code validation](#python-code-validation)
  * [Responsiveness Testing](#responsiveness-testing)
  * [Browser Compatibility Testing](#browser-compatibility-testing)
  * [Lighthouse Testing](#lighthouse-testing)
      - [Home - desktop](#home---desktop)
      - [Home - mobile](#home---mobile)
  * [Manual Testing](#manual-testing)
    + [Sign up form](#sign-up-form)
      - [Sign up error-1](#sign-up-error-1)
      - [Sign up error-2](#sign-up-error-2)
      - [Sign up error-3](#sign-up-error-3)
    + [Sign in form](#sign-in-form)
      - [Sign in error](#sign-in-error)
    + [Profile form](#profile-form)
      - [Profile form error-1](#profile-form-error-1)
      - [Profile form error-2](#profile-form-error-2)
      - [Profile form error-3](#profile-form-error-3)
      - [Profile form error-4](#profile-form-error-4)
    + [Cart payment](#cart-payment)
      - [Card error 1](#card-error-1)
      - [Card error 2](#card-error-2)
      - [Card error 3](#card-error-3)
    + [Contact us form](#contact-us-form)
      - [Contact form error 1](#contact-form-error-1)
      - [Contact form error 2](#contact-form-error-2)
      - [Contact form error 3](#contact-form-error-3)
      - [Contact form error 4](#contact-form-error-4)
  * [User Story Testing](#user-story-testing)
    + [Epics & User Stories](#epics---user-stories)
      - [Epic 1 - Site Admin](#epic-1---site-admin)
      - [Epic 2 - Home & Contact app](#epic-2---home---contact-app)
      - [Epic 3 - Products app](#epic-3---products-app)
      - [Epic 4 - Cart app](#epic-4---cart-app)
      - [Epic 5 - Profiles app](#epic-5---profiles-app)
      - [Epic 6 - Checkout app](#epic-6---checkout-app)
  * [Automated Testing](#automated-testing)
  * [Unsolved Known Bugs](#unsolved-known-bugs)
      - [Product price](#product-price)
      - [Wishlist count](#wishlist-count)
      - [Product forms validations](#product-forms-validations)
      - [Lighthouse performance bugs](#lighthouse-performance-bugs)
    + [Resolved Bugs](#resolved-bugs)
      - [Product size](#product-size)
      - [BadHeaderError](#badheadererror)
      - [Product admin forms](#product-admin-forms)
      - [Full name form field validation](#full-name-form-field-validation)
      - [Webhooks bug](#webhooks-bug)
      - [W3C HTML validation errors and warnings](#w3c-html-validation-errors-and-warnings)

  

## Code Validation

### W3C HTML validation report

* #### Home page

    ![W3C HTML](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/w3c-html-no-errors.png)

* #### Product page

    ![Product page](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/w3c-product.png)

* #### Product details page

    ![Product details](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/w3c-product-details.png)

[Back to top](#testing)

* #### Add product

    ![Add product](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/w3c-html-add-no-errors.png)

[Back to top](#testing)

* #### Cart page

    ![Cart](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/w3c-cart.png)

* #### Checkout page

    ![Checkout](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/w3c-checkout.png)

[Back to top](#testing)

* #### Profile page

    ![Profile](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/w3c-html-profile-no-errors.png)

* #### Sign in page

    ![Sign in](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/w3c-login.png)

### W3C CSS validation report

![W3C CSS](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/w3c-css-no-errors.png)


[Back to top](#testing)

### Python code validation

* The ```pep8online.com``` was not working for python code validation during the project's code validaion period. 

    ![Pep8online](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/pep8.png)


* I followed the steps from Slack announcement channel to check the code.

    ![Slack](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/slack-msg.png)

* I manually checked all files with indication under the tab ```PROBLEMS``` in my GitPod workspace. The **home**, **cart** and **contact** apps that the Python code files have no issues. 

    ![Proflem-free](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/cart-p.png)

* However, there are a few lines of code that contains too many characters which I opted to fix it due to the unexpected side effects. And some lines in the settings.py and env.py contain the value with a large amount characters.

    * checkout app

        ![Checkout app](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/checkout-p.png)

    * products app

        ![Products app](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/products-p.png)

    * profiles app

        ![Profiles app](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/profile-p.png)

    * settings.py

        ![Settings.py](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/settings.png)

     * env.py 

        ![env.py](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/env.png)
 
 

## Responsiveness Testing

* The website has been manually tested and passed on the **Google Chrome Dev Tools** and the **Responsive Design Checker**.

  |       | **Moto G4** | **Galaxy S5** | **iPhone 5** | **iPad** | **iPad Pro** | **Display < 1200px** | **Display <= 4000px** |
  |-------|:-----------:|:-------------:|:------------:|:--------:|:------------:|:--------------------:|:---------------------:|
  |Render |  &check;    |   &check;     |   &check;    |  &check; |    &check;   |        &check;       |        &check;        |  
  |Image  |  &check;    |   &check;     |   &check;    |  &check; |    &check;   |        &check;       |        &check;        |   
  |Links  |  &check;    |   &check;     |   &check;    |  &check; |    &check;   |        &check;       |        &check;        | 

[Back to top](#testing)

* The website has been tested and passed on my own devices. It is fully responsive on two desktops, two laptops, iPad Air and  three mobile phones while using Google Chrome, Microsoft Edge and Sarari browsers.

  |       |**Samsung Galaxy S22 Ultra**|**Xiaomi 12 pro**|**Huawei P30 Pro**|**iPad Air**|**Lenovo E540**|**HP Elitebook 850 G5**|**DELL 2407WFP**|**Yiyama ProLite XB3288UHSU**|
  |-------|:--------------:|:--------------:|:----------------:|:----------:|:-------------:|:---------------------:|:---------------:|:--------------------------:|
  |Render |    &check;     |   &check;      |      &check;     |   &check;  |    &check;    |        &check;        |     &check;     |        &check;             |
  |Image  |    &check;     |   &check;      |      &check;     |   &check;  |    &check;    |        &check;        |     &check;     |        &check;             |
  |Links  |    &check;     |   &check;      |      &check;     |   &check;  |    &check;    |        &check;        |     &check;     |        &check;             |

[Back to top](#testing)

## Browser Compatibility Testing

Kiwi Piano Studio website has been tested on **Google Chrome**, **Microsoft Edge** and **Safari** browsers. The site's compatibility and the functionality are working fine with no issues.

## Lighthouse Testing

Vero Perfume site has been tested on ```Google Chrome Lighthouse``` function on incognito window for the desktop and mobile screens.

* #### Home - desktop

    ![Home](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/lighthouse-home.png)

* #### Home - mobile

    The Performance score is 64 for the mobile due to the render blocking resources.

    ![Home-m](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/lighthouse-home-m.png)

[Back to top](#testing)

## Manual Testing

### Sign up form

The form fields are required to fill in with valid data. It provides error messages. The email addresses and the password must be filled in with the same email addresses or the same password. The email address must be a valid email address. If account with the username and email address already exist, it gives user hints.

* #### Sign up error-1

    ![Sign up error](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/sign-up-err1.png)

[Back to top](#testing)

* #### Sign up error-2

    ![Sign up error2](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/sign-up-err2.png)

[Back to top](#testing)

* #### Sign up error-3

    ![Sign up error3](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/sign-up-err3.png)

[Back to top](#testing)

### Sign in form

The username and the password must be correct when signing into the account.

* #### Sign in error

    ![Sign in error](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/signin-error.png)

[Back to top](#testing)

### Profile form

The fields are required in the profile form. Full name must be only letters and the phone number must be only numbers.

* #### Profile form error-1

The empty spaces are not allowed .

    ![Profile1](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/profile-form-validations.png)

[Back to top](#testing)

* #### Profile form error-2

The specail characters are not allowed for the full name field. The phone number and postcode fields accept only numbers.

    ![Profile2](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/profile-form-validations1.png)

[Back to top](#testing)

* #### Profile form error-3

    ![Profile3](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/profile-form-validations2.png)

* #### Profile form error-4

The full name field is not allowed to have numbers.

    ![Profile4](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/profile-form-validations3.png)

[Back to top](#testing)

### Cart payment

The order form and the credit card must be valid to complete the online order.

* #### Card error 1

The form must be valid with valid value in the form fields.

    ![Card1](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/card-error1.png)

[Back to top](#testing)

* #### Card error 2

The card must be valid to checkout orders.

    ![Card2](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/card-error2.png)

* #### Card error 3

The card number must be complete.

    ![Card3](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/card-error3.png)

[Back to top](#testing)

### Contact us form

Contact us form has been manually tested. 

* #### Contact form error 1 

Empty space is now allowed and email address must be valid

    ![Contact-1](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/contact-1.png)

[Back to top](#testing)

* #### Contact form error 2

Special signs and characters are not allowed

    ![Contact-2](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/contact-2.png)

[Back to top](#testing)

* #### Contact form error 3

Numbers are not allowed and email address must not be empty

    ![Contact-3](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/contact-3.png)

[Back to top](#testing)

* #### Contact form error 4

Email address must contain an '@'

    ![Contact-4](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/contact-4.png)

[Back to top](#testing)

## User Story Testing

Vero Perfume e-commerce application has total 35 user stories. The finished site has covered and satisfied the 32 user storeis as I manually tested. The other user stories ```#5 #6 and #26``` are left for the future development due the project's current scope. 

The features of user storeis can be views on the [README.md](README.md) page's ```Existing Features``` section.

[Back to top](#testing)

### Epics & User Stories

* #### Epic 1 - Site Admin 

    | User Story |[#1](https://github.com/VeronicaLourens/vero-perfume/issues/1) Admin CRUD  |
    |:-------:|:--------|
    | &check; | Admin is able to perform full CRUD functionality. |

    | User Story |[#2](https://github.com/VeronicaLourens/vero-perfume/issues/2) Admin add, update and delete product  |
    |:-------:|:--------|
    | &check; | Admin is able to perform add, update and delete product both on the site and in the database. |

    | User Story |[#3](https://github.com/VeronicaLourens/vero-perfume/issues/3) Admin edit product  |
    |:-------:|:--------|
    | &check; | Admin is able to edit product. |

    | User Story |[#4](https://github.com/VeronicaLourens/vero-perfume/issues/4) Admin manage reviews  |
    |:-------:|:--------|
    | &check; | Admin is able to manage reviews. |

    | User Story |[#5](https://github.com/VeronicaLourens/vero-perfume/issues/5) Admin receive payment  |
    |:-------:|:--------|
    |  | ```This is yet to implement in the future development```. |

    | User Story |[#6](https://github.com/VeronicaLourens/vero-perfume/issues/6) Send newsletter  |
    |:-------:|:--------|
    |    | ```This is yet to implement in the future development```. |

[Back to top](#testing)

* #### Epic 2 - Home & Contact app

    | User Story |[#7](https://github.com/VeronicaLourens/vero-perfume/issues/7) Navigate the site  |
    |:-------:|:--------|
    | &check; | User is able to navigate the site easily using dynamic navigation dropdown menu and search bar. |

    | User Story |[#8](https://github.com/VeronicaLourens/vero-perfume/issues/8) Access the site  |
    |:-------:|:--------|
    | &check; | User is able to access the site easily on the media screens from ```320px up to 4000px``` using different browsers. |

    | User Story |[#18](https://github.com/VeronicaLourens/vero-perfume/issues/18) View messages  |
    |:-------:|:--------|
    | &check; | User is able to view all the messages when interacting the site from the ```Bootstrap toasts```. |

    | User Story |[#31](https://github.com/VeronicaLourens/vero-perfume/issues/31)  Access social media / Facebook page  |
    |:-------:|:--------|
    | &check; | User is able to visit Vero Perfume's Facebook page for instant updates. |

    | User Story |[#32](https://github.com/VeronicaLourens/vero-perfume/issues/32) Contact site owner  |
    |:-------:|:--------|
    | &check; | User is able to contact Vero Perfume via the contact form on the footer. |

    | User Story |[#33](https://github.com/VeronicaLourens/vero-perfume/issues/33) Advertise shop / product  |
    |:-------:|:--------|
    | &check; | Store owner is able advertise the shop on ```Google``` and ```Facebook```. |

[Back to top](#testing)

* #### Epic 3 - Products app

    | User Story |[#9](https://github.com/VeronicaLourens/vero-perfume/issues/9) View product list  |
    |:-------:|:--------|
    | &check; | User is able to view the product lists on the products page. |

    | User Story |[#10](https://github.com/VeronicaLourens/vero-perfume/issues/10) View product details   |
    |:-------:|:--------|
    | &check; | User is able to view the product lists on the product details page. |

    | User Story |[#11](https://github.com/VeronicaLourens/vero-perfume/issues/11) Filter and view search product result  |
    |:-------:|:--------|
    | &check; | User is able to filter and view search product result. |

    | User Story |[#12](https://github.com/VeronicaLourens/vero-perfume/issues/12) Sort products by a specific category  |
    |:-------:|:--------|
    | &check; | User is able to sort products by a specific category. |

    | User Story |[#30](https://github.com/VeronicaLourens/vero-perfume/issues/30) Post / delete review and rate a product  |
    |:-------:|:--------|
    | &check; | User is able to post / delete review and maek star rating to a product. |

    | User Story |[#35](https://github.com/VeronicaLourens/vero-perfume/issues/35) View and select product size  |
    |:-------:|:--------|
    | &check; | User is able to view and select product size in the size option dropdown. |

[Back to top](#testing)


* #### Epic 4 - Cart app
    | User Story |[#14](https://github.com/VeronicaLourens/vero-perfume/issues/14) Add / delete product in the shopping cart  |
    |:-------:|:--------|
    | &check; | User is able to add / delete product in the shopping cart. |

    | User Story |[#15](https://github.com/VeronicaLourens/vero-perfume/issues/15) View the total product in the shopping cart  |
    |:-------:|:--------|
    | &check; | User is able to view the total product in the shopping cart. |

    | User Story |[#16](https://github.com/VeronicaLourens/vero-perfume/issues/16) View policy documents  |
    |:-------:|:--------|
    | &check; | User is able to view the site's policy documents with terms and conditions. |

    | User Story |[#17](https://github.com/VeronicaLourens/vero-perfume/issues/17) Update quantity in the shopping cart  |
    |:-------:|:--------|
    | &check; | User is able to update quantity in the shopping cart. |

[Back to top](#vero-perfume)

* #### Epic 5 - Profiles app

    | User Story |[#13](https://github.com/VeronicaLourens/vero-perfume/issues/13) Add / delete product to wishlist   |
    |:-------:|:--------|
    | &check; | User is able to add / delete product to wishlist. |

    | User Story |[#19](https://github.com/VeronicaLourens/vero-perfume/issues/19) Register an account  |
    |:-------:|:--------|
    | &check; | User is able to register an account via the sign up form. |

    | User Story |[#20](https://github.com/VeronicaLourens/vero-perfume/issues/20) Login / log out  |
    |:-------:|:--------|
    | &check; | User is able to login / log out to the account and receiving feedback messages. |

    | User Story |[#21](https://github.com/VeronicaLourens/vero-perfume/issues/21) Edit / delete account profile  |
    |:-------:|:--------|
    | &check; | User is able to edit / delete account profile. |

    | User Story |[#22](https://github.com/VeronicaLourens/vero-perfume/issues/22) Verify email address  |
    |:-------:|:--------|
    | &check; | User is albe to verify email address when signing up an account. |

    | User Story |[#23](https://github.com/VeronicaLourens/vero-perfume/issues/23) Receive feedback  |
    |:-------:|:--------|
    | &check; | User is able to verify the activities on the site with the feedback messages. |

    | User Story |[#24](https://github.com/VeronicaLourens/vero-perfume/issues/24) Reset account password  |
    |:-------:|:--------|
    | &check; | User is able to reset the account passwork. |

    | User Story |[#25](https://github.com/VeronicaLourens/vero-perfume/issues/25) Subscribe newsletter  |
    |:-------:|:--------|
    | &check; | User is able to fill in the email address to subscribe the newsletter. |

    | User Story |[#26](https://github.com/VeronicaLourens/vero-perfume/issues/26) Unsubscribe newsletter  |
    |:-------:|:--------|
    |   | ```This is yet to implement in the future development```. |

    | User Story |[#27](https://github.com/VeronicaLourens/vero-perfume/issues/27) View purchase history  |
    |:-------:|:--------|
    | &check; | User is able to view the purchse history in the profile page. |

[Back to top](#testing)

* #### Epic 6 - Checkout app

    | User Story |[#28](https://github.com/VeronicaLourens/vero-perfume/issues/28)  Checkout and pay  |
    |:-------:|:--------|
    | &check; | User is able to checkout and pay while completing the online orders. |

    | User Story |[#29](https://github.com/VeronicaLourens/vero-perfume/issues/29) Receive order confirmation   |
    |:-------:|:--------|
    | &check; | User is able to receive order confirmation on both the Bootstrap toasts message and email confirmation . |

    | User Story |[#34](https://github.com/VeronicaLourens/vero-perfume/issues/34)  Process online orders  |
    |:-------:|:--------|
    | &check; | User is able to process the online orders easily with the order form and Stripe payment system implemented on the site. |


[Back to top](#testing)

## Automated Testing

I have conducted and ran 11 automated testing for the project with the OK result. In my Gitpod workspace using command ```python manage.py test```.

![Automated testing](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/auto-test.png)

[Back to top](#testing)

## Unsolved Known Bugs

* #### Product price

    The product prices are displayed dynamically based on the sizes selected when adding product into the cart. However, the prices are not correct on the cart page and on the checkout page. I tried a couple of different ways to solve the problem but I couldn't make it work due to current knowledge and the time strain. 

    ![Product price](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/price-bug.png)

[Back to top](#testing)

* #### Wishlist count

    The total count on the wishlist page doesn't work. I tried the same way of doing the shopping cart count but it didn't work out as expected.

* #### Product forms validations

    The add / edit product forms for store owners to add or edit product are not validated.

* #### Lighthouse performance bugs

    The issues of Lighhouse testing performance were not solved.

    ![Lighthouse performace issues](https://github.com/VeronicaLourens/vero-perfume/blob/main/media/lighthouse-error.png)

[Back to top](#testing)

### Resolved Bugs

* #### Product size

    The product sizes were displayed when adding product to the shopping cart and the sizes were also displayed on the cart page in the first place. However, it doesn't work anymore after reset the project's entire database on the very last stage of the project develoment due to some adjustment. 
    
    The issues were resolved again in the end when set the product size default to True and manually set the has_size file to YES in the database.

* #### BadHeaderError

    In ```checkout``` app's confirmation_email foler, deleted the empty line in the confirmation_email_subject.txt file.

[Back to top](#testing)

* #### Product admin forms

    The add & edit product forms were opening a file when clicking every form fileds. To solve the problem, set the file positon to relative in ```base.css``` file.

* #### Full name form field validation

    Add ```Regexvalidators``` in the profile model to solve the form input problems.

* #### Webhooks bug

    Set the port 8000 to public to make the checkout process smooth with ```Stripe```.

    
* #### W3C HTML validation errors and warnings

    To correct the errors and get rid of the warnings, I deleted the duplicated ids, hrefs, script type attribute and the spaces between the names of brands. 

   ![W3C HTML errors](https://veroperfume.s3.eu-west-2.amazonaws.com/media/readme-pics/w3c-html.png)

    
[Back to top](#testing)


[Back to README.md](README.md)

