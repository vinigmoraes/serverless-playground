integration-test: start-serverless-offline access-integration-test run-test

start-serverless-offline:
	AWS_PROFILE=serverless-admin serverless offline

deploy: export-dependencies deploy-application

export-dependencies:
	poetry export -f requirements.txt > requirements.txt --without-hashes

deploy-application:
	serverless deploy



