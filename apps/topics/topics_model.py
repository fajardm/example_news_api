from helpers.database import db
from helpers.base_model import BaseModel


class Topics(BaseModel):
    name = db.Column(db.String(255), nullable=False, unique=True)
