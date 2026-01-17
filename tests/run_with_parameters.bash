pytest -v # verbouse printing log

pytest --collect-only  # don't run only show tests

# look for distinct unique named tests
pytest -k "asdict or defaults" --collect-only

# look for marked tests @pytest.mark.run_smoke
pytest -m "run_smoke"

# exit immediately
pytest -x
pytest --maxfail=1

# without traceback printing
pytest --tb=no

# show print from tests)
pytest  -s 
pytest --capture=no


# print local variables from failed tests
pytest -l 
pytest --showlocals

# print duration duration=0 - all tests time
pytest --duration=0
