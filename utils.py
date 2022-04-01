import os.path
import pandas as pd


def create_path(site) -> str:
    if not os.path.isdir(f"files/{site}"):
        os.mkdir(f"files/{site}")
        path = f"files/{site}"
    else:
        path = f"files/{site}"
    return path


def get_data_dataframe(all_data):
    frame = {
        "cpu_vcpus": [],
        "memory": [],
        "storage_ssd_disk": [],
        "bandwith_transfer": [],
        "price_by_month": [],
    }
    for line_data in all_data:
        frame["cpu_vcpus"].append(line_data[0])
        frame["memory"].append(line_data[1])
        frame["storage_ssd_disk"].append(line_data[2])
        frame["bandwith_transfer"].append(line_data[3])
        frame["price_by_month"].append(line_data[4])
        df = pd.DataFrame(frame)
    return df


def get_data_cmd(all_data) -> None:
    df = get_data_dataframe(all_data)
    print(df)


def save_data_csv(all_data, site) -> None:
    df = get_data_dataframe(all_data)
    path = create_path(site)
    df.to_csv(
        f"{path}/data_csv.csv",
        index=False,
        sep=";",
        encoding="utf-8",
        header="true",
    )
    print(df)
    print("O arquivo csv foi salvo na pasta files, verifique-o!")


def save_data_json(all_data, site) -> None:
    df = get_data_dataframe(all_data)
    out = df.to_json(force_ascii=False, orient="records")[1:-1].replace("} {", "},{")
    path = create_path(site)
    with open(f"{path}/data_json.json", "w", encoding="utf-8") as f:
        f.write(out)
    print(df)
    print("O arquivo json foi salvo na pasta files, verifique-o!")
