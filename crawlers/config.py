# create twitter app to access Twitter Streaming API (https://apps.twitter.com)
TWITTER = dict(
    consumer_key = '...',
    consumer_secret = '...',
    access_token = '...',
    access_secret = '...'
)

# Elasticsearch configurations
ELASTICSEARCH = dict(
    hostname = "localhost:9200",
    index = "hash_tweets" # new elastic collection index
    type = "doc"# new elastic collection type
)

# emotion hashtags keywords
KEYWORDS = dict( joy = [
"#accomplished",
"#alive",
"#amazing",
"#awesome"],
trust = [
"#acceptance",
"#admiration",
"#amused",
"#appreciated"],
fear = [
"#afraid",
"#anxious",
"#apprehension",
"#awe",
"#concerned"],
surprise = [
"#amazed",
"#amazement",
"#crazy",
"#different"],
sadness = [
"#alone",
"#ashamed",
"#awful",
"#awkward"],
disgust = [
"#bitter",
"#blah",
"#bored"
"#boredom"],
anger = [
"#aggravated",
"#aggressiveness",
"#anger",
"#anger2"],
anticipation = [
"#adventurous",
"#anticipation",
"#curious",
"#desperate"],
other = [
"#asleep",
"#awake",
"#brave",
"#busy"])