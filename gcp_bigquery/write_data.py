import apache_beam as beam
from apache_beam.io.gcp.internal.clients import bigquery

table_spec = bigquery.TableReference(
    projectId='reppley-ai',
    datasetId='test',
    tableId='player'
)

table_schema = {
    'fields': [
        {'name': 'pid', 'type': 'INTEGER', 'mode': 'REQUIRED'},
        {'name': 'p_name', 'type': 'STRING', 'mode': 'REQUIRED'},
        {'name': 'position', 'type': 'STRING', 'mode': 'REQUIRED'}
    ]
}


class ParseCsv(beam.DoFn):
    def process(self, element):
        index, name, position = element.split(',')
        return [{
            'pid': int(index),
            'p_name': name,
            'position': position.strip()
        }]


with beam.Pipeline() as pipeline:
    max_temperatures = (
        pipeline
        | "Read from Text" >> beam.io.ReadFromText("example/player.txt", skip_header_lines=1)
        | 'TransformData' >> beam.ParDo(ParseCsv())
        | "Quotes" >> beam.io.WriteToBigQuery(
            table=table_spec,
            schema=table_schema,
            write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            custom_gcs_temp_location='gs://test-player'
        )
    )