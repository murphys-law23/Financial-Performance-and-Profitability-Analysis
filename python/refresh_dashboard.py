from pathlib import Path
import csv, json, re
root = Path(__file__).resolve().parents[1]
source = next((root / 'data').glob('*.csv'))
rows = list(csv.DictReader(source.open()))
path = root / 'dashboard' / 'index.html'
html = path.read_text()
html, count = re.subn(r'const DATA=.*?;const \$=', lambda m: 'const DATA=' + json.dumps(rows, separators=(',', ':')) + ';const $=', html, count=1, flags=re.S)
assert count == 1, 'Embedded dataset marker not found'
path.write_text(html)
print('Updated embedded dashboard data from', source.name)
