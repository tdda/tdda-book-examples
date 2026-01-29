with open('format.json') as f:
    params = json.load(f)
df = pd.read_csv(path, **params)
