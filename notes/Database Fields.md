
## Database Fields
### Standard Tables
##### Tracks

- track_id: int (Primary Key, auto increment)
- artist: str
- title: str
- price: float
- genre: str
- bpm: int
- music_key: str
- label: str

##### Users

- user_id: int (Primary Key, auto increment)
- email: str (unique, indexed)
- password: str
- phone: str
- first_name: str
- last_name: str
- creation_date: datetime (auto generate)
- admin: bool (default False)

##### Orders

- order_id: int (Primary Key, auto increment)
- user_id: int (Foreign Key to User.user_id)
- created_at: datetime (auto generate)
- updated_at: datetime (auto generate)
- subtotal: float
- tax: float
- total: float

### Associative Tables

##### OrderTrack (Many-to-many link between Orders and Tracks)

- order_track_id: int (Primary Key, auto increment)
- order_id: int (Foreign Key to Order.order_id)
- track_id: int (Foreign Key to Track.track_id)
- price_at_purchase: float (snapshot of track price at time of order)
