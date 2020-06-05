import click

from flask.cli import FlaskGroup, with_appcontext

from sangetal.app import create_app


@click.group(cls=FlaskGroup, create_app=create_app)
@with_appcontext
def sangetal():
    pass

@sangetal.command()
def version():
    from sangetal.version import __version__
    
    print('sangetal version ', __version__)
