import os

path = '/Users/zhangsicai/Desktop/Taiger/Projects/Tender/SkillsCSVs/'
files = os.listdir(path)
s = []
for file in files:
    with open(path+"/"+file, encoding='utf-8') as f:
        filecontent=f.read()
        s.append(filecontent)

#for scontent in s:
 #   skill = scontent.split('|')
  #  s1.append(skill)
s1=str(s)
print(str(s))


skillpath = '/Users/zhangsicai/Desktop/Extractedskills/'
matchedskillsfiles = os.listdir(skillpath)
matchedskills = []

allfiles_allskill_count =0
allfiles_allmatch_count = 0
file_count = 0

for matchedskillsfile in matchedskillsfiles:
    with open(skillpath+"/"+matchedskillsfile, "r") as f:
        popdatas = json.load(f)
        #popdatas['matchedSkills']
        allskills = popdatas['matchedSkills']

        allskill_count = len(allskills)
        allfiles_allskill_count += allskill_count

        ##count number of matched skills if it can be found in the database
        count_match = 0
        for allskill in allskills:
            if allskill in s1:
                count_match +=1
                #print(allskill + 'is in')

            else:
                print(allskill + "is not in")
        allfiles_allmatch_count += count_match
        file_count += 1
        try:
            fileaccuracy = count_match / allskill_count
        except ZeroDivisionError:
            print('matched skills set list is empty')

        print('file'+str(file_count)+'matched skills accuracy is:', '%.2f%%' % (fileaccuracy*100))

overallaccuracy = allfiles_allmatch_count/allfiles_allskill_count
print('overall accuracy is:', '%.2f%%' % (overallaccuracy*100))