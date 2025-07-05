from backend.config.settings import settings
from backend.db.database import Base, engine

print("DEBUG DATABASE_URL:", settings.DATABASE_URL)

Base.metadata.create_all(bind=engine)

