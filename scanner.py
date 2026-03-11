import argparse
import nmap
import json
from datetime import datetime

def scan_network(network, ports):

    scanner = nmap.PortScanner()

    print(f"\nEscaneando red {network}...\n")

    scanner.scan(hosts=network, arguments=f"-p {ports}")

    results = []

    for host in scanner.all_hosts():

        host_info = {
            "ip": host,
            "estado": scanner[host].state(),
            "puertos": []
        }

        if "tcp" in scanner[host]:

            for port in scanner[host]["tcp"]:

                port_info = {
                    "puerto": port,
                    "estado": scanner[host]["tcp"][port]["state"],
                    "servicio": scanner[host]["tcp"][port]["name"]
                }

                host_info["puertos"].append(port_info)

        results.append(host_info)

        print(f"Host: {host} | Estado: {scanner[host].state()}")

        for p in host_info["puertos"]:
            print(f"  Puerto {p['puerto']} -> {p['estado']} ({p['servicio']})")

    return results


def save_report(data):

    date = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"reports/network_report_{date}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"\nReporte guardado en {filename}")


def main():

    parser = argparse.ArgumentParser(description="Network Scanner")

    parser.add_argument(
        "-t",
        "--target",
        default="192.168.1.0/24",
        help="Red objetivo"
    )

    parser.add_argument(
        "-p",
        "--ports",
        default="22,80,443,445,8080",
        help="Puertos a escanear"
    )

    args = parser.parse_args()

    data = scan_network(args.target, args.ports)

    save_report(data)


if _name_ == "_main_":
    main()
