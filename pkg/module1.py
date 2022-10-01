from enum import StrEnum

import click

class Foo(StrEnum):
    bar = 'bar'
    baz = 'baz'

some_foos = {Foo.bar, Foo.baz}


@click.command
def cli():
    ...


reveal_type(Foo.bar)
reveal_type(some_foos)
