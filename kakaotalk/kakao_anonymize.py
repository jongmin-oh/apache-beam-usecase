import apache_beam as beam

import base64
from deidentify import DeIdentifier
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


class GetId(beam.DoFn):
    def process(self, element):
        yield element[0]


with beam.Pipeline() as pipeline:
    lines = pipeline | "ReadFromText" >> beam.io.ReadFromText("example/kakaotalk.txt")
    filter_line = (
        lines
        | "Split1" >> beam.Map(lambda line: line.split())
        | "Filter" >> beam.Filter(lambda line: len(line) > 6)
        | "Join" >> beam.Map(" ".join)
    )
    transform = (
        filter_line
        | "SplitDate" >> beam.Map(lambda line: line.split(","))
        | "Transform" >> beam.ParDo(TransformDatetime())
    )
    
    get_id = (
        transform
        | "Print" >> beam.Map(print)
    )
        # | "SplitDate" >> beam.Map(lambda line: line.split(","))
        # | "TransformDatetime" >> beam.ParDo(TransformDatetime())
        # | "Anonyzmize" >> beam.ParDo(Anonymize())
        # | "Print" >> beam.Map(print)
