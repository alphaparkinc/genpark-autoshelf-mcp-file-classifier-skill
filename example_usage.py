from client import AutoShelfMcpFileClassifierClient
client = AutoShelfMcpFileClassifierClient()
print(client.classify_file("invoice_450.pdf", "Total cost: $450"))