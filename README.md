# Group 3 Vet Appointment Scheduler

## Run the Django database locally

From the repository root in PowerShell, run:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

Open [Django admin](http://127.0.0.1:8000/admin/). Create a user with the owner's name, add their address and phone number in an owner profile, then add their pets. Each owner can have multiple pets. Future intake records can reference `accounts.Pet`.
