import apache_beam as beam
from de_identify import DeIdentifier


class Anonymize(beam.DoFn):
    def process(self, element):
        element[-1] = DeIdentifier.run_info(element[-1])
        element[-1] = DeIdentifier.run_name(element[-1], "김철수", "신짱구")
        element[-3] = DeIdentifier.run_name(element[-3], "김철수", "신짱구")
        yield element


with beam.Pipeline() as pipeline:
    lines = pipeline | "ReadFromText" >> beam.io.ReadFromText("example/kakaotalk.txt")
    processing = (
        lines
        | "Split" >> beam.Map(lambda line: line.split())
        | "Filter" >> beam.Filter(lambda line: len(line) > 6)
        | "ContextMerge" >> beam.Map(lambda line: line[:7] + [" ".join(line[7:])])
        | "Anonyzmize" >> beam.ParDo(Anonymize())
        | "Join" >> beam.Map(" ".join) 
        | "Print" >> beam.Map(print)
    )