# Purchase-Requisition-System

A Software Engineering project to manage purchase requisitions inside a company (from creating PR, until the generation of a PO). The system involves five actors: Employee, Manager, Vendor, Purchaser, and Finance Officer. 

## Roles/Features (Not Detailed)

- Employee: Submits Purchase Requisitions, views and manages them. 
- Manager: Reviews the PRs, manages the approval of them and add Remarks. 
- Vendor: Submits quotations, views and manages them. 
- Purchaser: Reviews the Quotations, manages the approval of them and add Remarks.
- Finance Officer: Creates Purchase Orders and manages them. 


# Getting Started

## Installation

- Clone the repository
- Set up a virtual environment:
  - Install virtualenv if you don't already have it: `pip install virtualenv`
  - Create a virtual environment: `virtualenv env`
  - Activate the virtual environment:
    - On Windows: `env\Scripts\activate`
    - On macOS/Linux: `source env/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Run migrations: `python manage.py migrate`
- Start the development server: `python manage.py runserver`

## Usage

- Create a superuser account: `python manage.py createsuperuser`
- Access the admin site and create user accounts with different roles: `http://localhost:8000/admin/`
- Log in with the created accounts and test the features of the system
