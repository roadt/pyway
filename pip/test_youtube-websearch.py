import youtube_websearch as yt
import webbrowser

yt_basis = "https://www.youtube.com/watch?v="

search_results = yt.video_search('we will rock you')
# search_results = yt.search('we will rock you', useragent="something")  # you can set your own useragent
videoId = search_results[0]["videoId"]

webbrowser.open(yt_basis + videoId)
