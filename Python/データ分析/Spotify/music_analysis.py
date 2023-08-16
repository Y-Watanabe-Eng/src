import pandas as pd

top200_20190609_df = pd.read_csv('./csv/20190609_top200_songdata.csv')
top200_20190609_df.head()

top200_20200609_df = pd.read_csv('./csv/20200609_top200_songdata.csv')
top200_20200609_df.head()

top200_20210609_df = pd.read_csv('./csv/20210609_top200_songdata.csv')
top200_20210609_df.head()

top200_20220609_df = pd.read_csv('./csv/20220609_top200_songdata.csv')
top200_20220609_df.head()

top200_20230609_df = pd.read_csv('./csv/20230609_top200_songdata.csv')
top200_20230609_df.head()


columns_list = [
    'streams', 'tempo', 'duration_ms', 'energy', 'loudness', 'valence', 'danceability', 'acousticness', 'speechiness', 'instrumentalness'
    ]

ave_2019 = top200_20190609_df[columns_list].mean()

ave_2020 = top200_20200609_df[columns_list].mean()

ave_2021 = top200_20210609_df[columns_list].mean()

ave_2022 = top200_20220609_df[columns_list].mean()

ave_2023 = top200_20230609_df[columns_list].mean()


ave_df = pd.DataFrame(
    [ave_2019, ave_2020, ave_2021, ave_2022, ave_2023],
    index = ['2019', '2020', '2021', '2022', '2023']
)


columns_name = [
    '平均再生数', 'BPM', '曲の長さ(ms)', 'ラウド感', 'dB値', '曲の明るさ', 'ダンス感', 'アコースティック感', '言葉の密度', 'インスト度'
    ]

ave_df = ave_df.rename(columns=dict(zip(ave_df.columns, columns_name)))


ave_df.to_csv('./csv/ave_data.csv', index=True, encoding='utf_8_sig', mode='w')

print('出力しました。')