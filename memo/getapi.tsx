import { NextPage } from 'next'

interface Props {

}


export default function Youtube() {

  async function feed() {
    'use server'

    const apiKey = process.env.YOUTUBE_API_KEY
    const channelID = 'UCUBvFfyuBrATTPxnAZ4OsCQ'

    const channelRes = await fetch(

      'https://www.googleapis.com/youtube/v3/channels?part=' +
        'snippet' +
        '&id=' +
        channelID + 
        '&key=' +
        apiKey
    )

    const channelData = await channelRes.json()

    console.log(channelData)

}