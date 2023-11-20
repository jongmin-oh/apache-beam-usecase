import apache_beam as beam


def split_words(text):
    return text.split(",")


with beam.Pipeline() as pipeline:
    plants = (
        pipeline
        | "Gardening plants" >> beam.Create(
            [
                "🍓Strawberry,🥕Carrot,🍆Eggpl",
                "🍅Tomato,🥔Pota",
            ]
        )
        | "Split words" >> beam.FlatMap(split_words)
        | beam.Map(print)
    )
