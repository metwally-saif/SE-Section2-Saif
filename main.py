import csv
import json
import time
import requests


class WebPerformanceAnalyzer:
    def __init__(self, url, cycles):
        self.url = url
        self.cycles = cycles

    def fetch_page_load_times(self):
        page_load_times = []

        for _ in range(self.cycles):
            start_time = time.time()
            response = requests.get(self.url)
            end_time = time.time()

            if response.status_code == 200:
                page_load_times.append(end_time - start_time)
                time.sleep(2)  # Pause for 2 seconds before next request

        return page_load_times


def save_as_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)


def save_as_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Load Time (s)'])

        for load_time in data:
            csv_writer.writerow([load_time])


def calculate_average_load_time(data):
    return sum(data) / len(data) if len(data) > 0 else 0


def main():
    website_url = "https://en.wikipedia.org/wiki/Software_metric"
    iterations = 10

    analyzer = WebPerformanceAnalyzer(website_url, iterations)
    page_load_times = analyzer.fetch_page_load_times()

    save_as_json(page_load_times, 'page_load_times.json')
    save_as_csv(page_load_times, 'page_load_times.csv')

    average_load_time = calculate_average_load_time(page_load_times)
    print(f"Average Page Load Time: {average_load_time:.4f} seconds")


if __name__ == '__main__':
    main()
