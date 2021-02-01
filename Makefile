#Docker Compose
server-compose-interactive:
	docker-compose build
	docker-compose up 

server-compose-background:
	docker-compose build
	docker-compose up -d 

server-compose-production:
	docker-compose build
	docker-compose -f docker-compose.yml -f docker-compose-production.yml up -d

attach:
	docker exec -i -t gnps_datasetcache_gnps-datasetcache-web_1 /bin/bash

attach-worker:
	docker exec -i -t gnps_datasetcache_gnps-datasetcache-worker_1  /bin/bash

