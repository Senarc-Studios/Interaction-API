import uvicorn

from fastapi import FastAPI, Request

app = FastAPI(
	docs_url = None,
	redoc_url = None
)

@app.get("/")
async def index(request: Request):
	return "This is a Discord Interaction Template.", 200

if __name__ == '__main__':
	try:
		uvicorn.run(
			"main:app",
			host = '127.0.0.1',
			port = SERVER_PORT[internal.Constants.fetch("ENVIRONMENT")],
			reload = True,
			debug = True,
			workers = 2
		)
	
	except Exception as error:
		print("Error: ", error)