```mermaid
erDiagram
    Order
    User
    Track
    OrderTrack
    User ||--|{ Order : Places
    Order ||--|{ OrderTrack : Has
    OrderTrack }|--|| Track : References
```
