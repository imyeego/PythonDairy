# _*_ coding:utf-8 _*_
import requests
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#print(json.dumps({'a': 'liuzhao', 'b': 7} ,sort_keys = True,indent = 4 ,separators = (',',': ')))

def getcomments(musicid):
	url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=ec5b9ab2b034958a8910d950b45d20a5'.format(musicid)
	payload = {
		'params': '0aNySJ+0sfqP+banoyon8mUqdXsaZgtxEj3rezh9rDQwaoG2nY7lDhuizPL1Ea4Vcg2eDk5H/N6Xat6IG/AcQywRPZUtp68RA7atOF3Cr9Iezj9cF7YlwAdTQooZgVBkjks5IidLeF92s1nQBPOPSxkK4rE73L74fCUI6vZp2I4apWk41o5Gqk77oUzqtetOcOiIPi2fc5KZTM/iXL3Bs2CTrZWzagFJ3hbZ/zXM/Ng=',
		'encSecKey': '30f33961f7f3a96399484c42f59054c4fc0c82171648d9d049d030da1d30482b0d6f476d3f99e8c78b4b203291a4020824d3a43d3c0f557a1842e1ef804c7c68547b8b079ac53bcde72acfa43af8fa9a295679fd902bbddcaeca3c7a201dc60d9208a80eb5716fe207cde7e670140b7851d33e27153503439084ed6ab1b33ab6'
	}
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
		'Referer': 'http://music.163.com/song?id={}'.format(musicid),
		'Host': 'music.163.com',
		'Origin': 'http://music.163.com'

	}

	response = requests.post(url = url, headers = headers, data = payload)
	data = json.loads(response.text)

	hotcomments = []
	for hotcomment in data['hotComments']:
		item = {
            'nickname': hotcomment['user']['nickname'],
            'content': hotcomment['content']
		}
		hotcomments.append(item)

	# 返回热门评论
	return [content['content'] for content in hotcomments]
	

if __name__ == '__main__':
	text = " ".join(getcomments(185879))

	wordcloud = WordCloud(random_state = 1, font_path = r'C:\\Windows\\Fonts\\msyh.ttc').generate(text)
	plt.figure()
	plt.imshow(wordcloud, interpolation = 'bilinear')
	plt.axis('off')
	plt.show()
'''
print('first')
print(__name__)

if __name__ == '__main__':
	print('second')

'''