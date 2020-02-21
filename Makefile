dub:
	docker-compose up -d --build

das:
	docker exec -it $(container) /bin/bash