# Interactive Tech Repair Shop System

## Overview

This project is a terminal-based Tech Repair Shop management system built with Python using Object-Oriented Programming concepts.

The system allows users to:

* View available repair services
* Add repair services to an invoice
* View the current invoice
* Print the final bill
* Exit the program

The project was created mainly to practice OOP concepts in Python in a practical way.

---

# Features

* Abstract base class for repair services
* Inheritance between parent and child classes
* Encapsulation using private attributes and properties
* Polymorphism for different cost calculations
* Customer invoice system
* Interactive terminal menu
* Input validation
* Beginner-friendly structure

---

# OOP Concepts Used

## 1. Abstraction

The project uses an abstract parent class called `RepairService`.

This class defines common methods and attributes that every repair service must have.

It also contains abstract methods that child classes must implement.

---

## 2. Inheritance

Two child classes inherit from `RepairService`:

* `HardwareRepair`
* `SoftwareRepair`

This allows code reuse and cleaner organization.

---

## 3. Encapsulation

Important data such as labor cost and status are protected using:

* private attributes
* properties
* setters

Validation is used to prevent invalid values.

---

## 4. Polymorphism

Different repair classes calculate their costs differently.

The invoice system calls the same methods on all repair objects without needing to know their exact type.

---

# Project Structure

```text
RepairService (Abstract Parent Class)
│
├── HardwareRepair
│
└── SoftwareRepair

CustomerInvoice
```

---

# Classes

## RepairService

Parent abstract class for all repair services.

Contains:

* service id
* service name
* labor cost
* repair status

Abstract methods:

* `calculate_service_cost()`
* `display_service_info()`

---

## HardwareRepair

Handles hardware-related repairs such as:

* Screen replacement
* Battery replacement
* Motherboard repair

Extra attributes:

* parts cost
* warranty months

Cost calculation:

```text
labor cost + parts cost + tax
```

---

## SoftwareRepair

Handles software-related repairs such as:

* OS installation
* Virus removal
* Driver updates

Extra attributes:

* license key
* operating system version

Cost calculation:

```text
labor cost + digital fee
```

---

## CustomerInvoice

Stores repairs selected by the customer.

Functions:

* add repairs
* view invoice
* print final bill

---

# How the Program Works

1. The program starts and asks the user for their name.
2. A main menu is displayed.
3. The user can:

   * view services
   * add services
   * view invoice
   * print final bill
4. The program continues running until the user exits.

---

# Example Menu

```text
1. View Services
2. Add Service
3. View Invoice
4. Print Final Bill
5. Exit
```

---

# Example Available Services

```text
HW01 --> Screen Replacement
HW02 --> Battery Replacement
HW03 --> Motherboard Repair
SW01 --> OS Reinstallation
SW02 --> Virus Removal
```

---

# Example Final Bill

```text
===== FINAL BILL =====
Customer: Ahmed

Screen Replacement --> $128.0
Virus Removal --> $35

TOTAL = $163.0
```

---

# Technologies Used

* Python
* Object-Oriented Programming (OOP)
* Abstract Base Classes (`abc` module)

---

# Future Improvements

Possible future features:

* Save invoices to files
* Add customer database
* GUI version using Tkinter or PyQt
* Database integration
* Employee management system
* Search and remove services
* Better error handling

---

# How to Run

1. Make sure Python is installed.
2. Open the project folder.
3. Run the file:

```bash
python main.py
```




video link : https://drive.google.com/drive/folders/1j4Pd8Rd93cFl0UkAVnQ1JDonkkjDEeab?usp=drive_link 
