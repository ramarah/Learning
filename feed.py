import yaml
import xml.etree.ElementTree as Xml_tree

with open('feed.yaml','r') as file:
    yaml_data = yaml.safe_load(file)

    rss_element = Xml_tree.Element('rss', {'version':'2.0',
    'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:content':'http://purl.org/rss/1.0/modules/content/'})

    link_prefix = yaml_data['link']

    channel_element = Xml_tree.SubElement(rss_element,'channel')
    Xml_tree.SubElement(channel_element,'title').text = yaml_data['title']
    Xml_tree.SubElement(channel_element,'format').text = yaml_data['format']
    Xml_tree.SubElement(channel_element,'subtitle').text = yaml_data['subtitle']
    Xml_tree.SubElement(channel_element,'itunes:author').text = yaml_data['author']
    Xml_tree.SubElement(channel_element,'itunes:image',{'href': link_prefix + yaml_data['image']}) 
    Xml_tree.SubElement(channel_element,'link').text = link_prefix
    Xml_tree.SubElement(channel_element,'language').text = yaml_data['language']
    Xml_tree.SubElement(channel_element,'itunes:category',{'text': yaml_data['category']}) 

    for item in yaml_data['item']:
        item_element = Xml_tree.SubElement(channel_element, 'item')
        Xml_tree.SubElement(item_element, 'title').text = item['title']
        Xml_tree.SubElement(item_element, 'itunes:author').text = yaml_data['author']
        Xml_tree.SubElement(item_element, 'description').text = item['description']
        Xml_tree.SubElement(item_element, 'itunes:duration').text = item['duration']
        Xml_tree.SubElement(item_element, 'pubDate').text = item['published']
        Xml_tree.SubElement(item_element, 'title').text = item['title']

        enclosure = Xml_tree.SubElement(item_element, 'enclosure', {
            'url': link_prefix + item['file'],
            'type': 'audio/mpeg',
            'length': item['length']
        })
  

    output_tree = Xml_tree.ElementTree(rss_element)
    output_tree.write('podcast.xml',encoding='UTF-8',xml_declaration=True)
    