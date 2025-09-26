# Bookstore_Python_CRUD

**DataMed: Python CRUD Application for Customers in "Nah! Bookstore"**

A comprehensive Python application to guide customers in purchasing items from the bookstore. This program implements Create, Read, Update, and Delete (CRUD) operations for managing a shopping cart.

## Business Understanding

This project focuses on a mini bookstore, helping customers efficiently browse and purchase items without physically wandering the store.

### Benefits
- Improved data accuracy and consistency.
- Efficient logging and history recording for purchases.

## Target Users

This application is designed for customers visiting the bookstore who prefer to search and shop using a provided corner computer, rather than browsing the physical shelves.

## Features

- **Create:**
  - Allows users to add new items from the bookstore's inventory to their shopping cart.
- **Read:**
  - Displays detailed information for each item, categorized by type (e.g., books, accessories, bags, pencils).
  - Handles large product lists through pagination (breaking lists into smaller pages) and sorting (by price, name, or other criteria).
- **Update:**
  - Enables users to modify items in their shopping cart, such as changing quantities or selecting different options.
  - Provides confirmation messages for successful updates (e.g., "Quantity updated") and error messages for failures (e.g., "Item out of stock").
- **Delete:**
  - Permits users to remove items from their shopping cart before completing a purchase.

## Installation

### Prerequisites
- Python (version 3.13.5 or compatible).

## Usage

1. **Run the Application:**
   ```bash
   python main.py
   ```

2. **CRUD Operations:**
   - **Create:** Add a new item to the shopping cart in the database.
   - **Read:** Display detailed information for each item.
   - **Update:** Modify shopping cart details, such as updating quantities based on customer needs.
   - **Delete:** Remove an item from the shopping cart.

## Data Model

This project uses manually input data and some auto-generated data to represent the bookstore's inventory and customer shopping cart. The following models are used:

### 1. Store Inventory Data Model

The `store_inventory` is a dictionary where the key is the `item_name`.

| Field     | Type       | Description                                                              |
| --------- | ---------- | ------------------------------------------------------------------------ |
| item_name | str        | The name of the item (e.g., book title or accessory name). Primary key.  |
| category  | str, alpha | The category of the item (e.g., International Novel, Accessories, etc.). |
| price     | int        | The price of the item in Indonesian Rupiah (IDR).                        |
| stock     | int        | The available stock quantity of the item.                                |

#### Notes
- The `item_name` (key of the `store_inventory` dictionary) serves as the unique identifier (primary key).
- Example entry: `'A Curtain Twitcher\'s Book of Murder': {'Category': 'International Novel', 'price': 103500, 'stock': 10}`.

### 2. Keranjang (Cart) Data Model

The `keranjang` is a list of dictionaries, where each dictionary represents an item in the cart.

| Field     | Type       | Description                                                              |
| --------- | ---------- | ------------------------------------------------------------------------ |
| No        | int        | The item number from `store_inventory` (used for selection).             |
| Nama      | str        | The name of the item (references `item_name` in `store_inventory`).      |
| Jumlah    | int        | The quantity of the item selected by the customer.                       |
| Harga     | int        | The unit price of the item (copied from `store_inventory['price']`).     |

#### Notes
- There is no explicit primary key, as items in the cart are temporary and identified by their index in the list during operations like `ubah_atau_hapus_keranjang`.
- Example entry: `{'No': 1, 'Nama': 'A Curtain Twitcher\'s Book of Murder', 'Jumlah': 2, 'Harga': 103500}`.

## Contributing

We welcome contributions to this project! Please feel free to open a pull request, email suggestions to bachtiarmardiansyah@gmail.com, or submit an issue if you encounter any problems or have ideas for improvements.
