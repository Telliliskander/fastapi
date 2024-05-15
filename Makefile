.PHONY: start start_build unit_tests check_typing

start :
	@docker-compose up -d 

start_build : 
	@docker-compose up --build -d

stop :
	@docker-compose down 

unit_tests : 
	@docker-compose exec -T app-test \
	@$(UNIT_TESTS)

unit_tests_local : 
	@$(UNIT_TESTS)

chech-typing :
	@docker-compose exec -T app-test mypy .