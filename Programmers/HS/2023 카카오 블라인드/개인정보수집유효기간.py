from collections import defaultdict

# 1년은 12달
M = 12
# 1달은 28일
D = 28


def solution(today, terms, privacies):
    answer = []

    # 오늘 날짜를 일수로 변환
    today = date2days(today)

    # 약관 종류, 만료 기준일수
    terms_dict = defaultdict(list)

    for term in terms:
        # 약관종류, 유효기간
        term_type, term_exp = term.split()
        # 유효기간 달수를 일수로 변환
        days = month2days(term_exp)
        # 약관종류와 만료 기준일
        terms_dict[term_type] = today - days

    for i, privacy in enumerate(privacies, start=1):
        # 개인정보 수집일자, 약관 종류
        date, term_type = privacy.split()
        # 개인정보 수집일자를 날짜에서 일수로 변환
        days = date2days(date)
        # 만료기준일 이전이면 answer에 추가
        if days <= terms_dict[term_type]:
            answer.append(i)

    return answer


# 날짜를 일수로 변환하는 함수
def date2days(date: str) -> int:
    year, month, day = map(int, date.split('.'))
    return year * M * D + (month - 1) * D + (day - 1)


# 달수를 일수로 변환하는 함수
def month2days(month: str) -> int:
    return int(month) * D