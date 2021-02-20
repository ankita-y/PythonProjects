from wordcloud import WordCloud, STOPWORDS
import wikipedia
import matplotlib.pyplot as plt

stopwords = set(STOPWORDS)
result = wikipedia.summary("Amazon Web Services",sentences=6)
# result = wikipedia.page("Amazon Web Services")
# final_result = result.content
# print(final_result)
wordcloud = WordCloud(width=800, height = 500, background_color='black',
                          stopwords = stopwords,min_font_size=7).generate(result)
# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()