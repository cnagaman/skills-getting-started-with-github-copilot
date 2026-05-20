import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activities before each test for isolation."""
    baseline = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(copy.deepcopy(baseline))
