import apache_beam as beam

# MapTuple for key-value pairs
with beam.Pipeline() as pipeline:
    plants = (
        pipeline
        | "Gardening plants" >> beam.Create(
            [
                ("1", "Strawberry"),
                ("2", "Carrot"),
                ("3", "Eggplant"),
                ("4", "Tomato"),
                ("5", "Potato"),
            ]
        )
        | "Format" >> beam.MapTuple(lambda idx, plant: "{}:{}".format(idx, plant))
        | beam.Map(print)
    )
