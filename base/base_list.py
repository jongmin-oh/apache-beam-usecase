import apache_beam as beam


def add_heart(text):
    return text + " ❤️ "


with beam.Pipeline() as pipeline:
    result = (
        pipeline
        | "Create" >> beam.Create(["안녕하세요", "감사해요", "잘있어요", "다시만나요"])
        | "Add Text" >> beam.Map(add_heart)
        | "Print" >> beam.Map(print)
    )
