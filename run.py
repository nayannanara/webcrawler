import argparse

from vultr import WebCrawlerVultr as vt
from digitalocean import WebCrawlerDigitalOcean as do
from utils import get_data_cmd, save_data_csv, save_data_json


class WebCrawler:
    def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("--site", help="[vultr/digitalocean]", required=True)
        parser.add_argument("--output", help="[cmd/csv/json]", required=True)

        args = parser.parse_args()

        site = args.site.lower()
        output = args.output.lower()
        if site in ["vultr", "digitalocean"] and output in ["cmd", "csv", "json"]:
            all_data = vt.get_data() if site == "vultr" else do.get_data()
            if output == "cmd":
                get_data_cmd(all_data)
            elif output == "json":
                save_data_json(all_data, site)
            else:
                save_data_csv(all_data, args.site.lower())
        else:
            print("Opção inválida! Digite um site e um output válido")

    if __name__ == "__main__":
        main()
