# Open IPv4 policy config file in Notepad++
# 1) - tab all the config file to 0 point
# 2) Replace 'edit' word with -> rule\nedit
# which is just adding new line called 'rule' before the 'edit' line.

def read_output_list(ipv4_policy: str):
    printing = False
    rule_list = list()

    with open(ipv4_policy, 'r') as f:
        for line in f:
            if line.startswith('rule'):
                printing = True
                continue # go to next line
            elif line.startswith('next'):
                printing = False

            if printing:
                rule_list.append(line)
            if printing is False:
                rule_list.append('!')

    new = ''.join(rule_list)
    new = new.split('!')
    return new


def all_objects_sum(every_rule: list):

    objects = ['set srcaddr "all"',
               'set dstaddr "all"',
               'set service "ALL"',
               'edit',
               'set action accept',
               'set status disable',
               '"SMB"',
               '"FTP"',
               '"TELNET"',
]

    srcdstsrv_list = list()
    srcdst_list = list()
    srcsrv_list = list()
    dstsrv_list = list()
    src_list = list()
    dst_list = list()
    srv_list = list()

    disabled_rules_list = list()

    smb_list = list()
    ftp_list = list()
    telnet_list = list()

    for l in sorted(every_rule):
        if objects[3] in l:
            
            # Assign variable to rule ID's
            rule_num = l.split(" ")[1].rstrip("\nset")

            # Check for "All" object in Source, Destination and Service fields
            if l.__contains__(objects[0]) and l.__contains__(objects[1]) and l.__contains__(objects[2]) and l.__contains__(objects[4]):
                if not l.__contains__(objects[5]):
                    srcdstsrv_list.append(rule_num)
                    # with open(f"All object in Source, Destination and Service fields.txt", "a") as srcdstsrv:
                    #     srcdstsrv.writelines(l)
                        # print("edit", rule_num)

            # Check for "All" object in Source and Destination fields
            if l.__contains__(objects[0]) and l.__contains__(objects[1]) and l.__contains__(objects[4]):
                if not l.__contains__(objects[5]):
                    if not l.__contains__(objects[2]):
                        srcdst_list.append(rule_num)
                        # with open("All object in Source & Destination fields.txt", "a") as srcdst:
                        # srcdst.writelines(l)
                        # print(rule_num)

            # Check for "All" object in Source and Service fields
            if l.__contains__(objects[0]) and  l.__contains__(objects[2]) and l.__contains__(objects[4]):
                if not l.__contains__(objects[5]):
                    if not l.__contains__(objects[1]):
                        srcsrv_list.append(rule_num)
                        # with open("All object in Source and Service fields.txt", "a") as srcsrv:
                            # srcsrv.writelines(l)
                            # print(rule_num)

            # Check for "All" object in Destination and Service fields
            if l.__contains__(objects[1]) and l.__contains__(objects[2]) and l.__contains__(objects[4]):
                if not l.__contains__(objects[5]):
                    if not l.__contains__(objects[0]):
                        dstsrv_list.append(rule_num)
                        # with open("All object in Destination and Service fields.txt", "a") as dstsrv:
                            # dstsrv.writelines(l)
                            # print(rule_num)

            # Check for "All" object in Destination field
            if l.__contains__(objects[1]) and l.__contains__(objects[4]):
                if not l.__contains__(objects[5]):
                    if not l.__contains__(objects[0]):
                        if not l.__contains__(objects[2]):
                            dst_list.append(rule_num)
                            # with open("All object in Destination field.txt", "a") as dst:
                                # dst.writelines(l)
                                # print(rule_num)

            # Check for "All" object in Source field
            if l.__contains__(objects[0]) and l.__contains__(objects[4]):
                if not l.__contains__(objects[5]):
                    if not l.__contains__(objects[1]):
                        if not l.__contains__(objects[2]):
                            src_list.append(rule_num)
                            # with open("All object in Source field.txt", "a") as src:
                                # src.writelines(l)
                                # print(rule_num)

            # Check for "All" object in Service field
            if l.__contains__(objects[2]) and l.__contains__(objects[4]):
                if not l.__contains__(objects[5]):
                    if not l.__contains__(objects[0]):
                        if not l.__contains__(objects[1]):
                            srv_list.append(rule_num)
                            # with open("All object in Service field.txt", "a") as srv:
                                # srv.writelines(l)
                                # print(rule_num)

            # Check for Disabled policies                    
            if l.__contains__(objects[5]):
                disabled_rules_list.append(rule_num)
                # with open("Disabled rules.txt", "a") as dis:
                #     dis.writelines(l)
                
            # Check for potentially Un-safe protocols
            if l.__contains__(objects[6]):
                smb_list.append(rule_num)
                # with open("Un-safe protocols.txt", "a") as un_safe:
                #     un_safe.writelines(l)

            if l.__contains__(objects[7]):
                ftp_list.append(rule_num)
                # with open("Un-safe protocols.txt", "a") as un_safe:
                #     un_safe.writelines(l)

            if l.__contains__(objects[8]):
                telnet_list.append(rule_num)
                # with open("Un-safe protocols.txt", "a") as un_safe:
                #     un_safe.writelines(l)

    with open('Summary.txt', 'a') as summary:        
        summary.write(f"All object in Source, Destination & Service fields\nRules in total: {len(srcdstsrv_list)}\nRules ID's: {srcdstsrv_list}\n\n")
        summary.write(f"All object in Source & Destination fields\nRules in total: {len(srcdst_list)}\nRules ID's: {srcdst_list}\n\n")
        summary.write(f"All object in Source & Service fields\nRules in total: {len(srcsrv_list)}\nRules ID's: {srcsrv_list}\n\n")
        summary.write(f"All object in Destination & Service fields\nRules in total: {len(dstsrv_list)}\nRules ID's: {dstsrv_list}\n\n")
        summary.write(f"All object in Source field\nRules in total: {len(src_list)}\nRules ID's: {src_list}\n\n")
        summary.write(f"All object in Destination field\nRules in total: {len(dst_list)}\nRules ID's: {dst_list}\n\n")
        summary.write(f"All object in Service field\nRules in total: {len(srv_list)}\nRules ID's: {srv_list}\n\n")
        summary.write(f"Disabled Rules\nRules in total: {len(disabled_rules_list)}\nRules ID's: {disabled_rules_list}\n\n")
        summary.write(f"SMB presents in rules\nRules in total: {len(smb_list)}\nRules ID's: {smb_list}\n\n")
        summary.write(f"FTP presents in rules\nRules in total: {len(ftp_list)}\nRules ID's: {ftp_list}\n\n")
        summary.write(f"TELNET presents in rules\nRules in total: {len(telnet_list)}\nRules ID's: {telnet_list}\n\n")


all_objects_sum(every_rule=read_output_list(ipv4_policy="firewallPolicy.txt"))
