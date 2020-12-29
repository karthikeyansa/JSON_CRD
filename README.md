# JSON CRD

## Installation

JSON CRD requires python3.

For installing third-party-libraries it is a best pratice to use Virtual Environment

This install all the necessary dependancies:

```
$ pip3 install dist/jsonfile_crd-1.0.6
```

## Testing

The test file is located in the `JSON_CRD/tests/test_jsonfile_operation.py`
The testing were referred from pytest `https://docs.pytest.org/en/latest/getting-started.html`

The command to do test:
`python setup.py pytest`

The function test_JsonFileOperation with key, value and ttl as arguments
returns "data_created", "key", "data_deleted".

```
test_JsonFileOperation()
```
