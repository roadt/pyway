import click


@click.command()
@click.option('--message', '-m', multiple=True)
def commit(message):
    click.echo('\n'.join(message))


@click.command()
@click.option('--message', '-m', multiple=True, default=["a", "b"])
def commit2(message):
    click.echo('\n'.join(message))

if __name__ == '__main__':
    commit2()
