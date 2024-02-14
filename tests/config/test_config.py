from unittest.mock import patch

import pytest

from lims_utils.settings import Settings


@pytest.mark.asyncio
@patch("lims_utils.config.json.loads")
async def test_return_default(mock_json_loads):
    """Should return default values"""
    mock_json_loads.return_value = {"auth": {}, "db": {}}

    settings = Settings()

    assert settings.auth.endpoint == "https://localhost/auth"


@pytest.mark.asyncio
@patch("lims_utils.config.json.loads")
async def test_custom(mock_json_loads):
    """Should return custom values"""
    mock_json_loads.return_value = {
        "auth": {"endpoint": "https://localhost/diff-auth"},
        "db": {"pool": 90},
    }

    settings = Settings()

    assert settings.auth.endpoint == "https://localhost/diff-auth"

    assert settings.db.pool == 90
