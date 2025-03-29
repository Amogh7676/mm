class Test:
  def duplicate_elements(arr):
    c=[]
    c=list(set(arr))
    c.sort(reverse=True)
    return c
  arr=[1,2,1,12,3,4,5,1,]
  print(duplicate_elements(arr))

