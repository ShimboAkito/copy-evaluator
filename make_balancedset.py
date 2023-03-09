import pandas as pd
from sklearn.model_selection import train_test_split
import os

max_num = 1613

output_dir = './data/balanced_dataset'
copira_path = './data/slogans.tsv'
award_score = {
    'None' : 0,
 'TCCクラブ賞' : 2,
 'TCCグランプリ':2,
 'TCC広告賞':2,
 'TCC最高賞':2,
 'TCC賞':2,
 'ノミネート':1,
 'ファイナリスト':1,
 '一般部門賞':2,
 '会長賞':2,
 '奨励賞':2,
 '審査委員長賞':2,
 '新人賞':1,
 '最高新人賞':2,
 '特別賞':2,
 '部門賞':2}


data_dict = {
    'text':[],
    'sector':[],
    'company':[],
    'score':[]
}

copira_set = set()

num_list = [0 for i in range(3)]

copira_df = pd.read_table(copira_path).dropna()
for i, row in copira_df.iterrows():
    text = row['short_copy'].strip('\n')
    sector = row['sector'].strip('\n')
    company = row['company'].strip('\n')
    if text in copira_set:
        continue
    else:
        if num_list[award_score[row['award']]] < max_num:
            num_list[award_score[row['award']]]+=1
            data_dict['text'].append(text)
            data_dict['sector'].append(sector)
            data_dict['company'].append(company)
            data_dict['score'].append(award_score[row['award']])
            copira_set.add(text)
data_df = pd.DataFrame(data_dict)
data_df = data_df.sample(frac=1)

print(data_df.isnull().sum())

train_set, test_set = train_test_split(data_df,shuffle=True, test_size=0.2)
test_set, dev_set = train_test_split(test_set, shuffle=True, test_size=0.5)

train_set_sector = train_set.copy()
dev_set_sector = dev_set.copy()
test_set_sector = test_set.copy()

train_set_company = train_set.copy()
dev_set_company = dev_set.copy()
test_set_company = test_set.copy()

train_set_sector_company = train_set.copy()
dev_set_sector_company = dev_set.copy()
test_set_sector_company = test_set.copy()

for i in range(len(train_set['text'])):
    text = train_set.iat[i, 0]
    sector = train_set.iat[i, 1]
    company = train_set.iat[i, 2]

    train_set_sector.iat[i, 0] = sector+'[SEP]'+text
    train_set_company.iat[i, 0] = company+'[SEP]'+text
    train_set_sector_company.iat[i, 0] = sector+'[SEP]'+company+'[SEP]'+text


for i in range(len(dev_set['text'])):
    text = dev_set.iat[i, 0]
    sector = dev_set.iat[i, 1]
    company = dev_set.iat[i, 2]

    dev_set_sector.iat[i, 0] = sector+'[SEP]'+text
    dev_set_company.iat[i, 0] = company+'[SEP]'+text
    dev_set_sector_company.iat[i, 0] = sector+'[SEP]'+company+'[SEP]'+text

for i in range(len(test_set['text'])):
    text = test_set.iat[i, 0]
    sector = test_set.iat[i, 1]
    company = test_set.iat[i, 2]

    test_set_sector.iat[i, 0] = sector+'[SEP]'+text
    test_set_company.iat[i, 0] = company+'[SEP]'+text
    test_set_sector_company.iat[i, 0] = sector+'[SEP]'+company+'[SEP]'+text


os.mkdir(output_dir)
os.mkdir(output_dir+'/copyonly')
os.mkdir(output_dir+'/sector')
os.mkdir(output_dir+'/company')
os.mkdir(output_dir+'/sector_company')
train_set.to_csv(output_dir+'/copyonly'+'/train.tsv', sep='\t')
dev_set.to_csv(output_dir+'/copyonly'+'/dev.tsv', sep='\t')
test_set.to_csv(output_dir+'/copyonly'+'/test.tsv', sep='\t')

train_set_sector.to_csv(output_dir+'/sector'+'/train.tsv', sep='\t')
dev_set_sector.to_csv(output_dir+'/sector'+'/dev.tsv', sep='\t')
test_set_sector.to_csv(output_dir+'/sector'+'/test.tsv', sep='\t')

train_set_company.to_csv(output_dir+'/company'+'/train.tsv', sep='\t')
dev_set_company.to_csv(output_dir+'/company'+'/dev.tsv', sep='\t')
test_set_company.to_csv(output_dir+'/company'+'/test.tsv', sep='\t')

train_set_sector_company.to_csv(output_dir+'/sector_company'+'/train.tsv', sep='\t')
dev_set_sector_company.to_csv(output_dir+'/sector_company'+'/dev.tsv', sep='\t')
test_set_sector_company.to_csv(output_dir+'/sector_company'+'/test.tsv', sep='\t')
