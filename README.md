# Site Overview
VL Perfume is an e-commerce online shop where sells fine fragrance and perfumes. The site provides a smooth online shopping experience to customers. The site processes online orders, online secured payment method and fast delivery service. The site is accessible across all the devices using different browsers. The site sends out marketing newsletters directly to customers and has a Facebook page to promote the selling business.

# UX
## Agile Project Management
I used GitHub Agile project management tool to create user stories using issues and planned the user stories into three different stages using Kanban board with three columns that are ```To do```, ```In progress``` and ```Done```. The user stories are labeled with **MoSCoW** techniques to prioritize the project’s tasks.

### Epics & User Stories

* #### Epic 1 - Site Admin 
|  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
| --------------- | -------------- | --------- | --------| -------------|
| [#1](https://github.com/VeronicaLourens/vl-perfume/issues/1) Admin CRUD | As a shop owner  | I want to navigate the admin panel so that I can create, read, update and delete data on the site. | Django admin | Must Have |
| [#2](https://github.com/VeronicaLourens/vl-perfume/issues/2) Admin add / delete product | As a shop owner  | I want to add or delete product so that I can easily add new product or delete unavailable product on the site.| Django admin | Must Have |
| [#3](https://github.com/VeronicaLourens/vl-perfume/issues/3) Admin edit product | As a shop owner  |  I want to edit the product so that I can update the product information.| Django admin | Must Have |
| [#4](https://github.com/VeronicaLourens/vl-perfume/issues/4)  Admin manage reviews | As a shop owner  |  I want to manage the customer review so that I can filter out and approve the reviews that user wants to post on the site.| Django admin | Must Have |
| [#5](https://github.com/VeronicaLourens/vl-perfume/issues/5)  Admin receive payment| As a shop owner  |  I want to receive payment from customers so that I can enjoy doing business.| Django admin | Must Have |
| [#6](https://github.com/VeronicaLourens/vl-perfume/issues/6)  Send newsletter| As a shop owner  |  I want to send the newsletters out so that I can promote the products to customer with updates for more business.| Django admin | Should Have |

* #### Epic 2 - Home app
|  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
| --------------- | -------------- | --------- | --------| -------------|
| [#7](https://github.com/VeronicaLourens/vl-perfume/issues/7)  Navigate the site| As a shopper  |   I want to navigate the site easily so that I know what products the site sells to see if I am interested or not.| home | Must Have |
| [#8](https://github.com/VeronicaLourens/vl-perfume/issues/8) Access the site | As a shopper  | I want to access the site easily so that I can view the site on any media screens using different browsers.| home | Must Have |
| [#18](https://github.com/VeronicaLourens/vl-perfume/issues/18) View messages | As a shopper  |  I want to view messages so that I know my activities when updating my shopping cart or make a payment. | home | Should Have |
| [#31](https://github.com/VeronicaLourens/vl-perfume/issues/31)  | As a shopper  |  I want to access the shop's social media platform so that I can follow the shop and get updates instantly. | home | Could Have |
| [#32](https://github.com/VeronicaLourens/vl-perfume/issues/32) Contact site owner | As a registered shopper  | I want to make contact to the site owner so that I can contact the owner for any questions.  | home | Should Have |
| [#33](https://github.com/VeronicaLourens/vl-perfume/issues/33) Advertise shop / product | As a shop owner  | I want to advertise my shop and product so that I can have more customers to buy my products.  | home | Could Have |

* #### Epic 3 - Products app
|  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
| --------------- | -------------- | --------- | --------| -------------|
| [#9](https://github.com/VeronicaLourens/vl-perfume/issues/9)  View product list| As a shopper  |  I want to view the list of products so that I know what product the site sells. | product | Must Have |
| [#10](https://github.com/VeronicaLourens/vl-perfume/issues/10) View product details | As a shopper  |  I want to view the product details so that I can have enough information about the individual product before I purchase. | home | Must Have |
| [#11](https://github.com/VeronicaLourens/vl-perfume/issues/11)  Filter and view search product result| As a shopper  |  I want to filter products so that I can quickly find the products I am looking for. | products | Should Have |
| [#12](https://github.com/VeronicaLourens/vl-perfume/issues/12) Sort products by a specific category  | As a shopper  |  I want to find the best priced or best rated product in a specific category so that I can easily find what I want. | products | Should Have |
| [#13](https://github.com/VeronicaLourens/vl-perfume/issues/13) Save product to wishlist | As a shopper  |  I want to save product to my wish list so that I can easily select the products to purchase. | products | Should Have |

* #### Epic 4 - Cart app
|  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
| --------------- | -------------- | --------- | --------| -------------|
| [#14](https://github.com/VeronicaLourens/vl-perfume/issues/14)  Add / delete product in the shopping cart| As a shopper  |  I want to add or delete products from the shopping cart so that I know what products and the amount of products I would buy. | cart | Must Have |
| [#15](https://github.com/VeronicaLourens/vl-perfume/issues/15) View the total product in the shopping cart | As a shopper  |  I want to view the products in my shopping cart so that I know what I buy and the total cost for the products. | cart | Should Have |
| [#16](https://github.com/VeronicaLourens/vl-perfume/issues/16)  View policy documents| As a shopper  | I want to view the site's documents so that I know the site's terms and conditions when purchasing the product.  | home | Should Have |
| [#17](https://github.com/VeronicaLourens/vl-perfume/issues/17) Update quantity in the shopping cart | As a shopper  | I want to update the product quantity in my shopping cart so that I can easily add or delete the same product in my shopping cart.  | cart | Should Have |


* #### Epic 5 - Users app
|  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
| --------------- | -------------- | --------- | --------| -------------|
| [#19](https://github.com/VeronicaLourens/vl-perfume/issues/19)  Register an account| As a shopper  | I want to register an account so that I can manage my activities on the site.  | users | Must Have |
| [#20](https://github.com/VeronicaLourens/vl-perfume/issues/20) Login / log out | As a registered shopper  |   I want to login and logout so that I can access my account and manage my purchase on the site. | users | Must Have |
| [#21](https://github.com/VeronicaLourens/vl-perfume/issues/21)  | As a registered shopper  | I want to edit or delete account so that I can personalize my own account profile or delete my account as I wish.  | users | Must Have |
| [#22](https://github.com/VeronicaLourens/vl-perfume/issues/22) Verify email address | As a  registered shopper  | I want to verify my email address so that I can be sure the security of my account and purchase on the site.  | users | Must Have |
| [#23](https://github.com/VeronicaLourens/vl-perfume/issues/23) Receive feedback | As a  registered shopper  |  I want to receive feedback so that I can verify my activities on the site. | users | Should Have |
| [#24](https://github.com/VeronicaLourens/vl-perfume/issues/24) Reset account password | As a  registered shopper  | I want to reset my account password so that I can be sure that I can access my account again in case I forgot the password.  | users | Should Have |
| [#25](https://github.com/VeronicaLourens/vl-perfume/issues/25) Subscribe newsletter | As a  registered shopper  |   I want to receive newsletters so that I receive regular updates about the products. | home | Could Have |
| [#26](https://github.com/VeronicaLourens/vl-perfume/issues/26) Unsubscribe newsletter  | As a  registered shopper  | I want to unsubscribe newsletters so that I can no longer receiving regular newsletters.  | home | Could Have |
| [#27](https://github.com/VeronicaLourens/vl-perfume/issues/27) View purchase history | As a shopper  | I want to view my purchase history so that I can see what I have bought in the past.  | users | Should Have |


* #### Epic 6 - Checkout app
|  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
| --------------- | -------------- | --------- | --------| -------------|
| [#28](https://github.com/VeronicaLourens/vl-perfume/issues/28) Checkout and pay  | As a registered shopper  | I want to check out and pay online so that I can complete the purchase.  | checkout | Must Have |
| [#29](https://github.com/VeronicaLourens/vl-perfume/issues/29) Receive order confirmation | As a registered shopper  |   I want to receive confirmation after paying so that I know whether my purchase is successful or not. | checkout | Must Have |
| [#34](https://github.com/VeronicaLourens/vl-perfume/issues/34)  | As a shop owner | I want to process orders online so that I can sell products online  | checkout | Must Have |

* #### Epic 7 - Review app
|  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
| --------------- | -------------- | --------- | --------| -------------|
| [#30](https://github.com/VeronicaLourens/vl-perfume/issues/30)  | As a registered shopper  | I want to post review or rate a product / shop so that I can share my opinion to the others.  | review | Could Have |



## Wireframes
I used ```Balsamiq``` to create basic site structure to visualize the site’s potential features which helps me to understand better what needs to be done for the project. The end result might slightly different due to the project development.

* ### Desktop
* ### Mobile
## Design Choice
The site uses white background with high quality colorful images in a carousel sideshow for the landing page. The site is intuitive with great color contrast which is very user friendly. The project is designed for potentially being used in a real e-commerce online web shop that can be used for both the shopper and the site owner. The application was created using Django MVC structure.

### Color Scheme
### Database ERD
#### Models
### Business Model
# Exisiting Features
# Technologies Used
## Languages
## Frameworks
## Programs
# Testing
# Deployment
# Clone Project
# Credit
## Content
## Media
## Code
# Acknowledgement