import requests

# ご自身のAPIキーを入れてください
API_KEY = '88888888888888888888888888'


def get_by_securities(securities_code: str):
    """
    企業の証券コードを指定して有価証券報告書データを取得する
    使用例: get_by_securities('7203')
    返り値: 取得したJsonデータを返す
    """
    # JP Funda APIのエンドポイントurl
    url = 'https://www.jp-funda.com/api/jp/securities_code/' + securities_code
    headers = headers = {'Authorization': f'Token {API_KEY}'}

    res = requests.get(url, headers=headers)
    return res.json()


if __name__ == '__main__':

    data = get_by_securities('7203')
    print(data)
