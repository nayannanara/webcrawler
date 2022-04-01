import requests
from bs4 import BeautifulSoup


class WebCrawlerVultr:
    def get_data():
        main_url = "https://www.vultr.com/pricing/"
        page = requests.get(main_url)
        soup = BeautifulSoup(page.text, "html.parser")

        cloud_ssd_section = soup.find(id="optimized-cloud-compute")
        subsection = cloud_ssd_section.find(id="general-purpose")
        all_data = []
        rows_content = subsection.find_all(class_="pt__row")

        for row in rows_content:
            line_data = []
            current_line = row.find_all(class_="pt__cell")
            for line in current_line:
                new_content = line.text.split()
                new_content.pop() if len(new_content) > 2 else new_content
                line = "".join(content for content in new_content)
                line_data.append(line)
            line_data.pop(-1)
            all_data.append(line_data)
        return all_data
