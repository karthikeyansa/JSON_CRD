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

## Get Started

The main class is JsonFileOperation which is located in the `JSON_CRD/jsonfile_crd/__init__.py`
The cli commands were referred from click `https://click.palletsprojects.com/en/7.x/`

#### To do json_crd

```
$ json_crd --path="/Users/karthikeyan/desktop/testing/mydata.json" --key="round" --value="ball" --ttl=20
```

returns "Operations performed at /Users/karthikeyan/desktop/testing/mydata.json" for the above case.

```
$ json_crd --path="/Users/karthikeyan/desktop/testing/mydata.json"
```

returns "Failed for the following reason:
Missing option '--key'." for the above case.
