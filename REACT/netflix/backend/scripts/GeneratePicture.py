import requests

pixel_api_key = '14542612-035f6230f4fc0dcfefaf3e544'

def generatePicture(title):
    try:
        resp = requests.get(f'https://pixabay.com/api/?key={pixel_api_key}&q={title}&page=1&per_page=3')
        data = resp.json()
        pictures = data['hits']

        if len(pictures) < 1:
            img = ''
        else:
            img = pictures[0]['webformatURL']

        print(img)
        return img
    except Exception as e:
        print(str(e))
        return ''


if __name__ == "__main__":
    generatePicture('sponge')