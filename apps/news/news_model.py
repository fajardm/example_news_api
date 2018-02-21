from helpers.database import db
from helpers.base_model import BaseModel


class News(BaseModel):
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.TEXT, nullable=False)
    status = db.Column(db.Enum('draft', 'publish'), nullable=False, default='draft')
