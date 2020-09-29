"""Demonstrates how to make a simple call to the Natural Language API."""

import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def print_result(annotations):
    count = 0

    for num,entity in enumerate(annotations.entities):
        print('Entity {}\n'.format(num))
        print('Name: {}\n'.format(entity.name))
        print('Type: {}\n'.format(enums.Entity.Type(entity.type).name))
        print('Metadata: {}\n'.format(entity.metadata))
        print('Salience: {}\n\n'.format(entity.salience))
        count += 1

    print('Total number of entities found: {}'.format(count))
    return 0


def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    with open(movie_review_filename, 'r') as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_entities(document=document,encoding_type='UTF32')

    # Print the results
    print_result(annotations)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'movie_review_filename',
        help='The filename of the movie review you\'d like to analyze.')
    args = parser.parse_args()

    analyze(args.movie_review_filename)