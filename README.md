# FortiGate_IPv4_policy_check
Basic security policy check

1) Run "show firewall policy" in Fortigate command line & export it to .txt file.
2) Open in notepad++ and press Shift+Tab untill every line in the starting point.
3) Run Fortigate_policy_check.py like this --> all_objects_sum(every_rule=read_output_list(ipv4_policy="exportedFileFromFortiCLI.txt"))

For now it will only check broad configuration that are using object "All" in Source, Destination & Service fields.
Later will add more features, or do it yourself :)
