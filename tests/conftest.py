import pytest
from sqlmodel import SQLModel

import app.models.alert  # noqa: F401
import app.models.health_check  # noqa: F401
import app.models.stellar_health  # noqa: F401
from app.db.database import engine


@pytest.fixture(autouse=True)
def setup_database():
    SQLModel.metadata.create_all(engine)
    yield
