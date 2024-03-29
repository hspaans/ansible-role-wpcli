"""Role testing files using testinfra."""

import pytest


@pytest.mark.parametrize("file", [
    "/usr/local/bin/wp",
    "/etc/bash_completion.d/wp_local"
])
def test_file_exists(host, file):
    """Test if file is present."""
    item = host.file(file)

    assert item.is_file
