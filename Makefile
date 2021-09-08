ex_1:
	python exercises/ex_1.py

ex_2:
	python exercises/ex_2.py

ex_3:
	python exercises/ex_3.py

ex_4:
	python exercises/ex_4.py

build:
	docker-compose build

start:
	docker-compose up -d

stop:
	docker-compose stop

down:
	docker-compose down

migrate:
	docker-compose run --rm api alembic revision --autogenerate -m ${message}

migrations:
	docker-compose run --rm api alembic upgrade head