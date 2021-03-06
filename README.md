# JSON CRD

## Installation

JSON CRD requires python3.

For installing third-party-libraries it is a best pratice to use Virtual Environment

To install the jsonfile_crd library:

```
$ pip3 install dist/jsonfile_crd-1.0.1
```

## Getting Started

The class JsonFileOperation from `jsonfile_crd/jsonfile_operation/__init__.py` is responsible for validating filepath, key and value and also for executing operations like create, read, delete under thread-safe conditions.

The file `driver.py` shows a simple way of executing the above mentioned functions under
thread-safe conditions.

The thread-safe flow is created by referring from [threading](https://docs.python.org/3/library/threading.html).

* Before running `driver.py` in cmd by using `python driver.py`, load your json file within
the JsonFileOperation class, else `default.json` file will be autogenerated from the provided data.

```
jsonfile_obj = JsonFileOperation('<PathtoFile>')
```
* On calling create_data from JsonFileOperation class with key, value and an optional ttl(time-to-live) as arguments.

```
jsonfile_obj.create_data('datastream','abcdesfhgkt123',120)
```

returns as follows.

```
{"datastream": {"value": "abcdesfhgkt123", "ttl": 120}}
```
* On calling read_data from JsonFileOperation class with key as argument.

```
jsonfile_obj.read_data('datastream')
```

returns as follows.

```
abcdesfhgkt123
```

* On calling delete_data from JsonFileOperation class with key as argument.

```
jsonfile_obj.delete_data('datastream')
```

returns as follows.

```
data_deleted
```

## Testing

The test file is located in the `JSON_CRD/tests/test_jsonfile_operation.py`
The testing were referred from [pytest](https://docs.pytest.org/en/latest/getting-started.html).

The command to do test: `python setup.py pytest`

To test for key is alphanum.

```
test_key_isalpha()
```

To test for key is crossing 32 bytes.

```
test_key_read()
```

To test for given invalid filepath.

```
test_filepath()
```

To test for value is crossing 16 KB.

```
test_valuesize()
```

The function test_JsonFileOperation with key, value and ttl as arguments returns "data_created", "key", "data_deleted".

```
test_JsonFileOperation():
```
