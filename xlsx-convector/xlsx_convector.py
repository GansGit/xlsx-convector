#!/usr/bin/env python3

import pandas

def main():
    file_location = './forma_1_lyutiy_2020.xlsx' 

    xlsx = pandas.ExcelFile(file_location)
    print('success')


if __name__ == "__main__":
    main()

