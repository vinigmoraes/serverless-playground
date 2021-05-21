integration-test: start-serverless-offline access-integration-test run-test

start-serverless-offline:
	AWS_PROFILE=serverless-admin serverless offline

access-integration-test:
	cd test/integration

run-test:
	pytest

