```mermaid
erDiagram
    Order
    User
    Cart
    Track
    User ||--|{ Order : Places
    Order }|--o{ Track : Contains
    User ||--|{ Cart : Has
    Cart }|--o{ Track : Contains
```


