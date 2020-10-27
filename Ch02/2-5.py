"""
날짜 : 2020/07/23
이름 : 김철학
내용 : 파이썬 logging 실습하기
"""
import logging

# 기본 로그레벨 설정
logging.basicConfig(filename='./2-5.log', level=logging.DEBUG)

# 각 로그 레벨 기본출력
logging.debug('log debug...')
logging.info('log info...')
logging.warning('log warn...')
logging.error('log error...')
logging.fatal('log fatal...')

print('로그파일 생성완료...')