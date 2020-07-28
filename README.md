## In Defense of Podcast Full RSS Generator

Unfortunately, the RSS feed generator used by the author of the podcast, _In Defense of Plants_, only supports the most recent 100 episodes. Though they are all available on the website, this is rather inconvienient for how I often listen to podcasts.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Unfortunately my RSS feed will only provide podcatchers with the most recent 100 episodes. However, all episodes are freely available for streaming/downloading at <a href="https://t.co/AwPI28CUB8">https://t.co/AwPI28CUB8</a> - just search for episode numbers/topics in the search bar to locate them directly 🎧</p>&mdash; In Defense of Plants (@indfnsofplnts) <a href="https://twitter.com/indfnsofplnts/status/1287828213260066821?ref_src=twsrc%5Etfw">July 27, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

This script will scrape the podcast website and generate a custom RSS feed based on the information found there. **Note:** This does not host or move any of the content found on that website. It merely creates an RSS feed. You will still need to download the episodes from Matt's servers using your podcast app just like the official RSS.

### Installing

I recommend creating a virtual environment to run this script out of. Once created and activated, install the provided requirements file.

This script relies on FireFox and the latest [geckodriver ](https://github.com/mozilla/geckodriver) provided by Mozilla. If Firefox is not installed on your system, install it as normal. Place a copy of the geckodriver in this directory.
