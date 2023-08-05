from website import create_app
from website import db

app = create_app()

app.app_context().push()
db.create_all()

if __name__ == "__main__":
    app.run(debug=True)