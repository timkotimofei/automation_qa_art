import pytest
import logging
@pytest.mark.smoke
def test_smoke_example():
    logging.info('Prepare to printing')
    print("Running smoke test!")
    logging.info('After print preparations')
    assert 1 == 1

@pytest.mark.regression
def test_regression_example():
    print("Running regression test!")
    assert 2 == 2

# pytest -m smoke
# pytest -m regression
# pytest -m regression tests/ui_tests - запуск в новой организации тестов

