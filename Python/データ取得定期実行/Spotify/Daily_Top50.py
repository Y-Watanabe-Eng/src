from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import datetime


client_id='********************************'
client_secret='********************************'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

current_date = datetime.date.today().strftime('%Y-%m-%d')

# 保存先のパスを指定
save_path = '/home/ubuntu/app/Daily_Top50/csv/'

#空のデータフレームを作成
base_df = pd.DataFrame()

# 日付とプレイリストのIDを指定
date = current_date  # 現在の日付を使用する
playlist_id = '37i9dQZEVXbKXQ4mDTEBXq'  # 日本のTOP50プレイリストID

# プレイリストのトラックを取得
results = sp.playlist_items(playlist_id, fields='items(track(uri))', additional_types=['track'], market='JP')

# データフレームに変換
data = []
for item in results['items']:
    track = item['track']
    uri = track['uri']
    data.append({'URI': uri})

uri_df = pd.DataFrame(data)


data = []
for uri in uri_df['URI']:
    track_info = sp.track(uri)
    track_name = track_info['name']
    artist_names = ', '.join([artist['name'] for artist in track_info['artists']])
    popularity = track_info.get('popularity')
    
    data.append({
        '曲名': track_name,
        'アーティスト': artist_names,
        'URI': uri,
        '人気指数': popularity
    })

df = pd.DataFrame(data)

# データフレームに順位の列を追加
df.insert(0, 'ランク', range(1, len(df) + 1))


#df1内のuriカラムデータを変数uriへ
for uri in uri_df['URI']:

	#uriをキーとしてデータフレームにaudio_features情報を格納
	#これを変数features_dfへ
	features_df = pd.DataFrame.from_dict(sp.audio_features(uri))

	# base_dfとfeatures_dfを結合する
	base_df = pd.concat([base_df, features_df], ignore_index=True)

# dfとbase_dfを結合する
merged_df = pd.concat([df, base_df], axis=1)


# 除去するカラム名のリストを作成
columns_to_drop = ['type', 'id', 'uri', 'track_href', 'analysis_url']

# 特定のカラムを除去したデータフレームを作成
merged_df = merged_df.drop(columns=columns_to_drop)


columns_name = [
    'ランク', 
    '曲名', 
    'アーティスト', 
    'URI', 
    '人気指数', 
    'ダンス感', 
    'ラウド感', 
    'キー', 
    'dB値', 
    '調', 
    '言葉の密度',
    'アコースティック感',  
    'インストゥルメンタル', 
    'ライブ感', 
    '曲の明るさ',
    'BPM',
    '曲の長さ(ms)',
    '拍子'
    ]

merged_df = merged_df.rename(columns=dict(zip(merged_df.columns, columns_name)))


# CSVファイルに保存
merged_df.to_csv(f'{save_path}{date}_top50_JP.csv', index=False, encoding='utf_8_sig', mode='w')

print('Complete!')