run-api:
	go run server.go

run-frontend:
	@cd frontend && npm run dev

test:
	go test
