import os
import sys
import json
import argparse

import xml.etree.ElementTree as ET
from apkinfo.utils import Utils
from rich.console import Console

console = Console()
utils = Utils()

packageName = ''
permissions = json.loads(open(os.path.join("config", "permissions.json")).read())

def check_dependencies():
    if os.system('which jadx') != 0:
        utils.logError('Please install jadx')
        sys.exit(0)
    
# Extract information from the AndroidManifest.xml file
def extract_info(xml):
    android = str(xml.attrib)[2:int(str(xml.attrib).index('}')+1)]
    utils.logInfo('Extracting information from the AndroidManifest.xml file')
    check_dependencies()

    # Package information
    utils.printTitle('Package Information')
    for i in xml.attrib:
        if i == 'package':
            utils.printText(f'Package Name: {xml.attrib[i]}')
            packageName = xml.attrib[i]
        if "versionName" in i:
            utils.printText(f'Version Name: {xml.attrib[i]}')
        if f"{android}compileSdkVersion" == i:
            utils.printText(f'Compiler SDK Version: {xml.attrib[i]}')
        clean_up()
    print()

    # Permissions
    utils.printTitle('Permissions')
    for child in xml:
        if child.tag == 'uses-permission' and child.attrib[f'{android}name'][len(packageName)+1:] in permissions:
            utils.printText(f"{child.attrib[f'{android}name'][len(packageName)+1:]} -> {permissions[child.attrib[f'{android}name'][len(packageName)+1:]]}")
        elif child.tag == 'uses-permission':
            utils.printText(f"{child.attrib[f'{android}name'][len(packageName)+1:]}")
    print()

    # Activities and Services
    utils.printTitle('Activity')
    for child in xml:
        if child.tag == 'application':
            for activity in child:
                if activity.tag == 'activity':
                    utils.printText(f'{activity.attrib[f'{android}name']} : Exported = {activity.attrib[f'{android}exported']}')
    
def decompile_apk(apk_path):
    with console.status("Decompiling APK ", spinner="dots2"):
        os.system('mkdir temp_decompile')
        os.system(f'jadx {apk_path} -d ./temp_decompile/apk_decompiled')
    xml = utils.checkFile(f'./temp_decompile/apk_decompiled/Resources/AndroidManifest.xml')
    utils.logInfo('APK decompiled successfully')
    return xml

def clean_up():
    os.system('rm -rf temp_decompile')

def parse_args():
    parser = argparse.ArgumentParser(description='A simple tool to extract data from Android Mainfest files')
    parser.add_argument('--apk', type=str, help='The path to the APK file', required=False)
    parser.add_argument('--xml', type=str, help='The path to the AndroidManifest.xml file', required=False)
    parser.add_argument('--output', type=str, help='The output file', required=False)
    return parser.parse_args()

def parse_manifest(file_path):
    if os.path.exists(file_path) is False:
        utils.logError(f'The file {file_path} does not exist')
        sys.exit(0)
    else:
        if file_path.endswith('.xml'):
            amxml = utils.convert_to_xml(file_path)
            extract_info(amxml)

        elif file_path.endswith('.apk'):
            xml_path = decompile_apk(file_path)
            amxml = utils.convert_to_xml(xml_path)
            extract_info(amxml)

        else:
            utils.logError('Unsupported file format')
            sys.exit(0)
            
                
def main():
    utils.heading()
    choice = parse_args()
    if choice.apk and choice.xml:
        utils.logError('Please provide either apk or AndroidManifest.xml file')
        exit(0)
    elif choice.apk:
        parse_manifest(choice.apk)
    elif choice.xml:
        parse_manifest(choice.xml)
    else:
        utils.logError('Usage: python3 apkinfo.py -apk <path_to_apk> -xml <path_to_AndroidManifest.xml> -output <output_file>')