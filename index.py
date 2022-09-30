from downloadImages import download, listFile
r = download.delay('https://property145.com/media/documents/agent/property_10/tanah-kavling.png', 'property145.png')
r.ready()