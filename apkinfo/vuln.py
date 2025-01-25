from openai import OpenAI
import os
import json
from dotenv import load_dotenv

class Vuln:
    def __init__(self):
        load_dotenv()
        self.API_KEY = os.getenv("OPENAI_KEY")
        self.client = OpenAI(
          api_key=self.API_KEY
        )

    def find_vulnerabilities(self, xml_path):
        
        with open(xml_path, "r") as file:
            file_content = file.read()

        completion = self.client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {
                "role": "user", 
                "content": f'''
                        Inspect the following content:\n\n{file_content}
                        Find all the potential vulnerabilities in the AndroidManifest.xml file and return a json object with the following structure:
                        
                            [
                            {{
                                "name": "Vulnerability Name",
                                "description": "Description of the vulnerability",
                                "line": "Line number where the vulnerability is found"
                            }}
                            ]
                        DO NOT include any other information in the response except the json. Also do not include the markdown code formmating. DO not use newline in the description.
                        '''
                }
        ]
        
        )

        vulnerabilities =  json.loads(completion.choices[0].message.content)
        return vulnerabilities

