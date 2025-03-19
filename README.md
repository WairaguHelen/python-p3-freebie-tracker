# Freebie Tracker

## Overview
Freebie Tracker is a Python application that allows developers to keep track of all the freebies they collect from various companies. This project uses SQLAlchemy to manage database relationships and CRUD operations.

## Learning Goals
- Write SQLAlchemy migrations.
- Establish relationships between tables using SQLAlchemy.
- Perform CRUD operations using SQLAlchemy.

## Technologies Used
- Python
- SQLAlchemy
- SQLite

## Domain Model
The application consists of three models:
- `Company`: Represents a company that distributes freebies.
- `Dev`: Represents a developer who collects freebies.
- `Freebie`: Represents an item given by a company to a developer.

### Relationships
- A `Company` has many `Freebie`s.
- A `Dev` has many `Freebie`s.
- A `Freebie` belongs to a `Dev` and a `Company`.
- `Company` and `Dev` have a many-to-many relationship through `Freebie`.

## Database Schema
### Companies Table
| Column        | Type    |
|--------------|--------|
| id           | Integer (Primary Key) |
| name         | String  |
| founding_year | Integer |

### Devs Table
| Column | Type   |
|--------|--------|
| id     | Integer (Primary Key) |
| name   | String |

### Freebies Table
| Column     | Type   |
|------------|--------|
| id         | Integer (Primary Key) |
| item_name  | String  |
| value      | Integer |
| company_id | Integer (Foreign Key) |
| dev_id     | Integer (Foreign Key) |

## Setup and Installation
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd freebie-tracker
   ```
2. Install dependencies:
   ```sh
   pipenv install
   pipenv shell
   ```
3. Run migrations:
   ```sh
   alembic upgrade head
   ```
4. Seed the database:
   ```sh
   python lib/seed.py
   ```
5. Start an interactive session:
   ```sh
   python debug.py
   ```

## Features and Methods
### Freebie
- `freebie.dev`: Returns the `Dev` instance for this Freebie.
- `freebie.company`: Returns the `Company` instance for this Freebie.
- `freebie.print_details()`: Returns a string formatted as `{dev_name} owns a {freebie_item} from {company_name}`.

### Company
- `company.freebies`: Returns all freebies for the company.
- `company.devs`: Returns all devs who received freebies from the company.
- `company.give_freebie(dev, item_name, value)`: Creates a new `Freebie` associated with the company and the given dev.
- `Company.oldest_company()`: Returns the `Company` instance with the earliest founding year.

### Dev
- `dev.freebies`: Returns all freebies that the dev has collected.
- `dev.companies`: Returns all companies from which the dev has received freebies.
- `dev.received_one(item_name)`: Returns `True` if the dev has received a freebie with the specified `item_name`, otherwise `False`.
- `dev.give_away(dev, freebie)`: Transfers ownership of a freebie to another dev, if the dev owns the freebie.

## Testing
To test the functionality, run `python debug.py` and manually query the database to check relationships and methods.

## Contributing
Feel free to fork the repository and submit pull requests for improvements.

## License
This project is licensed under the MIT License.
