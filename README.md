# Tesseract — Real-time Team Collaboration Hub (Django)

Live demo (backend ready): https://<>

Short pitch:
Tesseract is a Slack+Trello style collaboration app built with Django, DRF, Channels (WebSockets), and React-ready APIs. It includes:
• Teams & membership
• Boards → Columns → Tasks (Kanban)
• Real-time chat (Django Channels + Redis)
• JWT auth (SimpleJWT)
• AI automation hooks (planned: AutoFlow integrations)

How to run locally:
1. python -m venv env
2. env\Scripts\activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. redis-server   (or use Docker)
6. python manage.py runserver

Contact: Tarun HT — github.com/Tarun08940 — linkedin.com/in/tarun-ht-7a4278343
