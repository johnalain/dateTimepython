n : int = 1000_000_000
# # print(n)
# #add sepefrator _ or ,
# print(f'{n:_}')
# print(f'{n:,}')
# var: str = 'var'
# print(f'{var:_>20}')
# output                 var
# print(f'{var:#<20}')
#var 
#to center the text
# print(f'{var:|^20}' )
# withput _ or # or | 
# print(f'{var:>20}')
# print(f'{var:<20}')
# print(f'{var:^20}' ) 
#_________________var
#var#################
# ||||||||var|||||||||
#                  var
# var                 
#         var 
# from datetime import datetime
# now: datetime = datetime.now()
# print(f'{now:}')
#2024-03-05 08:45:06.058182

# print(f'{now:%d.%m.%y}')
#05.03.24

# print(f'{now:%d.%m.%y (%H:%M:%S)}')
# # 05.03.24 (08:50:28)
# print(f'{now:%c}')
# #Tue Mar  5 08:55:47 2024

# # format using am pm
# print(f'{now:%I%p}')
#08AM

# from datetime import datetime
# import pytz

# Create a timezone-aware datetime object
# ny_time = datetime.now(pytz.timezone('America/New_York'))
# formatted_time = ny_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
# print(formatted_time)
#for new city america 2024-03-05 02:07:08 EST-0500

# ny_time = datetime.now(pytz.timezone('America/Los_Angeles'))
# formatted_time = ny_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
# print(formatted_time)
# 2024-03-04 23:10:07 PST-0800

n: float =1234.5678
print(round(n ,2))
# output1234.57
# ican use to round to decimal point also this:
# print(f'{n: .2f}')

# print(f'result: ={n: .2f}')
# result: = 1234.57
#1234.57
# 1234.57
# print(f'{n: .0f}')
#completly remove decimal  1235

# print(f'{n: ,.3f}')
# 1,234.568

a: int = 5
b: int =10
my_var: str = "rita jose say hi"
print(f'a + b ={a + b}')
# a + b =15

# print(f'{a + b =}')
# a + b =15
print(f'{my_var}')



