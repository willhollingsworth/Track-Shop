
### Standard Tables
##### Tracks

- Track ID (primary Key, auto increment)
- Artist
- Song Name
- Price
- Genre
- BPM
- Music Key
- Label

##### Users

- User ID (Primary Key, auto increment)
- Email
- Password ( store as hashed and salted)
- Is admin?
- Creation date (auto generate)

##### Carts

- Cart ID (Primary key, auto increment)
- Creation date (auto generate)
- User Id (Foreign key, unique as only one part per user allowed)

##### Orders

- Order Id (Primary key, auto increment)
- User Id (Foreign key)
- Order Date (auto generate)
- Total amount
- Status(unpacked, packed, shipped, delivered)

### associate tables

##### Tracks In Carts

Many to many link between Tracks to Carts

- Cart ID (Foreign Key)
- Track ID (Foreign Key)
- Cart Track id(Primary key, composite of Cart ID and Track ID)
- Quantity


##### Tracks in Orders

Many to many link between tracks to Orders

- Order Id (Foreign key)
- Track ID (Foreign Key)
- Order Track id(Primary key, composite of Order ID and Track ID)
- Price at purchase (snapshot of current price, in case of price change)
- Quantity
