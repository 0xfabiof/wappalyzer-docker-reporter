import json
import subprocess
import sys

input_list = sys.argv[1]
output_file = sys.argv[2]

output = open(output_file,'w')

output.write('''<html>
        <h1>Report</h1>
        <table align='center' border='1px solid black'>
        <tr>
            <th>site</th>
            <th>tech</th>
            <th>version</th>
        </tr>
        ''')
with open(input_list,'r') as file:
    for line in file:
        a = subprocess.check_output(['docker', 'run', '--rm','wappalyzer/cli' ,'https://%s' % line])
        a_json = json.loads(a)

        for i in range(0,len(a_json['applications'])):
            app_name = a_json['applications'][i]['name']
            app_version = a_json['applications'][i]['version']
            output.write('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (line,app_name,app_version))
            #print(a_json['applications'][i]['name'],a_json['applications'][i]['version'])
        
output.write('''
        </table>
        </html>
 ''')

output.close()