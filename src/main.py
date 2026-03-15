import sys
import json
import click


@click.command()
@click.option('--verbose', '-v', is_flag=True)
@click.argument('file', type=click.File("r"), default=sys.stdin)
def main(file, verbose): 
    text = file.read()
    parsed = json.loads(text)
    to_print = json.dumps(parsed, indent=4, sort_keys=True)
    print(to_print)


if __name__ == '__main__':
    main()