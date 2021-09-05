db_migrate:
	docker-compose exec web python src/manage.py create_db

db_ssh:
	docker-compose exec db psql --username=jacaranda_health --dbname=jacaranda_health_dev