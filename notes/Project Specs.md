## Description of the site:

- Site Name: **Track Shop**
- Brief description: **A Electronic music song store similar to sites like apple music but specializing in electronic music. Each song will have additional attributes like Genre, BPM and Music Key. Data will be populated from [Beatport.com top 100](https://www.beatport.com/top-100)**

## Client-side functionality :

- Search Bar dynamically populates results as user types
- User cart Management:
    - Initially loads from Carts DB Table
    - Allow dynamic adding and removing of entries without page refresh
    - Upon change updates associated DB Carts entries

## Server-side functionalities

#### Database interactions 

Run the following DB queries
##### Tracks

- List all
- List of a certain genre
- List matches to a given string (will be used for dynamic search bar functionality)

##### Users

- Register
- Login
- Add song to cart
- View items in cart
- Remove song from cart
- Checkout (convert cart into an order)

#### Admin Management

- View all users
- View orders (completed carts)

## Tech stack:

- Web Backend - **Fast api**
- Database server - **PostgreSQL**
- DB ORM - **SQL Model**
- Languages - **Python for the backend, JavaScript for the frontend**
- Security requirements - **User authentication and User Input Sanitization**

#### Further Tech Stack
- PyTest for Testing