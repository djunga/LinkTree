# Create the manifest
import json

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


# Example
data = {}
data['name'] = "Getting Started Example"
data['version'] = "1.0"
data['description'] = "Build an Extension!"
data['manifest_version'] = 2



writeToJSONFile('./','manni',data)
# './' represents the current directory so the directory save-file.py is in
# 'test' is my file name
