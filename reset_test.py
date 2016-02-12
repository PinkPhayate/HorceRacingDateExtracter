# coding: EUC-JP
# coding: UTF-8

import requests
from bs4 import BeautifulSoup
import json
import csv
import types

def pageSrc (url):
    r = requests.get(url)
    str_code = r.encoding
    # print str_code
    html_doc = r.text.encode(r.encoding)
    # print html_doc
    return html_doc

    # extract table data


def scraping(html_doc, output_name):
    soup = BeautifulSoup(html_doc, 'html.parser')
    result_table = soup.find(class_='race_result fc')

    writecsv = csv.writer(file(output_name, 'ab'), lineterminator='n')

    table_list = []
    for tr in result_table.findAll('tr'):

        table_low = []
        for td in tr.findAll('td'):
            # remove 'a' tag
            content = td.a
            if content != None:
                content = td.a.string
                table_low.append(content)
            else :
                content = td.span
                if content != None:
                    content = td.span.string
                    # print content
                    table_low.append(content)

                else:
                    content = td.renderContents()
                    # print content
                    table_low.append(content)
        print table_low + '\n'

        # table_list.append(table_low)
        # print table_low
    writecsv.writerow(table_list)
            # for a in td.findAll('a'):
            #     print a.renderContents()
            # print td.get_text

            # data = td.renderContents()
            # table_low.append(td)
    file.close

if __name__ == '__main__':
    url = 'http://race.netkeiba.com/?pid=race&id=c201605010411&mode=result'
    html_doc = pageSrc(url)
    scraping( html_doc, './201605010411.csv')
