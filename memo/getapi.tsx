async function getYoutube() {

  const apiKey = process.env.YOUTUBE_API_KEY
  const channelId = "UCUBvFfyuBrATTPxnAZ4OsCQ"

チャンネル情報の取得
  async function getChannel() {
//    'use server'

    const channelRes = await fetch(
      "https://www.googleapis.com/youtube/v3/channels?part=" +
        "contentDetails" +
        "&id=" +
        channelId + 
        "&key=" +
        apiKey
      )
      
    const channelData = await channelRes.json()

    return channelData;

  }

  const channelData = await getChannel()

  console.log(channelData)

  const uploadsId = channelData.items[0].contentDetails.relatedPlaylists.uploads
  
  console.log(uploadsId)

  
//プレイリスト情報の取得
  async function getPlaylist() {
//    'use server'

    const playlistRes = await fetch(
      "https://www.googleapis.com/youtube/v3/playlistItems?part=" +
        "contentDetails" +
        "&playlistId=" +
        uploadsId +
        "&maxResults=50" +
        "&key=" +
        apiKey
      )
      
    const playlistData = await playlistRes.json()

    return playlistData;

  }

  const playlistData = await getPlaylist()

  console.log(playlistData)

  const videoIdArray = []

  for (let i = 0; i < 50; i++) {
    videoIdArray.push(playlistData.items[i].contentDetails.videoId)
  }
  
  console.log(videoIdArray)
  
}

getYoutube()
