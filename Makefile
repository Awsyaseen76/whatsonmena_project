MAKE_DIR = $(PWD)

auth_make = $(MAKE_DIR)/back
auth_vue = $(MAKE_DIR)/front

start: 
	# cd $(auth_make) && make start && docker run -it -d -p 4200:80 --rm --name dockerize-vuejs dockerize-vue
	cd $(auth_make) && make start && docker run -it -d -p 4200:80 --rm --name auth-service auth-vue

start-dev: 
	cd $(auth_make) && make start && cd $(auth_vue) && npm run serve

stop: 
	cd $(auth_make) && make stop

kill:
	docker kill $$(docker ps -q)

superuser:
	cd $(auth_make) && make superuser
	
db:
	cd $(auth_make) && make db

make_migrations:
	cd $(auth_make) && make make_migrations

migrate:
	cd $(auth_make) && make migrate


	# build new docker then run it
	# docker build -t auth-vue .
	# docker run -it -p 4200:80 --rm --name auth-vuejs dockerize-vue