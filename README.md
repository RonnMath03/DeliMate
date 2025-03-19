# DeliMate - Delivery Management System 
![DeliMate Logo](Documentation/DeliMate%20logo.png)

My class 12 python project

## Overview

DeliMate is a comprehensive delivery management system developed as my first coding project for my Class 12 final assignment. The application provides a simple yet effective solution for managing delivery orders, tracking their status, and maintaining customer information.

## Features

- **Order Management**: Create, modify, and delete delivery orders
- **Search Functionality**: Find orders by various parameters including:
  - Order number
  - Customer name
  - Phone number
  - Delivery date
  - Pincode (area/locality)
- **Status Tracking**: Update and monitor order status through the delivery lifecycle:
  - Ordered
  - Dispatched
  - In Transit
  - Out for Delivery
  - Delivered
- **Data Persistence**: All order data is stored securely in a local database file
- **Command-Line Interface**: Easy-to-navigate menu system

## Technical Details

- **Language**: Python
- **Data Storage**: Binary file using Python's pickle module
- **Input Validation**: Ensures phone numbers, pincodes, and other data are entered correctly
- **Date Management**: Automatic calculation of delivery dates based on order date

## Getting Started

1. Ensure you have Python installed on your system
2. Clone this repository or download the code files
3. Navigate to the [`Code`](Code) directory
4. Run the program:
   ```
   python DeliMate_Complete.py
   ```

## Usage Guide

The main menu provides the following options:

1. **Add a New Order**: Enter customer details, with automatic order number generation and delivery date calculation
2. **Search Receiver Details**: Find orders using various search parameters
3. **Display All Existing Orders**: View all orders in the system
4. **Modify Order Details**: Update customer information for existing orders
5. **Modify Order Status**: Update the delivery status of orders
6. **Delete an Order**: Remove orders from the system
7. **Exit**: Close the application

## Project Structure

```
DeliMate/
├── Code/
│   ├── DeliMate_Complete.py  # Main application file
│   └── dmdb.dat              # Database file
└── Documentation/
    ├── DeliMate logo.jpeg    # Project logo
    └── Documentation.pdf     # Detailed documentation
```

## Learning Outcomes

This project was my first programming venture and helped me learn:
- Python programming fundamentals
- File handling and data persistence
- Input validation techniques
- Command-line interface design
- Basic data management operations (CRUD)
- Function organization and modularization

## Future Improvements

As this was my first coding project, there are several areas for potential enhancement:
- Graphical user interface
- Database migration to SQL
- Data export capabilities
- Multiple user support
- Web or mobile interface

---

*DeliMate - Simplifying Delivery Management*
