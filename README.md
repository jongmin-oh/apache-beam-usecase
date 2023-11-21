# Apache Beam Python Client
Base Function and Usecase

 - Python 3.11

```
pip install apache-beam==2.51.0
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
'Write to text'>> beam.io.WriteToText('regular_filter.txt'))
```

### 5. Filter
```python
def is_midfielder(text):
    return text[2] == "MF"

"Filter Postion" >> beam.Filter(is_midfielder)
```

### Reference
- https://esevan.tistory.com/19
