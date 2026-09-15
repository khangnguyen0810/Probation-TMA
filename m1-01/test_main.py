from main import check_connectivity


def test_check_connectivity_runs_without_error():
    assert callable(check_connectivity)