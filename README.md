# JSON CRD

## Installation

JSON CRD requires python3.

This install all the necessary dependancies:

```
$ pip install -r requirements.txt
```

This install the jsonfile_crd as python packages:

```
$ python setup.py develop
```

## Testing

The test file is located in the `JSON_CRD/tests/test_jsonfile_operation.py`
The testing were referred from pytest `https://docs.pytest.org/en/latest/getting-started.html`

The command to do test:
`python setup.py pytest`

The function to tests for creating data

```
test_create(key, value, ttl)
```

The function to tests for creating data

```
test_read(key)
```

The function to tests for creating data

```
test_delete(key)
```
