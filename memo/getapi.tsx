async function getYoutube() {

  const apiKey = process.env.YOUTUBE_API_KEY
  const channelID = "UCUBvFfyuBrATTPxnAZ4OsCQ"

  async function getChannel() {
//    'use server'

    const channelRes = await fetch(
      "https://www.googleapis.com/youtube/v3/channels?part=" +
        "snippet" +
        "&id=" +
        channelID + 
        "&key=" +
        apiKey
      )
      
    const channelData = await channelRes.json()

    return channelData;

  }

  const channelData = await getChannel()

  console.log(channelData)

}

getYoutube()
