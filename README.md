# Train Ticket Reservation Management System

This application is a train ticket reservation management system created using Django and Django Rest Framework. With this application, administrators can manage, reserve, and cancel train tickets, and users can reserve their tickets.

## Features

- User registration and management
- Station registration and management
- Train registration and management
- Schedule registration and management
- Ticket reservation and cancellation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/NavidAhmadiii/TrainTicketReservationsSystem.git
```


3. Install dependencies:
```bash
pip install -r requirements.txt
```


4. Run migrations:
```bash
python manage.py migrate
```

5. Run the server:
```bash
python manage.py runserver
```

The application should now be accessible. You can visit `http://localhost:8000` in your browser.

## Usage

1. User Account Creation:
   - Create a user account using the registration form in the application.
   - Administrators can also create user accounts from the admin dashboard.

2. Station Management:
   - As an administrator, navigate to the station management section and add, edit, or delete stations.

3. Train Registration:
   - As an administrator, navigate to the train management section and register new trains.

4. Schedule Planning:
   - Register schedules for each train and station.

5. Ticket Reservation:
   - Users can reserve their tickets by entering the required details.

6. Reservation Management:
   - As an administrator, manage user reservations, approve, or cancel them.

## Contribution
If you would like to contribute to improving and expanding this application, please send your feedback or submit a pull request.

## License
This project is licensed under the terms of the [MIT license](LICENSE).

## Admin Panel
You can access the admin panel using the following credentials:
- Username: admin
- Password: admin


