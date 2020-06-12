def solution(phone_book):
    for phone in phone_book:
        for another_phone in phone_book:
            if phone != another_phone and phone.startswith(another_phone):
                return False
    return True