import os
os.system('git log')
os.system('git bisect start')
os.system('git bisect good 6ca24e408f1c16411abf140f9928cfe4ddec3f7d')
os.system('git bisect bad c1a4be04b972b6c17db242fc37752ad517c29402')
os.system('git bisect run python manage.py test')