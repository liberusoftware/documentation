#!/usr/bin/env python3
"""Validate proposed enterprise request schemas, examples and route alignment."""
import json
from pathlib import Path
import re
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]


def main():
    root=ROOT/'projects/sap'
    examples=json.loads((root/'design/api-command-examples.json').read_text())
    for slug,command in examples.items():
        request=json.loads((root/'api/contracts'/f'{slug}.request.schema.json').read_text())
        example=json.loads((root/'api/contracts'/f'{slug}.request.example.json').read_text())
        Draft202012Validator.check_schema(request)
        validator=Draft202012Validator(request)
        validator.validate(example)
        assert example==command['body'],slug+': published body drifted from authored example'
        assert not validator.is_valid({**example,'unexpected_property_example':'rejected'}),slug+': unknown properties not rejected'
        design=(root/'design'/f'{slug}.md').read_text()
        paths=re.findall(r'^\| POST \| `([^`]+)`',design,re.M)
        assert any(path.endswith('/'+command['action']) for path in paths),slug+': command is missing from the domain route plan'
        doc=(root/'api'/f'{slug}.md').read_text()
        assert f'{slug}.request.schema.json' in doc and f'/{command["action"]}' in doc
    print(f'Validated {len(examples)} draft JSON Schemas and examples, unknown-property rejection, and domain/API command alignment.')
    print('This checks documentation contracts only; it does not establish implemented business validation or a deployed API.')


if __name__=='__main__':main()
