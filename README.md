🏠 ComradeHousing

ComradeHousing is a housing management system designed to simplify user authentication, property management, and tenant interactions. It provides a secure and organized way to manage housing data and user accounts.

✨ Features

🔑 User Authentication: Secure login, registration, and password management

🏡 Property Management: Add, update, and remove properties (future)

💬 Tenant Interaction: Communication between tenants and admins

🛡️ Security: Password hashing and token-based authentication

⚙️ Installation

Clone the repository

git clone https://github.com/yourusername/comradeHousing.git


Navigate to the project directory

cd comradeHousing


Create a virtual environment (recommended)

python -m venv venv
# Activate it:
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Set environment variables

set SECRET_KEY=your_secret_key
set ALGORITHM=HS256

🚀 Usage

Run the application:

python main.py


Users can register and log in using the authentication module.

Future updates will include property management and tenant dashboards.

📂 Project Structure
comradeHousing/
│
├── Auth.py           # Authentication module (login, registration, password hashing)
├── main.py           # Entry point of the application
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation

🔮 Future Enhancements

Full CRUD for properties

Tenant and landlord dashboards

Email notifications

Integration with a database (SQLite/PostgreSQL)

🤝 Contributing

Contributions are welcome! Submit a pull request or open an issue for bug fixes or feature requests.

📝 License

MIT License © Ray
