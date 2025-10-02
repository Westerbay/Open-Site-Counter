from app import Application

import uvicorn


def main():
    app = Application().get_app()
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5001,
        reload=False
    )    

if __name__ == "__main__":
    main()
