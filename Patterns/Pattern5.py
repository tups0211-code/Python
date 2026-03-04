n = 5
for i in range(n):
  
  for j in range(i,n):      #[0,5]=5space [1,5]=4 space [2,5]=3 space
    print(" ",end=" ")
 
  for j in range(i):    #left star [0] no star [1]=1 star *  [2]= 2star
        print("*",end=" ")
 
  for j in range(i+1):  #right star [1] 1star  [2]=1+2=3 star [3]=3+2 = 5 star
        print("*",end=" ")
  print(" ")

#output : 

  #         *  
  #       * * *  
  #     * * * * *  
  #   * * * * * * *  
  # * * * * * * * * *  
