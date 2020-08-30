import datetime
import os

# Need to change these constants.
# --- URL ---
# IMDA
url = 'https://extract-dev.taiger.io'

# Sompo
# url = 'http://imatch-macquarie1.taiger.io:8080'
# url = 'http://168.63.244.231:8080'

# Do not change unless the iMatch is not a kubernetes deployment.
# Kubernetes deployment needs all the calls to be directed to /gateway instead of :8080
# host = url + 'gateway'
# For normal deployments;
host = url

# --- Credentials ---
username = 'lilik'
# password = 'Password123@' # Sompo
password = 'Password@123' # IMDA

# --- docType and subtype ---
docType = 'IMDA'
subType = 'SkillFuture'

# --- Accepted Formats ---
accepted_formats = ['png', 'pdf', 'jpg', 'tif']

# Change only if necessary
uploadURL = host + '/imatchpipelineexecutor/api/v2/selector/'
resourceURL = host + '/imatchresourcemanager/api/resource/'
pipelineURL = host + '/imatchpipelineexecutor/api/v2/selector/'
role = 'ROLE_TAIGER'
countryName = 'Singapore'
languageCode = 'ENGLISH'
mobile = 'false'
normalize = 'false'
signature = 'false'
checkbox = 'false'
usergroupId = '1'
randAlphaNum = "o5l5l5c2ta"
webSocketSessionId = username + role + randAlphaNum

d = datetime.datetime.today()
uploadId = '\"Documents_{0:0=2d}/{1:0=2d}/{2:0=4d}-{3:0=2d}:{4:0=2d}:{5:0=2d}\"'.format(d.month,
                                                                                        d.day,
                                                                                        d.year,
                                                                                        d.hour,
                                                                                        d.minute,
                                                                                        d.second)

upload_json = '"usergroupId":{0},"docType":"{1}","subType":"{2}","countryName":"{3}","languageCode":"{4}",' \
              '"mobile":{5},"normalize":{6},"signature":{7},"checkbox":{8},"uploadId":{9}'.format(usergroupId,
                                                                                                  docType,
                                                                                                  subType,
                                                                                                  countryName,
                                                                                                  languageCode,
                                                                                                  mobile,
                                                                                                  normalize,
                                                                                                  signature,
                                                                                                  checkbox,
                                                                                                  uploadId)

upload_json = "{" + upload_json + "}"

# Folder path and Gold csv path
folder_to_process = os.getcwd() + "/test/"

# --- Gold Data Path
# gold_csv_path = folder_to_process + "GOLD.csv"
