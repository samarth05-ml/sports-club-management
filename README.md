# ⚽ Sports Club Management System

A backend web application built with **Flask** for managing sports clubs efficiently. The system provides role-based access control and allows administrators, coaches, players, and medical staff to manage teams, training sessions, matches, attendance, injuries, transfers, and player performance.

---

## 🚀 Features

### 🔐 Authentication & Authorization
- User Registration
- Secure Login & Logout
- Password hashing using Bcrypt
- Role-based access control
- Flask-Login session management

### 👥 Team Management
- Create teams
- Assign coaches to teams
- Assign players to teams
- View team information

### 🏃 Player Management
- Add players
- Update player details
- Delete players
- View player information
- Jersey number, position, height, weight, DOB management

### 🧑‍🏫 Coach Management
- Assign coaches to teams
- View coach profiles

### 📅 Training Management
- Schedule training sessions
- Update sessions
- Delete sessions
- View team-specific sessions

### ⚽ Match Management
- Schedule matches
- Update match details
- Record match scores
- Store winner information
- Delete matches

### 📊 Attendance Management
- Record attendance
- Track player participation
- View attendance history

### 🩺 Injury Management
- Record player injuries
- Update recovery status
- View injury history

### 📈 Player Performance
- Store player statistics
- Track performance over multiple matches

### 🔄 Player Transfers
- Transfer players between teams
- Maintain transfer history

---

# 🛠 Tech Stack

- Python
- Flask
- Flask SQLAlchemy
- Flask Migrate
- Flask Login
- Flask Bcrypt
- SQLite
- Jinja2
- HTML (Templates)

---

# 📁 Project Structure

```
sports-club-management/

│
├── app/
│   ├── auth/
│   ├── attendance/
│   ├── coach/
│   ├── injury/
│   ├── match/
│   ├── performance/
│   ├── player/
│   ├── statistics/
│   ├── team/
│   ├── training/
│   ├── transfer/
│   ├── models/
│   ├── services/
│   ├── templates/
│   ├── static/
│   ├── extensions.py
│   └── __init__.py
│
├── migrations/
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

# 🗄 Database Models

- User
- Team
- Coach
- Player
- Training
- Match
- Attendance
- Injury
- Statistics
- Performance
- Transfer

---

# 👤 User Roles

| Role | Permissions |
|------|-------------|
| Admin | Full access to all modules |
| Coach | Manage assigned team, players, training sessions |
| Player | View personal information, training sessions, matches |
| Medical Staff | Manage injuries and recovery records |

---

# ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/sports-club-management.git
```

```bash
cd sports-club-management
```

---

### Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Database

```bash
flask db init
```

```bash
flask db migrate
```

```bash
flask db upgrade
```

---

### Run Application

```bash
python run.py
```

or

```bash
flask run
```

---

# 🔐 Authentication

Passwords are securely hashed using **Flask-Bcrypt** before storing them in the database.

Session management is handled using **Flask-Login**.

---

# 📌 API/Routes Overview

## Authentication

- Register
- Login
- Logout

## Team

- Create Team
- View Teams

## Coach

- Assign Coach
- View Coaches

## Player

- Add Player
- View Players
- Update Player
- Delete Player

## Training

- Create Training Session
- View Sessions
- Update Session
- Delete Session

## Match

- Schedule Match
- View Matches
- Update Match
- Delete Match

## Attendance

- Mark Attendance
- View Attendance

## Injury

- Record Injury
- Update Recovery
- View Injuries

## Performance

- Add Performance
- View Performance

## Transfer

- Transfer Player
- View Transfer History

---

# 🔒 Security

- Password Hashing
- Authentication using Flask-Login
- Role-Based Authorization
- Input Validation
- Duplicate Record Checks
- Relationship Validation

---

# 📚 Future Improvements

- REST API support
- JWT Authentication
- Email Verification
- Player Statistics Dashboard
- Match Analytics
- Notifications
- File Uploads
- Docker Support
- PostgreSQL Deployment
- Frontend with React

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Samarth Prabhu**

Backend Developer | Python | Flask | SQLAlchemy