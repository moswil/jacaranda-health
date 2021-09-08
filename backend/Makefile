db_migrate:
	docker-compose exec web python src/manage.py create_db

db_ssh:
	docker-compose exec db psql --username=jacaranda_health --dbname=jacaranda_health_dev

init_migrations:
	docker-compose exec web python src/manage.py db init -d src/migrations

migrate:
	docker-compose exec web python src/manage.py db migrate -d src/migrations

upgrade:
	docker-compose exec web python src/manage.py db upgrade -d src/migrations