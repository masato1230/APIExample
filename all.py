import requests

# ご自身のAPIキーを入れてください
API_KEY = '8888888888888888888888888'


def get_by_securities(securities_code: str):
    """
    企業の証券コードを指定して有価証券報告書データを取得する
    使用例: get_by_securities('7203')
    返り値: 取得したJsonデータをPythonの辞書形式で返す
    """
    # JP Funda APIのエンドポイントurl
    url = 'https://www.jp-funda.com/api/jp/securities_code/' + securities_code
    headers = headers = {'Authorization': f'Token {API_KEY}'}

    res = requests.get(url, headers=headers)
    return res.json()


def get_by_securities_list(securities_code: str):
    """
    企業の証券コードを指定して有価証券報告書データ(数年分)を取得する
    使用例: get_by_securities_code_list('7201')
    返り値: 取得したJsonデータをPythonの辞書形式で返す
    """
    # JP Funda APIのエンドポイントurl
    url = 'https://www.jp-funda.com/api/jp/securities_code/list/' + \
          securities_code
    headers = headers = {'Authorization': f'Token {API_KEY}'}

    res = requests.get(url, headers=headers)
    return res.json()


def get_by_edinet(edinet_code: str):
    """
    企業のEDINETコードを指定して有価証券報告書データを取得する
    使用例: get_by_edinet('E02144')
    返り値: 取得したJsonデータをPythonの辞書形式で返す
    """
    # JP Funda APIのエンドポイントurl
    url = 'https://www.jp-funda.com/api/jp/edinet_code/' + edinet_code
    headers = headers = {'Authorization': f'Token {API_KEY}'}

    res = requests.get(url, headers=headers)
    return res.json()


def get_by_edinet_list(edinet_code: str):
    """
    企業のEDINETコードを指定して有価証券報告書データを取得する
    使用例: get_by_edinet_list('E02144')
    返り値: 取得したJsonデータをPythonの辞書形式で返す
    """
    # JP Funda APIのエンドポイントurl
    url = 'https://www.jp-funda.com/api/jp/edinet_code/list/' + edinet_code
    headers = headers = {'Authorization': f'Token {API_KEY}'}

    res = requests.get(url, headers=headers)
    return res.json()


def get_today():
    """
    今日公開された有価証券報告書のデータを取得する
    """
    url = 'https://www.jp-funda.com/api/jp/today/'
    headers = headers = {'Authorization': f'Token {API_KEY}'}

    res = requests.get(url, headers=headers)
    return res.json()


def get_yesterday():
    """
    昨日公開された有価証券報告書のデータを取得する
    """
    url = 'https://www.jp-funda.com/api/jp/yesterday/'
    headers = headers = {'Authorization': f'Token {API_KEY}'}

    res = requests.get(url, headers=headers)
    return res.json()


def get_week():
    """
    今日含めた1週間以内に公開されてた有価証券報告書のデータを取得する
    """
    url = 'https://www.jp-funda.com/api/jp/week/'
    headers = headers = {'Authorization': f'Token {API_KEY}'}

    res = requests.get(url, headers=headers)
    return res.json()


if __name__ == '__main__':
    # get_by_securities
    data = get_by_securities('7203')
    print(data)

    # get_by_securities_code_list
    data = get_by_securities_list('7201')
    print(data)

    # get_by_edinet
    data = get_by_edinet('E02144')
    print(data)

    # get_by_edinet_list
    data = get_by_edinet_list('E02144')
    print(data)

    # get_today
    data = get_today()
    print(data)

    # get_yesterday
    data = get_yesterday()
    print(data)

    # get_week
    data = get_week()
    print(data)
