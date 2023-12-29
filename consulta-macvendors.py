import requests

# Dicionário que mapeia endereços MAC a nomes
mac_to_name = {
    "mac":"nome cliente",
}

# Nome do arquivo de saída
output_file = "chb-6-14.txt"

with open(output_file, "w") as file:
    for mac_address in mac_to_name.keys(): 
        url = f"https://api.macvendors.com/{mac_address}"
        response = requests.get(url)

        if response.status_code == 200:
            vendor = response.text
            name = mac_to_name[mac_address]
            output_line = f"Name: {name}, MAC Address: {mac_address}, Vendor: {vendor}\n"
            file.write(output_line)
        else:
            output_line = f"MAC Address: {mac_address}, Not Found\n"
            file.write(output_line)

print(f"Resultados foram escritos em {output_file}")
