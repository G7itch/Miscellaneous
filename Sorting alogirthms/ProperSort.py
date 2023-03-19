def sort(li:list,comp=None) -> Exception:
  """Returns 'fuck you' if you try and call it without a comparison function"""
  if comp==None:
    raise Exception("fuck you")
  else:
    return sorted(li,key=comp)


print(sort(["1","4","3","1"],len))
