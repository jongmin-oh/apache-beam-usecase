import apache_beam as beam


def add_heart(text):
    return text + " ❤️ "


with beam.Pipeline() as pipeline:
    lines = pipeline | "ReadFromText" >> beam.io.ReadFromText("example/hello.txt")
    processing = (
        lines 
        | "Add Text" >> beam.Map(add_heart) 
        | "Print" >> beam.Map(print)
    )
