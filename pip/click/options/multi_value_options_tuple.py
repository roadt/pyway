import click


@click.command()
@click.option('--item', type=(str, int), required=True)
def putitem(item):
    name, id = item
    click.echo(f"name={name} id={id}")

@click.command()
@click.option('--item', nargs=2, type=click.Tuple([str, int]), required=True)
def putitem2(item):
    name, id = item
    click.echo(f"name={name} id={id}")

if __name__ == '__main__':
    putitem2()
