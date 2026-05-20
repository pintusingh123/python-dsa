def decimal_converion(s:str):
  desimal_num = 0;
  power = 0 ;
  index = len(s)-1;
  while index >= 0:
   num = int(s[index]) * (2**power);
   desimal_num += num;
   index -= 1;
   power +=1;
  return desimal_num;

print(decimal_converion('110 1'));