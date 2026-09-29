# Movie-Ticket-Booking-System
A Movie Ticket Booking System that allows you to select movies, book seats, order snacks and generates your total bill

## Overview
The Movie Ticket Booking System is a Python-based console application that allows a user to select a movie, view the ticket price and seat arrangement, book available seats, and optionally order snacks. The program calculates the movie ticket cost, snack cost, and final bill.

The project is designed as a simple beginner-friendly booking system using Python lists, dictionaries, loops, conditional statements, functions, and user input.

## Features
- Displays a list of available movies.
- Shows the ticket price for each movie.
- Displays the theatre seat arrangement.
- Allows the user to select and book seats.
- Prevents a seat from being booked again during the current program run.
- Calculates the total ticket price.
- Provides an optional snack-ordering facility.
- Supports multiple snack items and quantities.
- Calculates the total snack price.
- Calculates and displays the final bill.

## Movies Available

| Movie | Ticket Price |
|---|---:|
| Avengers | ₹250 |
| Conjuring | ₹180 |
| Interstellar | ₹200 |
| The Lion King | ₹190 |
| The Jungle Book | ₹210 |

## Snacks Available

| Order ID | Snack | Price |
|---:|---|---:|
| 101 | Popcorn | ₹70 |
| 102 | French Fries | ₹60 |
| 103 | Chips | ₹50 |
| 104 | Cold Drink | ₹40 |
| 105 | Cookies | ₹55 |

## Technologies / Tools Used
- **Python 3**
- Python lists
- Python dictionaries
- Functions
- Loops
- Conditional statements
- Console input/output
- Git and GitHub for version control and submission

No external Python libraries are required

## Installation and Running

### 1. Install Python
Install Python 3.x on your computer.

### 2. Download or clone the repository
Clone the GitHub repository or download the project files.

### 3. Open a terminal in the project folder

### 4. Run the program

```bash
python Moviebookingvityarthi.py
```
## How to Use

1. Run the Python program.
2. Select one of the available movies.
3. Check the ticket price and seat arrangement.
4. Enter the number of tickets required.
5. Enter the seat IDs you want to book, such as `A1`, `B4`, or `H10`.
6. The program displays the total ticket price.
7. Choose whether you want to order snacks.
8. If snacks are selected, enter the snack order ID and quantity.
9. The program displays the snack total and final bill.

## Testing Instructions

The following cases can be used to test the program:

| Test Case | Input / Action | Expected Result |
|---|---|---|
| 1 | Select `Avengers` | Ticket price ₹250 is displayed |
| 2 | Book a valid seat such as `A1` | Seat is booked |
| 3 | Try booking the same seat again | Seat is reported as unavailable |
| 4 | Select an invalid movie | Movie unavailable message is displayed |
| 5 | Order popcorn, quantity 2 | Snack cost becomes ₹140 |
| 6 | Order multiple snack items | Snack total is calculated correctly |
| 7 | Choose `N` for snacks | Final bill equals ticket total |

## Screenshots
<img width="1920" height="1080" alt="Screenshot (89)" src="https://github.com/user-attachments/assets/4226ee10-82df-433f-82ec-911c992f03b7" />
<img width="1920" height="1080" alt="Screenshot (90)" src="https://github.com/user-attachments/assets/67f38561-d692-438b-9ff1-45dbd09cfeee" />
<img width="1920" height="1080" alt="Screenshot (91)" src="https://github.com/user-attachments/assets/d613e031-c944-4ba3-9818-8d85732faa22" />



