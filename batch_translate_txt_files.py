import os
import httpcore
from googletrans import Translator
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from time import sleep

# Add the retry decorator to the translate_file function
@retry(stop=stop_after_attempt(3), wait=wait_fixed(5), retry=retry_if_exception_type(httpcore.ConnectTimeout))
def translate_file(input_file_path, output_file_path, src_lang, dest_lang, punctuation):
    translator = Translator()
    translator.raise_Exception = True
    
    # Function to replace translated punctuation with English punctuation
    def replace_punctuation(text):
        punctuation_mapping = {
            '。': '.',
            '，': ',',
            '！': '!',
            '？': '?',
            '；': ';',
            '：': ':',
            '“': '"',
            '”': '"',
            '‘': "'",
            '’': "'",
            '（': '(',
            '）': ')',
            '《': '<',
            '》': '>',
            '【': '[',
            '】': ']',
            '—': '-',
            '、': ',',
            '……': '.',
        }
        for original, replacement in punctuation_mapping.items():
            text = text.replace(original, replacement)
        return text

    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        content = input_file.read()
        translated_text = translator.translate(content, src=src_lang, dest=dest_lang).text
        if punctuation == 'en':
            translated_text = replace_punctuation(translated_text)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(translated_text)


def batch_translate_txt_files(input_folder, output_folder, source_language, destination_language, punctuation):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.txt'):
            input_file_path = os.path.join(input_folder, file_name)
            output_file_path = os.path.join(output_folder, file_name)

            # Skip the file if it has already been translated
            if os.path.exists(output_file_path):
                print(f"{file_name} has already been translated. Skipping...")
                continue

            print(f"Translating {file_name}...")
            translate_file(input_file_path, output_file_path, source_language, destination_language, punctuation)
            print(f"Finished translating {file_name}")
            sleep(0.3)  # Wait a bit between file operations to avoid throttling from the Translation API


if __name__ == '__main__':
    input_folder = './tst_input' # 输入文件夹
    output_folder = './tst_output' # 输出文件夹
    source_language = 'en' # 语言代码，可以是英语，德语，繁体中文，简体中文等
    destination_language = 'zh-CN' 
    punctuation = 'en' # 标点符号，代表输出内容全部使用英文标点。若要使用中文标点符号，请将此值设为'zh-CN'

    batch_translate_txt_files(input_folder, output_folder, source_language, destination_language, punctuation)

