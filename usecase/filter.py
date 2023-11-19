import apache_beam as beam


def is_midfielder(text):
    return text[2] == "MF"


# from external resources
pipeline = beam.Pipeline()

grocery = (
    pipeline
    | "Read from Text" >> beam.io.ReadFromText("example/player.txt", skip_header_lines=1)
    | "split the record" >> beam.Map(lambda record: record.split(","))
    | "Filter Postion" >> beam.Filter(is_midfielder)
    | "Print" >> beam.Map(print)
)

pipeline.run()
