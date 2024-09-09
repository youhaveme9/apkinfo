from rich import print
from pyfiglet import Figlet
import xml.etree.ElementTree as ET
import time
import os

class Utils:
    def heading(self):
        f = Figlet(font='slant')
        print(f.renderText('Android Info'))
        print(f"[bold green]v1.0.0[/bold green]")
        print(f"[bold green]---[/bold green]")
        print(f"[bold green]Extract useful information from AndroidManifest.xml[/bold green]")
        print("\n\n")

    def logInfo(self, message: str):
        print(f"[bold blue][+] {message}[/bold blue]")
    
    def logError(self, message: str):
        print(f"[bold red][-] {message}[/bold red]")

    def logWarning(self, message: str):
        print(f"[bold yellow][!] {message}[/bold yellow]")

    def printTitle(self, title: str):
        print(f"[bold green][{title}] : [/bold green]")

    def printText(self, text: str):
        print(f"[yellow]{text}[/yellow]")

    def checkFile(self, file: str):
        try:
            with open(file, 'r') as f:
                return os.path.abspath(file)
        except FileNotFoundError:
            self.logError(f'The file {file} does not exist')
            exit(0)
    
    def convert_to_xml(self, xml):
        try:
            xml = ET.parse(xml)
            print(f'xml: {xml}')
            return xml.getroot()
        except Exception as e:
            self.logError(f'Error parsing the XML file: {e}')
            exit(0)