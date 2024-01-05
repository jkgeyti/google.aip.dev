import glob
import json
import os
import os

aips = {}
for f in sorted(glob.glob("../aip/**/*.md", recursive=True)):
    with open(f, 'r') as file:
        
        # read the aip
        data = file.read()
        json_data = json.dumps({"text": data})
        base_name = os.path.basename(f)
        base_name_prefix = os.path.splitext(base_name)[0]
        aip_number = int(base_name_prefix)        

        # extract the title
        lines = data.splitlines()
        title = ""
        description = ""
        
        while lines:
            line = lines.pop(0)
            if line.strip().startswith('# '):
                title = line.replace('# ', '')
                break

        while lines:
            line = lines.pop(0)
            if line.strip().startswith('#'):
                break
            description += line.replace("\n", " ").strip() + " "

        description = description.strip()

        if aip_number > 300:
            continue

        aips[aip_number] = {
            "title": title,
            "description": description,
            "text": data
        }

# write all aips to json files
for aip_number, aip in sorted(aips.items()):
    with open(f"json/{aip_number}.json", "w+") as f:
        f.write(json.dumps({"text": aip["text"]}))

# generate schema

schema_paths = {}
for aip_number, aip in sorted(aips.items()):
    path = f"json/{aip_number}.json"
    schema_paths[path] = {
        "get": {
            "description": aip['title'],
            "operationId": f"AIP-{aip_number}",
            "parameters": [],
        }
    }

schema = {
    "openapi": "3.1.0",
    "info": {
        "title": "Google AIP Guidelines",
        "description": "Google AIP Guidelines.",
        "version": "v1.0.0"
    },
    "servers": [
        {
        "url": "https://raw.githubusercontent.com/jkgeyti/google.aip.dev/master/fork/"
        }
    ],
    "paths": schema_paths,
    "components": {
        "schemas": {}
    }
}

print(json.dumps(schema, indent=2))