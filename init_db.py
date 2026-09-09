from app import app, db

with app.app_context():
    print("making tables")
    db.create_all()
    print("done!")
