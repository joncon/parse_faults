#!/usr/bin/env python
import xml.etree.ElementTree as etree    
tree = etree.parse('./all_faults.kml')  
root = tree.getroot()
print root
                    