# Apache Beam Python Client
Base Function and Usecase

 - Python 3.11

```
pip install apache-beam[gcp]==2.51.0
```

### 1. Create
```python
"Create" >> beam.Create(["안녕하세요", "감사해요", "잘있어요", "다시만나요"])
```

#### 2. Map
```python
"Split" >> beam.Map(lambda record: record.split(","))
"Print" >> beam.Map(print) # 출력
```

### 3. ReadFromText
```python
"ReadFromText" >> beam.io.ReadFromText("example/hello.txt")
```

### 4. WriteToText
```python
'WriteToText'>> beam.io.WriteToText('regular_filter.txt'))
```

### 5. Filter
```python
def is_midfielder(text):
    return text[2] == "MF"

"FilterPostion" >> beam.Filter(is_midfielder)
```

### Reference
- https://esevan.tistory.com/19
- https://beam.apache.org/releases/pydoc/2.52.0/index.html
- https://github.com/apache/beam/tree/master/sdks/python/apache_beam/examples