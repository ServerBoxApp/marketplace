from pathlib import Path
import yaml,json
workdir = Path('.')
templates = list(workdir.glob('*.yml'))

def generate():
    data = {}
    for template in templates:
        json_data = yaml.safe_load(template.read_text())
        data[json_data['info']['id']] = json_data
    product = workdir / 'data.json'
    product.write_text(json.dumps(data,indent=2, sort_keys=False))



def verify_all():
    for template in templates:
        if not verify(template.read_text()):
            return False
    return True

def verify(content):
    #TODO Finish the verify function.
    return True
