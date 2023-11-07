import os

os.system('git bisect start c1a4be04b972b6c17db242fc37752ad517c29402 c1a4be04b972b6c17db242fc37752ad517c29402')
os.system('git bisect run python manage.py test')