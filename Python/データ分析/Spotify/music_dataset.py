import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials


client_id='b7b13bd7a57142a8b6341185f995e113'
client_secret='a96d4d1c448148be8074722c9219aa0c'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


#CSV読み込み
songs2019=pd.read_csv('./csv/regional-jp-daily-2019-06-09.csv')
songs2019.head()

songs2020=pd.read_csv('./csv/regional-jp-daily-2020-06-09.csv')
songs2020.head()

songs2021=pd.read_csv('./csv/regional-jp-daily-2021-06-09.csv')
songs2021.head()

songs2022=pd.read_csv('./csv/regional-jp-daily-2022-06-09.csv')
songs2022.head()

songs2023=pd.read_csv('./csv/regional-jp-daily-2023-06-09.csv')
songs2023.head()


#空のデータフレームを作成
song_info = pd.DataFrame()

# 除去するカラム名のリストを作成
columns_to_drop = ['type', 'id', 'uri', 'track_href', 'analysis_url']


#2019
#CSV内のuriカラムデータを変数uriへ
for uri in songs2019['uri']:

	#uriをキーとしてデータフレームにaudio_features情報を格納
	#これを変数dfへ
	df = pd.DataFrame.from_dict(spotify.audio_features(uri))

	# song_infoとdfを結合する
	song_info = pd.concat([song_info, df], ignore_index=True)

# songs2019とsong_infoを結合する
merged_df = pd.concat([songs2019, song_info], axis=1)

# 出力するCSVファイルのパスとファイル名を指定
output_file = "./csv/20190609_top200_songdata.csv"

# 特定のカラムを除去したデータフレームを作成
merged_df_2019 = merged_df.drop(columns=columns_to_drop)

# データフレームをCSVファイルに出力
merged_df_2019.to_csv(output_file, index=False, encoding='utf_8_sig', mode='w')

print('2019OK!')


df = df.drop(df.index)
song_info = song_info.drop(song_info.index)
merged_df = merged_df.drop(merged_df.index)


#2020
#CSV内のuriカラムデータを変数uriへ
for uri in songs2020['uri']:

	#uriをキーとしてデータフレームにaudio_features情報を格納
	#これを変数dfへ
	df = pd.DataFrame.from_dict(spotify.audio_features(uri))

	# song_infoとdfを結合する
	song_info = pd.concat([song_info, df], ignore_index=True)

# songs2020とsong_infoを結合する
merged_df = pd.concat([songs2020, song_info], axis=1)

# 出力するCSVファイルのパスとファイル名を指定
output_file = "./csv/20200609_top200_songdata.csv"

# 特定のカラムを除去したデータフレームを作成
merged_df_2020 = merged_df.drop(columns=columns_to_drop)

# データフレームをCSVファイルに出力
merged_df_2020.to_csv(output_file, index=False, encoding='utf_8_sig', mode='w')

print('2020OK!')


df = df.drop(df.index)
song_info = song_info.drop(song_info.index)
merged_df = merged_df.drop(merged_df.index)


#2021
#CSV内のuriカラムデータを変数uriへ
for uri in songs2021['uri']:

	#uriをキーとしてデータフレームにaudio_features情報を格納
	#これを変数dfへ
	df = pd.DataFrame.from_dict(spotify.audio_features(uri))

	# song_infoとdfを結合する
	song_info = pd.concat([song_info, df], ignore_index=True)

# songs2021とsong_infoを結合する
merged_df = pd.concat([songs2021, song_info], axis=1)

# 出力するCSVファイルのパスとファイル名を指定
output_file = "./csv/20210609_top200_songdata.csv"

# 特定のカラムを除去したデータフレームを作成
merged_df_2021 = merged_df.drop(columns=columns_to_drop)

# データフレームをCSVファイルに出力
merged_df_2021.to_csv(output_file, index=False, encoding='utf_8_sig', mode='w')

print('2021OK!')


df = df.drop(df.index)
song_info = song_info.drop(song_info.index)
merged_df = merged_df.drop(merged_df.index)


#2022
#CSV内のuriカラムデータを変数uriへ
for uri in songs2022['uri']:

	#uriをキーとしてデータフレームにaudio_features情報を格納
	#これを変数dfへ
	df = pd.DataFrame.from_dict(spotify.audio_features(uri))

    # song_infoとdfを結合する
	song_info = pd.concat([song_info, df], ignore_index=True)

# songs2022とsong_infoを結合する
merged_df = pd.concat([songs2022, song_info], axis=1)

# 出力するCSVファイルのパスとファイル名を指定
output_file = "./csv/20220609_top200_songdata.csv"

# 特定のカラムを除去したデータフレームを作成
merged_df_2022 = merged_df.drop(columns=columns_to_drop)

# データフレームをCSVファイルに出力
merged_df_2022.to_csv(output_file, index=False, encoding='utf_8_sig', mode='w')

print('2022OK!')


df = df.drop(df.index)
song_info = song_info.drop(song_info.index)
merged_df = merged_df.drop(merged_df.index)


#2023
#CSV内のuriカラムデータを変数uriへ
for uri in songs2023['uri']:

	#uriをキーとしてデータフレームにaudio_features情報を格納
	#これを変数dfへ
	df = pd.DataFrame.from_dict(spotify.audio_features(uri))

    # song_infoとdfを結合する
	song_info = pd.concat([song_info, df], ignore_index=True)

# songs2023とsong_infoを結合する
merged_df = pd.concat([songs2023, song_info], axis=1)

# 出力するCSVファイルのパスとファイル名を指定
output_file = "./csv/20230609_top200_songdata.csv"

# 特定のカラムを除去したデータフレームを作成
merged_df_2023 = merged_df.drop(columns=columns_to_drop)

# データフレームをCSVファイルに出力
merged_df_2023.to_csv(output_file, index=False, encoding='utf_8_sig', mode='w')

print('2023OK!')


print("CSVファイルが出力されました。")

