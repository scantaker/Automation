from typing import Optional
from config import subType, host, username, password, resourceURL, webSocketSessionId, upload_json, uploadURL, \
    accepted_formats, folder_to_process
from xlsxwriter.utility import xl_range, xl_rowcol_to_cell
from xlsxwriter.worksheet import (
    Worksheet, cell_number_tuple, cell_string_tuple)
import requests
import json
import os
import time
import pandas as pd
import datetime
import xlsxwriter


# ---- Uploading documents to iMatch and get extracted data points ----
def authenticate(auth_url, auth_username, auth_password):
    """
    Authenticate to iMatch
    :param auth_url: Host URL
    :param auth_username: Configured in config.py
    :param auth_password: auth_username: Configured in config.py
    :return: Bearer Token if successful authentication. Or else Boolean False.
    """
    auth_url = auth_url + "/api/authenticate"
    payload = ""

    headers = {
        'Content-Type': "application/json",
        'username': auth_username,
        'password': auth_password,
        'Accept': "*/*",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "0",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    return_value = False

    try:
        authenticate_tries_counter = 0
        while authenticate_tries_counter < 5:
            authenticate_tries_counter = authenticate_tries_counter + 1
            response = requests.request("POST", auth_url, data=payload, headers=headers)
            if response.status_code == 200:
                return_value = json.loads(response.content)['id_token']
                authenticate_tries_counter = authenticate_tries_counter + 6
            else:
                time.sleep(3)
    except ConnectionError:
        pass

    return return_value


if authenticate(auth_url=host, auth_username=username, auth_password=password):
    authorization_token = "Bearer " + authenticate(auth_url=host, auth_username=username, auth_password=password)
else:
    authorization_token = False


def get_processed_file_data(file_id, resource_url=resourceURL):
    """
    :param file_id: File ID
    :param resource_url: iMatch Resource URL
    :return: returns file response
    """
    headers = {'Authorization': authorization_token}
    resource_url = resource_url + file_id
    print("File is in Pipeline")
    while True:
        time.sleep(1)
        file_response = requests.get(resource_url, headers=headers)
        if file_response.json()['textPlain'] is not None:
            break

    print("File is processed")
    return file_response.json()


def upload_file(file):
    """
    :param file: file id from iMatch
    :return:
    """
    if authorization_token:
        headers = {'Authorization': authorization_token}

        files = {
            'file': file,
            'webSocketSessionId': webSocketSessionId,
            'json': upload_json,
        }
        response = requests.post(uploadURL, headers=headers, files=files)

        return response.content
    else:
        print("Authentication Failed")
        return False


# Get first file and store the data
def get_data_labels(file_dir):
    image_test = open(file_dir, 'rb')
    upload_response = upload_file(image_test)
    print(json.loads(upload_response))
    counter = 0
    while "error" in json.loads(upload_response):
        print("Retrying")
        time.sleep(1)
        counter = counter + 1
        upload_response = upload_file(image_test)
        if counter > 5:
            upload_response = False
            print("Retired 5 times. Skipping the file for now")
            break

    file_id = json.loads(upload_response)['identifier']
    file_data = get_processed_file_data(file_id, resourceURL)
    list_of_datapoint_names = ['file_name', 'imatch_id']

    data = file_data['sections'][0]['attributes']
    for j in range(len(data)):
        list_of_datapoint_names.append(data[j]['key'])

    for keys in file_data['sections'][0]:
        if keys == "children":
            data = file_data['sections'][0][keys]
            for i in range(len(data)):
                attributes = data[i]['attributes']
                for j in range(len(attributes)):
                    list_of_datapoint_names.append(attributes[j]['key'])

    return {datapoint_name: None for datapoint_name in list_of_datapoint_names}


def process_folder(path):
    """
    :param path: Process the folder
    :return: None
    """
    os.chdir(path)
    os.makedirs(os.getcwd() + '/html_output', exist_ok=True)
    completed = ['.'.join(i.split('.')[:-1]) for i in os.listdir(os.getcwd() + '/html_output')]
    images = [im for im in os.listdir() if im.split('.')[-1] in accepted_formats]

    if images:
        first_file = images[0]
        file_path = os.getcwd() + '/' + first_file
        data_dict_template = get_data_labels(file_path)
        file_info = pd.DataFrame(columns=[keys for keys in data_dict_template.keys()])
        number_of_images = 0

        for image in images:
            number_of_images = number_of_images + 1
            if '.'.join(image.split('.')[:-1]) in completed:
                print('Skipped', image)
                continue
            else:
                print("Processing the {}".format(image))
                image_bin = open(image, 'rb')
                upload_response = upload_file(image_bin)

                counter = 0
                while "error" in json.loads(upload_response):
                    print("Retrying")
                    counter = counter + 1
                    upload_response = upload_file(image)
                    if counter > 5:
                        upload_response = False
                        print("Retired 5 times. Skipping the file for now")
                        break

                if upload_response:
                    file_id = json.loads(upload_response)['identifier']
                    file_data = get_processed_file_data(file_id, resourceURL)
                    with open(os.getcwd() + '/html_output/'
                              + '.'.join(image.split('.')[:-1]) + '.html', 'w', encoding='utf-8') as f:
                        f.write(file_data['textPlain']['ENGLISH'])

                    data_dict_template['file_name'] = file_data['information']['fileName']
                    data_dict_template['imatch_id'] = file_data['id']
                    data = file_data['sections'][0]['attributes']

                    for j in range(len(data)):
                        # this loop is used to obtain data point if the
                        # data is not hidden under a drop down menu
                        # in iMatch UI
                        key = data[j]['key']
                        value = data[j]['values'][0]['originalValue']
                        data_dict_template[key] = value

                    for keys in file_data['sections'][0]:
                        # this loop is used to obtain data point if the
                        # data is hidden under a drop down menu in
                        # iMatch UI
                        if keys == "children":
                            data = file_data['sections'][0][keys]
                            if len(data) != 0:
                                # this conditional will run when there is
                                # a data point with multiple data values
                                for sub_key in data[0]:
                                    if sub_key == 'children':
                                        sub_data = data[0][sub_key]
                                        for index in range(len(sub_data)):
                                            sub_data_attributes = sub_data[index]['attributes']
                                            for j in range(len(sub_data_attributes)):
                                                key = sub_data_attributes[j]['key'] + '_' + str(index+1)
                                                if key not in file_info.columns.tolist():
                                                    file_info[key] = ""
                                                value = sub_data_attributes[j]['values'][0]['originalValue']
                                                data_dict_template[key] = value

                            for i in range(len(data)):
                                attributes = data[i]['attributes']
                                for j in range(len(attributes)):
                                    key = attributes[j]['key']
                                    value = attributes[j]['values'][0]['originalValue']
                                    data_dict_template[key] = value

            file_info.loc[number_of_images] = [values for values in data_dict_template.values()]
            # this loop will flush out the dictionary for every documents uploaded
            for key in data_dict_template.keys():
                data_dict_template[key] = ""

        d = datetime.datetime.today()
        now = '{0:0=2d}_{1:0=2d}_{2:0=4d}-{3:0=2d}_{4:0=2d}_{5:0=2d}'.format(d.month,
                                                                             d.day,
                                                                             d.year,
                                                                             d.hour,
                                                                             d.minute,
                                                                             d.second)

        out_file_name = now + "_output.csv"
        file_info.to_csv(out_file_name, index=False)
        file_info = file_info.drop("imatch_id", axis=1)
        out_file_name = "compare" + out_file_name
        file_info.to_csv(out_file_name, index=False)
        print("All files are processed")
        return out_file_name


file_name = process_folder(folder_to_process)

# ----- Generating Accuracy Report -----
# subType header strings
subtype_header = ["Document Name", "Data Point Name",
                  "Expect Data", "Extract Data",
                  "Total", "Partial",
                  "Noisy", "Correct"]

# Document accuracy header strings
doc_accuracy_header = ["Document Name", "Total",
                       "Partial", "Noisy",
                       "Correct", "Accuracy % with Noise",
                       "Accuracy % without Noise", "Accuracy % with Partial Correct"]

# Data point accuracy header strings
data_point_accuracy_header = ["Data Point Name", "Total",
                              "Partial", "Noisy",
                              "Correct", "Accuracy % with Noise",
                              "Accuracy % without Noise", "Accuracy % with Partial Correct"]

# File that will be used to generate accuracy report
extracted_file_path = folder_to_process + file_name + ".csv"

# Read CSV files into data frames
compare_data = pd.read_csv(file_name, dtype=str)

# Fill any missing values
df1 = compare_data.fillna("")

# Creating data points list
data_point_list = list(df1.columns)
data_point_list.pop(0)

# Creating empty dictionary for each data points that will be used
# for data point accuracy sheet
total_dict = {}
partial_dict = {}
noisy_dict = {}
correct_dict = {}

# Adding a key of each data points with value of an empty list that will be
# filled with respective cells of the data points to all created dictionaries
for data_point in data_point_list:
    total_dict[data_point] = []
    partial_dict[data_point] = []
    noisy_dict[data_point] = []
    correct_dict[data_point] = []

# --- Functions ---
# Function to add cells to each data point list within each dictionaries
def add_cells_to_dict(dicts_list, dp_row_index, dp_column_index):
    dicts_list.append(xl_rowcol_to_cell(dp_row_index, dp_column_index))

# Borrowed function from karolyi at Stackoverflow to get column width
def get_column_width(worksheet: Worksheet, column: int) -> Optional[int]:
    """Get the max column width in a `Worksheet` column."""
    strings = getattr(worksheet, '_ts_all_strings', None)
    if strings is None:
        strings = worksheet._ts_all_strings = sorted(
            worksheet.str_table.string_table,
            key=worksheet.str_table.string_table.__getitem__)
    lengths = set()
    for row_id, colums_dict in worksheet.table.items():  # type: int, dict
        data = colums_dict.get(column)
        if not data:
            continue
        if type(data) is cell_string_tuple:
            iter_length = len(strings[data.string])
            if not iter_length:
                continue
            lengths.add(iter_length)
            continue
        if type(data) is cell_number_tuple:
            iter_length = len(str(data.number))
            if not iter_length:
                continue
            lengths.add(iter_length)
    if not lengths:
        return None
    return max(lengths)

# Borrowed function from karolyi at Stackoverflow to set column autowidth
def set_column_autowidth(worksheet: Worksheet, column: int):
    """
    Set the width automatically on a column in the `Worksheet`.
    !!! Make sure you run this function AFTER having all cells filled in
    the worksheet!
    """
    maxwidth = get_column_width(worksheet=worksheet, column=column)
    if maxwidth is None:
        return
    worksheet.set_column(first_col=column, last_col=column, width=(maxwidth * 1.3))
# --- ---

# Create a workbook and add a worksheet.
sheet_name = subType + "_Accuracy_Report.xlsx"
workbook = xlsxwriter.Workbook(sheet_name)
worksheet1 = workbook.add_worksheet(subType)
worksheet2 = workbook.add_worksheet("Document Accuracy")
worksheet3 = workbook.add_worksheet("Data Point Accuracy")
worksheet_list = [worksheet1, worksheet2, worksheet3]

# --- Formatting ---
bold = workbook.add_format({'bold': True,
                            'bg_color': '#DDDDDD',
                            'border': 1,
                            'font_size': 14,
                            'align': 'center'})

# Row and column index
row_index = 0
col_index = 0

# Creating header for each worksheet
for worksheet in worksheet_list:
    if worksheet == worksheet1:
        for header in subtype_header:
            worksheet.write(0, col_index, header, bold)
            col_index += 1
        col_index = 0
    if worksheet == worksheet2:
        for header in doc_accuracy_header:
            worksheet.write(0, col_index, header, bold)
            col_index += 1
        col_index = 0
    if worksheet == worksheet3:
        for header in data_point_accuracy_header:
            worksheet.write(0, col_index, header, bold)
            col_index += 1
        col_index = 0

# --- subType Sheet ---
doc_name_cell_list = []
dp_count_cell_list = []

# -- Writing all document name to column A --
subtype_doc_name_row_index = 1
subtype_doc_name_list = df1['file_name'].tolist()
data_point_len = len(data_point_list) + 1

for doc_name in subtype_doc_name_list:
    worksheet1.write(subtype_doc_name_row_index, 0, doc_name)
    doc_name_cell_list.append(xl_rowcol_to_cell(subtype_doc_name_row_index, 0))
    subtype_doc_name_row_index += data_point_len

# -- Writing all data points to column B --
subtype_data_point_row_index = 2
for i in range(0, len(subtype_doc_name_list)):
    for data_point in data_point_list:
        worksheet1.write(subtype_data_point_row_index, 1, data_point)
        # Add cells of respective total, partial, correct, and
        # noisy to dictionary list
        total_list = total_dict[data_point]
        partial_list = partial_dict[data_point]
        correct_list = correct_dict[data_point]
        noisy_list = noisy_dict[data_point]
        add_cells_to_dict(total_list, subtype_data_point_row_index, 4)
        add_cells_to_dict(partial_list, subtype_data_point_row_index, 5)
        add_cells_to_dict(correct_list, subtype_data_point_row_index, 6)
        add_cells_to_dict(noisy_list, subtype_data_point_row_index, 7)
        subtype_data_point_row_index += 1
    subtype_data_point_row_index += 1

# -- Writing all extracted data to column D --
subtype_extracted_data_row_index = 2
output_transpose = df1.drop(['file_name'], axis=1).T.rename_axis('Datapoint Name')
column_name = []
for i in range(0, len(output_transpose.columns)):
    column_name.append(str(i))
output_transpose.columns = column_name
extracted_data_df = output_transpose
for name in column_name:
    extracted_data_list = extracted_data_df[name].tolist()
    for extracted_data in extracted_data_list:
        worksheet1.write(subtype_extracted_data_row_index, 3, extracted_data)
        subtype_extracted_data_row_index += 1
    subtype_extracted_data_row_index += 1

# -- Writing all data points formula to column E, F, G, H --
subtype_formula_column_index_list = [4, 5, 6, 7]
temp_dict = {}
for i in subtype_formula_column_index_list:
    subtype_formula_row_index = 1
    range_start_index = 2
    temp_dict[i] = []
    temp_list = temp_dict[i]
    for j in range(0, len(subtype_doc_name_list)):
        range_end_index = range_start_index + len(data_point_list) - 1
        data_point_range = xl_range(range_start_index, i, range_end_index, i)
        worksheet1.write(subtype_formula_row_index, i, '=SUM(' + data_point_range + ')')
        temp_list.append(xl_rowcol_to_cell(subtype_formula_row_index, i))
        range_start_index += len(data_point_list) + 1
        subtype_formula_row_index += len(data_point_list) + 1
    dp_count_cell_list.append(temp_dict[i])

# Set columns autowidth
for i, header in enumerate(subtype_header):
    set_column_autowidth(worksheet1, i)

# --- Document Accuracy ---
# -- Writing all document names to column A --
# -- based on document name on subType sheet --
doc_accuracy_doc_name_row_index = 1
for doc in subtype_doc_name_list:
    worksheet2.write(doc_accuracy_doc_name_row_index, 0, doc)
    doc_accuracy_doc_name_row_index += 1

# -- Writing all data point flags to column B, C, D, E --
dp_count_column_index_list = [1, 2, 3, 4]
temp_dict = {}
for i in range(0, len(dp_count_column_index_list)):
    temp_dict[dp_count_column_index_list[i]] = dp_count_cell_list[i]

for i in dp_count_column_index_list:
    dp_count_row_index = 1
    for dp_count in temp_dict[i]:
        worksheet2.write(dp_count_row_index, i, '=' + subType + '!' + dp_count)
        dp_count_row_index += 1

# -- Writing accuracy formula to column G, H, I --
def accuracy_score(work_sheet, cell_list):
    # Creating 0.00% cell format
    cell_format = workbook.add_format()
    cell_format.set_num_format(10)

    formula_row_index = 1
    for index in range(0, len(cell_list)):
        correct_cell = xl_rowcol_to_cell(formula_row_index, 4)
        noise_cell = xl_rowcol_to_cell(formula_row_index, 3)
        partial_cell = xl_rowcol_to_cell(formula_row_index, 2)
        total_cell = xl_rowcol_to_cell(formula_row_index, 1)
        work_sheet.write(formula_row_index, 5,
                         '=' + correct_cell + '/' + total_cell, cell_format)
        work_sheet.write(formula_row_index, 6,
                         '=' + correct_cell + '/(' + total_cell + '-' + noise_cell + ')',
                         cell_format)
        work_sheet.write(formula_row_index, 7,
                         '=(' + correct_cell + '+(' + partial_cell + '*0.5))/' + total_cell,
                         cell_format)
        formula_row_index += 1

accuracy_score(worksheet2, doc_name_cell_list)

# Set columns autowidth
for i, header in enumerate(doc_accuracy_header):
    set_column_autowidth(worksheet2, i)

# --- Document Accuracy ---
# -- Writing all data points names to column A --
dp_accuracy_dp_name_row_index = 1
for data_point in data_point_list:
    worksheet3.write(dp_accuracy_dp_name_row_index, 0, data_point)
    dp_accuracy_dp_name_row_index += 1

# -- Writing the summation of each data points to column B, C, D, E
def summation_string(string_list):
    sum_string = '=SUM('
    for string in string_list:
        if string != string_list[-1]:
            sum_string += subType + '!' + string + ','
        else:
            sum_string += subType + '!' + string + ')'
    return sum_string

dp_accuracy_row_index = 1
for data_point in data_point_list:
    dict_list = [total_dict[data_point], partial_dict[data_point], correct_dict[data_point], noisy_dict[data_point]]
    dp_accuracy_column_index_list = [1, 2, 3, 4]
    for column_index in dp_accuracy_column_index_list:

        worksheet3.write(dp_accuracy_row_index, column_index, summation_string(dict_list[(column_index - 1)]))
    dp_accuracy_row_index += 1

# -- Writing accuracy formula to column G, H, I --
accuracy_score(worksheet3, data_point_list)

# Set columns autowidth
for i, header in enumerate(data_point_accuracy_header):
    set_column_autowidth(worksheet3, i)

workbook.close()
