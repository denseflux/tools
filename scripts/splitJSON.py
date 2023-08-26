import json
import pypandoc
import logging
import html2markdown
import html5lib_to_markdown 

logging.getLogger('pypandoc').addHandler(logging.NullHandler())

def split_json_file(input_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Assuming the JSON content is an array
    for index, item in enumerate(data['items']):
        if index == 1:
            print(html2markdown.convert(item["content"]))
            

            #print(str(pypandoc.convert_text(jsonString,to='markdown', format='json')))
        output_file = f'../data/{data["items"][index]["anchor"]}.md'
        #with open(output_file, 'w') as f:
        #    itemString = str(json.dumps(item))
        #    f.write(str(pypandoc.convert_text(itemString,'json', 'markdown')))
            #print(itemString)
            #docPart = pandoc.read(itemString, format="json")
            #return pandoc.write(docPart,format="markdown")
            # cdocPartMd, f, indent=4)

        #print(f'Split item {index}: {output_file}')

# Example usage
input_file = '../data/entries.json'
split_json_file(input_file)