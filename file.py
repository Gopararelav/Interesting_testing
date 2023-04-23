import click


@click.command()
@click.option('--count', prompt="hi?", help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    """Приветствует ИМЯ (`name`), несколько (`count`) раз."""
    for x in range(int(count)):
        click.echo(f"Hello {name}!")


hello()
