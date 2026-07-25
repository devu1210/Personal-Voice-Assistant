from news import get_news

articles = get_news()

print("\n" + "=" * 70)
print("📰                 TODAY'S TOP NEWS")
print("=" * 70)

if not articles:
    print("No news available.")
else:
    for i, article in enumerate(articles, start=1):
        print(f"\n{i}. {article['title']}")
        print(f"   🏢 Source : {article['source']['name']}")
        print(f"   🕒 Date   : {article['publishedAt'][:10]}")
        print(f"   🔗 Link   : {article['url']}")

print("\n" + "=" * 70)