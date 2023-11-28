import apache_beam as beam

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


with beam.Pipeline() as pipeline:
    lines = pipeline | "ReadFromText" >> beam.io.ReadFromText("example/kakaotalk.txt")
    filter_line = (
        lines
        | "Split1" >> beam.Map(lambda line: line.split())
        | "Filter" >> beam.Filter(lambda line: len(line) > 6)
        | "JoinText1" >> beam.Map(" ".join)
    )
    transform = (
        filter_line
        | "SplitDate" >> beam.Map(lambda line: line.split(","))
        | "Transform" >> beam.ParDo(TransformDatetime())
    )
    
    anonymize = (
        transform
        | "Anonymize" >> beam.ParDo(Anonymize())
        | "JoinText2" >> beam.Map(" : ".join)
    )
    anonymize | "WriteToText" >> beam.io.WriteToText("example/kakaotalk_anonymize.txt")
