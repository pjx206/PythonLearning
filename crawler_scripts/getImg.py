import requests
import re, os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm


def getLink(src: str, pattern: str) -> list:
    """
    根据正则表达式找到链接所在字符串，需要后续处理得到链接
    """
    linkre = re.compile(pattern)
    linklist = linkre.findall(src)
    if linklist != None:
        return linklist[0]
    else:
        return None


def downloadImg(img_url, file_path):
    savepath = '\\'.join(file_path.split('\\')[:-1])
    if not os.path.exists(savepath):
        os.mkdir(savepath)

    req = requests.get(url=img_url)
    with open(file_path, 'wb') as f:
        f.write(req.content)


def main():
    """
    使用方法，自行搜索selenium配置教程，其实就是要下载一个chromedriver.exe, 放到chrome
    根目录。

    这个网站每一页的图片是一个http:*.webp, 跳转到这个链接还会继续跳转到图片真正的url
    （以'.jpg'结尾）
    """
    # 从这一章开始
    lastChapter = 'https://m.duoduomh.com/manhua/zujienvyou/847943.html'

    #避免后面的get参数比如 *.html?p=1 的影响，p是页书，而本脚本根据章节来保存下载下来的图片
    cmpLen = lastChapter.find('.html')

    opt = Options()
    opt.add_argument('--headless') # 设置无界面启动
    opt.add_argument('--disable-gpu')
    opt.add_argument('blink-settings=imagesEnabled=false')
    opt.add_argument('log-level=3')

    # 我的chrome （其实是百分浏览器根目录也在这
    exepath = r'G:\Program Files\CentBrowser\Application\chromedriver.exe'
    browser = webdriver.Chrome(executable_path=exepath, chrome_options=opt)

    # 开始的章节编号
    beginchap = 120
    # 总共128章
    chapters = [[] for i in range(128 - beginchap)]

    currentChap = lastChapter
    # for i in range(len(chapters)):
    bar = tqdm(range(len(chapters)))
    for i in bar:
        bar.set_description(" Downloading Chapter %d" % (i + beginchap))
        page = 0
        lastChapter = currentChap
        browser.get(currentChap)
        while currentChap[:cmpLen] == lastChapter[:cmpLen]:
            sleep(0.2) # 腾出时间给selenium进入链接

            img_link = getLink(browser.page_source, 'img id="page-.*webp')
            if img_link != None:
                img_link = img_link[img_link.find('src="') + 5:]
                chapters[i].append((img_link, page := page+1))

                rootpath = r'G:\Downloads\zjny'
                savepath = rootpath + \
                    '\\chap%d\\page%d.jpg' % (beginchap + i, page)

                downloadImg(img_link, savepath)

            # 根据xpath找到 下一页 按钮，并模拟点击，浏览器F12，右键单击html源码，找一找可以找到
            # 复制XPath的选项
            browser.find_element_by_xpath(
                '/html/body/div[1]/div[8]/div/ul/li[3]/a').click()

            currentChap = browser.current_url

    browser.quit()
    print("downloaing finished")
    print(chapters)

if __name__ == '__main__':
    main()