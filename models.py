# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Entry(db.Model):
    __tablename__ = 'entries'   
    
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(120), unique=True, nullable=False, index=True)
    word = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(100), nullable=False)
    
    transliteration = db.Column(db.String(100), nullable=True)
    submitted_by = db.Column(db.String(100), nullable=True)

    literal_definition = db.Column(db.Text, nullable=True)
    etymology = db.Column(db.Text, nullable=True)
    story = db.Column(db.Text, nullable=True)

    origin = db.Column(db.String(150), nullable=True)
    dialect = db.Column(db.String(100), nullable=True)
    source = db.Column(db.String(250), nullable=True)

    status = db.Column(db.String(20), default="pending")  
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class EntryEdit(db.Model):
    __tablename__ = 'entry_edits'
    id = db.Column(db.Integer, primary_key=True)
    entry_id = db.Column(db.Integer, db.ForeignKey('entries.id'), nullable=False)

    transliteration = db.Column(db.String(100), nullable=True)
    word = db.Column(db.String(100), nullable=True)
    language = db.Column(db.String(100), nullable=True)
    literal_definition = db.Column(db.Text, nullable=True)
    etymology = db.Column(db.Text, nullable=True)
    story = db.Column(db.Text, nullable=True)
    origin = db.Column(db.String(150), nullable=True)
    dialect = db.Column(db.String(100), nullable=True)
    source = db.Column(db.String(250), nullable=True)
    submitted_by = db.Column(db.String(100), nullable=True)
    
    status = db.Column(db.String(20), default="pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    entry = db.relationship('Entry', backref=db.backref('edits', lazy=True))
