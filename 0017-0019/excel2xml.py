# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/11/3 上午11:40'

"""
将17-19题合并一起写
读取三个xls文件，然后写入三个xml文件中，每个xml文件以写入的xls文件名命名
"""
import os

from lxml import etree
import xlrd

xls_dir = "xls"
xml_dir = "xml"
files = os.listdir(xls_dir)


def readExcel(file):
    if "student" in file:
        file_path = os.path.join(xls_dir, file)
        wb = xlrd.open_workbook(file_path)
        sheet = wb.sheet_by_index(0)
        num_rows = sheet.nrows
        data = dict()
        for i in range(num_rows):
            data[str(sheet.row_values(i)[0])] = str(sheet.row_values(i)[1:])
    if "city" in file:
        file_path = os.path.join(xls_dir, file)
        wb = xlrd.open_workbook(file_path)
        sheet = wb.sheet_by_index(0)
        num_rows = sheet.nrows
        data = dict()
        for i in range(num_rows):
            data[str(sheet.row_values(i)[0])] = str(sheet.row_values(i)[1])
    if "numbers" in file:
        file_path = os.path.join(xls_dir, file)
        wb = xlrd.open_workbook(file_path)
        sheet = wb.sheet_by_index(0)
        num_rows = sheet.nrows
        data = list()
        for i in range(num_rows):
            data.append(sheet.row_values(i))
    return str(data)


def excel2xml(node_name, node_text):
    root = etree.Element('root')
    subnode = etree.SubElement(root, node_name)
    subnode.text = node_text
    tree = etree.ElementTree(root)
    xml_name = node_name + '.xml'
    if not os.path.exists(xml_dir):
        os.makedirs(xml_dir)
    xml_path = os.path.join(xml_dir, xml_name)
    tree.write(xml_path, pretty_print=True, xml_declaration=True, encoding='utf-8')


if __name__ == '__main__':
    for file in files:
        filename = os.path.splitext(file)[0]
        text = readExcel(file)
        excel2xml(filename, text)