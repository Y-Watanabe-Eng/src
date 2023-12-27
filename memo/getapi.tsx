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



  return (
    <body>

      <header>
        <div className='h-28 bg-red-600 flex items-center justify-center'>
          <div className='w-9/12'>
            <h1 className='text-4xl text-white pt-4'>けんぴ。ちゃんテナ</h1>
            <p className='pt-2 pl-2'>from Youtube</p>
          </div>
        </div>
      </header>

      <main className="flex min-h-screen flex-col items-center justify-between p-24">
        <div className='grid sm:grid-cols-2 my-8 mx-4 py-4 px-4 border-solid border-gray-400 border-2 rounded'>
          <div className='my-4 mx-4'>

          </div>
          <div className='flex items-center justify-center'>

          </div>
        </div>
      </main>

    </body>

  )
}