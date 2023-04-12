# 批处理文本文件翻译器

此 Python 脚本使用 googletrans 库将指定文件夹中的所有 .txt 文件从一种语言批量翻译为另一种语言。 它利用谷歌翻译服务来执行翻译。

＃＃ 要求

- Python 3.6 或更高版本
- googletrans 库（版本 4.0.0-rc1）

＃＃ 安装

1. 确保系统上安装了 Python 3.6 或更高版本。 可以通过运行“python --version”或“python3 --version”来检查 Python 版本。

2. 使用pip安装需要的库：

pip install -r requirements.txt

＃＃ 用法

1. 在文本编辑器中打开脚本，将“path/to/input/folder”替换为包含要翻译的 .txt 文件的文件夹的路径。 同样，将“path/to/output/folder”替换为要保存翻译文件的文件夹路径。

2. 将“source_language”和“destination_language”变量设置为适当的语言代码（例如，“en”代表英语，“es”代表西班牙语，“zh-CN”代表简体中文）。

3. 使用命令运行脚本：

python batch_translate_txt_files.py

该脚本将处理输入文件夹中的每个 .txt 文件，翻译其内容，并将翻译后的文本保存到输出文件夹中同名的新文件中。

## 语言代码

可以在此处找到 Google 翻译支持的语言代码：

[https://cloud.google.com/translate/docs/languages](https://cloud.google.com/translate/docs/languages)

---

**作者:** 井韶子 & GPT4（笑死，老能摸鱼了）
**日期:** 2023年4月4日