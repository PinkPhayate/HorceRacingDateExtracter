# coding: UTF-8
import requests
from bs4 import BeautifulSoup
import json
import csv
import types
import inspect
def location(depth=0):
    frame = inspect.currentframe(depth+1)
    return (frame.f_code.co_filename, frame.f_lineno)

def pageSrc (url):
    f = open('./text.txt', 'w')

    # type(r)   =>  response
    r = requests.get(url)

    # operate below, unable to encode('utf-8')
    r.encoding = r.apparent_encoding
    html_src = r.text.encode('utf-8')
    # print html_src

    # file write
    f = open('./text.txt', 'w')
    f.write(html_src)
    f.close()

    return html_src

def scraping(html_src, output_name):
    soup = BeautifulSoup(html_src, 'html.parser')
    result_table = soup.find(class_='race_result fc')
    # print result_table
    writecsv = csv.writer(file(output_name, 'ab'), lineterminator='n')
    table_list = []
    for tr in result_table.findAll('tr',''):
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
        print location(); print table_low
        if len(table_low) != 0 :
            print location();
            table_list.append(table_low)
            # print table_low;

    writecsv.writerow(table_list)
    file.close

if __name__ == '__main__':
    url = 'http://race.netkeiba.com/?pid=race&id=c201605010411&mode=result'
    output_file = '201605010411.csv'

    html_src = pageSrc(url)
    html_doc = scraping(html_src, output_file)
