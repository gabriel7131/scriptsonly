''' for python 3 reqires for of textFSM avialable at https://github.com/jonathanslenders/textfsm
 Copyright 2016 Hewlett Packard Enterprise Development LP.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.'''
import jtextfsm as textfsm
import json


vlan = '''Brief information about all VLANs:
Supported Minimum VLAN ID: 1
Supported Maximum VLAN ID: 4094
Default VLAN ID: 1
VLAN ID   Name                             Port
1         VLAN 0001                        FGE1/0/1  FGE1/0/2  FGE1/0/3
                                           FGE1/0/4  FGE1/0/5  FGE1/0/6
                                           FGE1/0/7  FGE1/0/8  FGE1/0/9
                                           FGE1/0/10  FGE1/0/11  FGE1/0/12
                                           FGE1/0/13  FGE1/0/14  FGE1/0/15
                                           FGE1/0/16  FGE1/0/17  FGE1/0/18
                                           FGE1/0/19  FGE1/0/20  FGE1/0/22
                                           FGE1/0/23  FGE1/0/24  FGE1/0/25
                                           FGE1/0/26  FGE1/0/27  FGE1/0/28
                                           FGE1/0/29  FGE1/0/30  FGE1/0/31
                                           FGE1/0/32
10        VLAN 0010                        FGE1/0/21
20        VLAN 0020
30        VLAN 0030
200       VLAN 0200
500       VLAN 0500'''


# Run the text through the FSM.
# The argument 'template' is a file handle and 'raw_text_data' is a
# string with the content from the show_inventory.txt file
template = open("./templates/displayvlanbrief.textfsm")
re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(vlan)



print (json.dumps(fsm_results, indent=4))
