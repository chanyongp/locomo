import json
import re

def clean_and_parse_json(text):

    print(text)

    try:
        # 작은따옴표와 큰따옴표의 개수를 계산하여 처리
        single_quote_count = text.count("'")
        double_quote_count = text.count('"')

        # 작은따옴표가 더 많으면 큰따옴표로 변환
        if single_quote_count > double_quote_count:
            text = text.replace('"', "")  # 큰따옴표를 제거
            text = text.replace("'", '"')  # 작은따옴표를 큰따옴표로 변환

        # # 작은따옴표를 큰따옴표로 변환 (키-값 쌍에서 값에 해당하는 부분만 변경)
        # # 정규 표현식을 사용하여 작은따옴표로 묶인 값을 큰따옴표로 변환
        # text = re.sub(r"(?<=: )'([^']*)'", r'"\1"', text)

        # 텍스트에서 작은따옴표로 둘러싸인 값들을 찾아서 큰따옴표로 변환
        lines = text.splitlines()
        for i in range(len(lines)):
            # 값이 작은따옴표로 둘러싸인 경우만 처리
            if ":" in lines[i]:
                key, value = lines[i].split(":", 1)
                value = value.strip()
                # print(value)
                # value = value.replace("'", '"')
                # print(value)

                # 값이 작은따옴표로 감싸져 있으면 큰따옴표로 변경
                if value.startswith("'") or value.endswith("'"):
                    value = value.replace("'", '"')
                    # print(value)
                    lines[i] = f"{key}: {value}"
                    # print(lines[i])
        # print('\n'.join(lines))
        # print(text)

        # JSON 파싱 시도
        # return json.loads(text)
        return json.loads('\n'.join(lines))

    except json.JSONDecodeError as e:
        # JSON 파싱 실패 시 예외 처리
        print(f"Error decoding JSON: {e}")
        print(f"Text received(answer.strip()): {text}")  # 디버깅을 위한 출력
        return None  # 빈 값 반환하여 이후 코드가 중단되지 않도록 함

# 예시 텍스트
text = '''{
    "0": 'next month',
    "1": 'April 2023',
    "2": '1 May, 2023',
    "3": '16 May, 2023',
    "4": '16 May, 2023',
    "5": 'next month',
    "6": 'a new car',
    "7": 'Aerosmith',
    "8": 'to open a shop and work on classic cars',
    "9": 'classic cars',
    "10": 'a car accident and a flooded place',
    "11": 'to relax and recharge',
    "12": 'Japan',
    "13": 'a few months',
    "14": 'Aerosmith',
    "15": 'Tokyo',
    "16": 'to stay true to myself and sound unique',
    "17": 'opened my own car maintenance shop',
    "18": 'all kinds of cars, from regular maintenance to full restorations of classic cars',
    "19": 'a beautiful necklace with a diamond pendant'
}'''

# JSON 파싱 시도
parsed_json = clean_and_parse_json(text)
print(parsed_json)
