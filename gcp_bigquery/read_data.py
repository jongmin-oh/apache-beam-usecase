import apache_beam as beam
from apache_beam.io.gcp.internal.clients import bigquery

table_spec = bigquery.TableReference(
    projectId='reppley-ai',
    datasetId='test',
    tableId='player'
)

with beam.Pipeline() as pipeline:
    max_temperatures = (
        pipeline
        | 'ReadTable' >> beam.io.ReadFromBigQuery(table=table_spec, gcs_location='gs://test-player')
        # Each row is a dictionary where the keys are the BigQuery columns
        # | 'Temp' >> beam.Map(lambda elem: elem['p_name'])
        | 'Print' >> beam.Map(print)
    )