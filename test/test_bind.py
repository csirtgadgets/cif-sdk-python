from cifsdk.format.cifbind import Bind

import re


def test_format_bind():
    data = [
        {
            'observable': "example.com",
            'provider': "me.com",
            'tlp': "amber",
            'confidence': "85",
            'reporttime': '2015-01-01T00:00:00Z',
            'otype': 'fqdn'
        },
        {
            'observable': "example2.com",
            'provider': "me.com",
            'tlp': "amber",
            'confidence': "85",
            'reporttime': '2015-01-01T00:00:00Z',
            'otype': 'fqdn'
        },
        {
            'observable': "example3.com",
            'provider': "me.com",
            'tlp': "amber",
            'confidence': "85",
            'reporttime': '2015-01-01T00:00:00Z',
            'otype': 'fqdn'
        },
    ]

    text = str(Bind(data))
    assert re.findall(r'^// generated by: CIF at \S+', text)
    assert re.findall(r'\nzone "example.com" {type master; file "\S+";};\n', text)
    assert re.findall(r'\nzone "example3.com" {type master; file "\S+";};', text)

if __name__ == '__main__':
    test_format_bind()