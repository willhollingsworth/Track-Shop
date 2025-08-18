```mermaid
erDiagram
    Order
    User
    Cart
    Track
    User ||--o{ Order : Places
    Order }|--|{ Track : Contains
    User ||--o{ Cart : Has
    Cart }|--|{ Track : Contains
```


