import requests
from bs4 import BeautifulSoup


class WebCrawlerDigitalOcean:
    def get_data():
        main_url = "https://web.archive.org/web/20210131084315/https://www.digitalocean.com/pricing/"
        page = requests.get(main_url)
        soup = BeautifulSoup(page.text, "html.parser")

        all_sections = soup.find_all(class_="css-8f57v9")
        data = None
        for section in all_sections:
            try:
                name_section = section.find(class_="e1id7d9a0")["id"].strip()
                if name_section == "basic-droplets":
                    results_section = section.find_all("tr")
                    results_section.pop(0)
                    all_data_section = []
                    data = [result.find_all("td") for result in results_section]
            except:
                pass

        for line in data:
            line_data = []
            line.pop(4)
            for data in line:
                if data.text:
                    line_data.append(data.text)
            (line_data[0], line_data[1], line_data[2], line_data[3],) = (
                line_data[1],
                line_data[0],
                line_data[3],
                line_data[2],
            )
            all_data_section.append(line_data)
        return all_data_section
