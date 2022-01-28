import re

# Exercise

phrase_01 = "Gabriel tem o numero de celular (61)98258-9107, Karina tem o numero (00)91111-1111, Gilmara tem o numero (76)96547-8721"
find_all_phrase_01 = re.findall("\(\d{2}\)\d{5}-\d{4}", phrase_01)
print(find_all_phrase_01)

phrase_02 = "72.445-020, 87.657-50, 12.456-60"
find_all_phrase_02 = re.findall("\d{2}\.\d{3}-\d{2}",phrase_02)
print(find_all_phrase_02)

phrase_03 = "www.google.com.br, www.lol.com.br, www.ge.com.br, www.iesb.edu.br, www.youtube.com"
find_all_phrase_03 = re.findall("\w{3}\.[A-z]+\.\w{3}", phrase_03)
print(find_all_phrase_03)