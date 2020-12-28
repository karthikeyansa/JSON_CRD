import click
from jsonfile_operation import JsonFileOperation


@click.command()
@click.option('--path', help='File path for output file', default='')
@click.option('--key', help='Key to be stored', required=True)
@click.option('--value', help='Value to be stored', required=True)
@click.option('--ttl', help='Time to live in secs', default=10)
def json_crd(path, key, value, ttl):
    try:
        obj = JsonFileOperation(path)
        obj.create_data(key, value, ttl)
        obj.read_data(key)
        obj.delete_data(key)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    json_crd()
