from scholarly import scholarly
import json

# Use your Google Scholar ID
author = scholarly.search_author_id('bcaxipEAAAAJ')
author = scholarly.fill(author)

metrics = {
    "publications": len(author.get('publications', [])),
    "citations": author['citedby'],
    "h_index": author['hindex']
}

with open("data/metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)
