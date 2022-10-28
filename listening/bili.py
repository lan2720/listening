# coding=utf-8
import requests
import re
import os
import json
from lxml import etree

headers = {
    'Referer': 'https://www.bilibili.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}


def get_all_urls(start_url):
    """获取有分p的所有视频的音频"""
    video_code = start_url.split('/')[4][:12] #提取B站视频的编号
    res = requests.get(url=start_url, headers=headers).text
    pattern_ = '<script>window.__INITIAL_STATE__=(.*?);\(function' # 提取分p视频列表信息的json数据
    n_ = re.findall(pattern_, res, re.S)
    xx_json = json.loads(n_[0])
    names = xx_json['videoData']['pages']# 提取分p视频的所有标题
    return names, video_code


def download_all_mp3_of_p(url_, save_dir="."):
    """
    获取有分p的所有视频的音频
    """
    os.makedirs(save_dir, exist_ok=True)
    data, code = get_all_urls(url_)
    for da in data:
        page_num = da['page']# 有多少个视频
        name = da['part']# 提取分p视频的所有标题
        url = 'https://www.bilibili.com/video/{}?p='.format(code) + str(page_num) #拼接所有的视频的url
        response = requests.get(url, headers).text
        pattern = '<script>window\.__playinfo__=(.*?)</script>' #提取音频url
        list_ = re.findall(pattern, response, re.S)
        list_json = json.loads(list_[0])
        volume_url = list_json['data']['dash']['audio'][0]['baseUrl']
        print(volume_url)
        save_filepath = os.path.join(save_dir, name + '.mp3') #保存路径
        audio = requests.get(url=volume_url, headers=headers).content
        with open(save_filepath, 'wb') as f:
            f.write(audio)
        print('下载完成')



def download_single_mp3_of_p(url, save_dir="."):
    """
    获取视频分p的单个特定视频的链接
    """
    os.makedirs(save_dir, exist_ok=True)
    pg_num = url.split('p=')[-1]
    response = requests.get(url, headers).text
    pattern = '<script>window\.__playinfo__=(.*?)</script>' # 提取音频url
    list_ = re.findall(pattern, response, re.S)
    pattern_ = '<script>window.__INITIAL_STATE__=(.*?);\(function' # 提取标题
    n_ = re.findall(pattern_, response, re.S)
    xx_json = json.loads(n_[0])
    names = xx_json['videoData']['pages']
    nn = 'sb'
    for name in names:
        if name['page'] == int(pg_num):
            nn = name['part']

    list_json = json.loads(list_[0])
    volume_url = list_json['data']['dash']['audio'][0]['baseUrl']
    print(volume_url)
    save_filepath = os.path.join(save_dir, nn + '.mp3')
    audio = requests.get(url=volume_url, headers=headers).content
    with open(save_filepath, 'wb') as f:
        f.write(audio)
    print('下载完成')


def download_mp3_no_p(url, save_dir="."):
    """
    获取没有分p视频的音频文件
    """
    os.makedirs(save_dir, exist_ok=True)
    response = requests.get(url, headers).text
    tree = etree.HTML(response)
    pattern = '<script>window\.__playinfo__=(.*?)</script>' #提取音频url
    list_ = re.findall(pattern, response, re.S)
    list_json = json.loads(list_[0])
    title = tree.xpath('//*[@id="viewbox_report"]/h1/span/text()')[0] # 获取标题
    volume_url = list_json['data']['dash']['audio'][0]['baseUrl']
    print(volume_url)
    save_filepath = os.path.join(save_dir, title + '.mp3')#保存路径
    audio = requests.get(url=volume_url, headers=headers).content
    with open(save_filepath, 'wb') as f:
        f.write(audio)
    print('下载完成')
