# Bookstore_Python_CRUD

**DataMed: Python CRUD Application for Customer in the Bookstore**

A comprehensive Python application to guide customers in the Bookstore to purchase items. This program implements Create, Read, Update, and Delete (CRUD) operations.

# Business Understanding
This project refers to the mini bookstore, specifically addressing they the customer know how to buy in their place efficiently. 

**Benefits:**

* Improved data accuracy and consistency
* Efficient data log and history recorder

# Target Users:

This application is designed for customer who come to the bookstore, but did not want to surrounding the bookstore room and just search in the corner computer that provide by the Nah! Bookstore.

# Features
* **Create:**
    * Allows users to add new items from the bookstore's inventory to their shopping cart.,
* **Read:**
    * Displays detailed information for each item, categorized by type (books, accessories, bags, pencils,
    * Includes the capability to handle large product lists through pagination (breaking a large list into smaller pages) and sorting (arranging items by price, name, or other criteria.
* **Update:**
    * Enables users to modify their existing shopping cart data. This could include changing the quantity of an item, selecting different product options.
    * Provides clear confirmation messages when an update is successful (e.g., "Quantity updated") and informative error messages if it fails (e.g., "Item out of stock").
* **Delete:**
    * Permits users to remove items from their shopping cart before completing a purchase
      
## Installation

 **Prerequisites:**
Python (version 3.13.5)

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Adds a new shopping cart to the database,
    * **Read:** SDisplays detailed information for each item,
    * **Update:** Modify shopping chart details, such as updating their needs come from bookstore.
    * **Delete:** Remove a book at shopping cart.

## Data Model
This project utilizes a manual input data and some auto-generated data to represent chart bookstore customer data need. The following fields are typically stored:
1. store_inventory Data Model
| Field             | Type       | Description                                                                                               |
| ----------------- | ---------- | --------------------------------------------------------------------------------------------------------- |
| item_name         | str        | The name of the item (e.g., book title or accessory name). Primary key.                                   |
| category          | str, alpha | The category of the item (e.g., International Novel, Accessories, etc.).                                  |
| price             | int        | The price of the item in Indonesian Rupiah (IDR)                                                          |
| stock             | int        | The available stock quantity of the item                                                                  |
Notes:

1. The item_name (key of the store_inventory dictionary) serves as the unique identifier (primary key).
2. Example entry: 'A Curtain Twitcher\'s Book of Murder': {'Category': 'International Novel', 'price': 103500, 'stock': 10}.

2. keranjang (Cart) Data Model
| Field             | Type       | Description                                                                                               |
| ----------------- | ---------- | --------------------------------------------------------------------------------------------------------- |
| No                | int        | The item number from store_inventory (used for selection).                                                |
| Nama              | str        | The name of the item (references item_name in store_inventory).                                           |
| Jumlah            | int        | The quantity of the item selected by the customer.                                                        |
| Harga             | int        | The unit price of the item (copied from store_inventory['price'])                                         |           

Notes:

1. The keranjang is a list of dictionaries, where each dictionary represents an item in the cart.
Example entry: {'No': 1, 'Nama': 'A Curtain Twitcher\'s Book of Murder', 'Jumlah': 2, 'Harga': 103500}.
2. There is no explicit primary key, as items in the cart are temporary and identified by their index in the list during operations like ubah_atau_hapus_keranjang.|

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to bachtiarmardiansyah@gmail.com or submit an issue if you encounter any problems or have suggestions for improvements.
