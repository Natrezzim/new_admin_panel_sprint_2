.DEFAULT_GOAL := help
help:
	$(info build up build_up start down destroy stop restart firsts_start)
build:
	docker-compose -f docker-compose.yml build
up:
	docker-compose -f docker-compose.yml up -d
build_up: build up
start:
	docker-compose -f docker-compose.yml start
down:
	docker-compose -f docker-compose.yml down
destroy:
	docker-compose -f docker-compose.yml down -v
stop:
	docker-compose -f docker-compose.yml stop
restart:
	docker-compose -f docker-compose.yml stop
	docker-compose -f docker-compose.yml up -d
first_start: build_up
	docker exec -it online_cinema-service-1 sh /usr/src/first_start.sh


