import click
import boto3


@click.command()
def shade():
    click.echo('Hello')

    # get pull request number

    # get coverage and upload to s3
