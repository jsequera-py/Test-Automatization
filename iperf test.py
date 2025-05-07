
import iperf3

#iperf3 -c speedtest.dal13.us.leaseweb.net -p 5201-5210

client = iperf3.Client()
client.server_hostname = 'speedtest.dal13.us.leaseweb.net'
client.port = 5202
client.json_output = False
result = client.run()