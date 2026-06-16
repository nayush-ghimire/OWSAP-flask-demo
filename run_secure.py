from secure.app import app
from secure.database import init_db
init_db()
if __name__ == '__main__':
    app.run(port=5002, debug=True)