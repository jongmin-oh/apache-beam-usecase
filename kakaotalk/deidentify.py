import re

phone_patterns = {
    "number1": r"(\d{8,20})",
    "number2": r"(\d{2,6}[ -]-?\d{2,6}[ -]-?\d{2,6})",
    "number3": r"(\d{3,5}[ -]-?\d{3,5})",
}

email_patterns = {
    "email": r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",
}

account_patterns = {
    "acount": r"(\d{2,6}[ -]-?\d{2,6}[ -]-?\d{2,6}[ -]-?\d{2,6})"
}

address_patterns = {
    "ad1": r"(\S+[구군])\s+(\S+)\s+(\d{1,5}(-\d{1,5})?)?",
    "ad2": r"(\S+[구군])\s+(\S+)\s+(\d{1,5})\s?(길|로|길|로)\s?(\d{1,5}(-\d{1,5})?)?",
    "ad3": r"([가-힣A-Za-z·\d~\-.]+(읍|동|번지)\s)[\d]+",
    "ad4": r"([가-힣a-zA-Z\d]+(아파트|빌라|빌딩|마을))",
}


class DeIdentifier:
    @staticmethod
    def run_info(text):
        # 계좌번호 패턴
        for pattern in account_patterns.values():
            text = re.sub(pattern, "[계좌번호]", text)

        # 전화번호 패턴
        for pattern in phone_patterns.values():
            text = re.sub(pattern, "[휴대폰번호]", text)

        # 이메일 주소 패턴
        for pattern in email_patterns.values():
            text = re.sub(pattern, "[이메일]", text)

        # 주소 패턴
        for pattern in address_patterns.values():
            text = re.sub(pattern, "[주소]", text)

        return text

    @staticmethod
    def run_name(text, my_name, friend_name):
        text = text.replace(my_name, "[A]")
        text = text.replace(my_name[1:], "[A]")
        text = text.replace(friend_name, "[B]")
        text = text.replace(friend_name[1:], "[B]")
        return text


if __name__ == "__main__":
    sample_text = "전화번호: 010-1234-5678, 이메일: test@example.com, 계좌번호: 123-456-789-01, 주소: 서울시 강남구 강남대로 123"
    result_text = DeIdentifier.run(sample_text)
    print(result_text)