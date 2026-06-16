from vulnerable.app import app
from vulnerable.database import init_db
init_db()
if __name__ == '__main__':
    app.run(port=5001, debug=True)