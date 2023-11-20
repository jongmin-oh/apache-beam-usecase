import apache_beam as beam
from de_identify import DeIdentifier
from transform_datetime import datetime_to_int


class Anonymize(beam.DoFn):
    def process(self, element):
        split_data = element[-1].split(' : ')
        name = split_data[0]
        utterance = split_data[1]
        utterance = DeIdentifier.run_info(utterance)
        utterance = DeIdentifier.run_name(utterance, "김철수", "신짱구")
        name = DeIdentifier.run_name(name, "김철수", "신짱구").strip()
        yield [element[0], name, utterance]


class TransformDatetime(beam.DoFn):
    def process(self, element):
        element[0] = datetime_to_int(element[0]).strftime("%Y-%m-%d %H:%M")
        yield element


with beam.Pipeline() as pipeline:
    lines = pipeline | "ReadFromText" >> beam.io.ReadFromText("example/kakaotalk.txt")
    processing = (
        lines
        | "Split" >> beam.Map(lambda line: line.split())
        | "Filter" >> beam.Filter(lambda line: len(line) > 6)
        | "Join" >> beam.Map(" ".join) 
        | "SplitDate" >> beam.Map(lambda line: line.split(","))
        | "TransformDatetime" >> beam.ParDo(TransformDatetime())
        | "Anonyzmize" >> beam.ParDo(Anonymize())
        | "Print" >> beam.Map(print)
    )
