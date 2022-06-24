
import sys
import click

@click.command()
@click.option('--shout/--no-shout', default=False)
def info(shout):
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!111'
    click.echo(rv)


#If you really don’t want an off-switch, you can just define one and manually inform Click that something is a flag:
@click.command()
@click.option('--shout', is_flag=True)
def info2(shout):
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!111'
    click.echo(rv)


#Note that if a slash is contained in your option already (for instance, if you use Windows-style parameters where / is the prefix character), you can alternatively split the parameters through ; instead:
@click.command()
@click.option('/debug;/no-debug')
def log(debug):
    click.echo(f"debug={debug}")


#If you want to define an alias for the second option only, then you will need to use leading whitespace to disambiguate the format string:
@click.command()
@click.option('--shout/--no-shout', ' /-S', default=False)
def info3(shout):
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!111'
    click.echo(rv)


#main
if __name__ == '__main__':
    #info()
    #info2()
    #log()
    info3()
