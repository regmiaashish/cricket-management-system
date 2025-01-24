from django.shortcuts import redirect

#-------authenticated
def auth(view_function):
  def wrapped_view(request, *args, **kwargs):
    if request.user.is_authenticated == False:
      return redirect('login')
    return view_function(request, *args,**kwargs)
  return wrapped_view

#-------authenticated
def guest(view_function):
  def wrapped_view(request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect('homepage')
    return view_function(request, *args,**kwargs)
  return wrapped_view


def staff(view_function):
    def wrapped_view(request, *args, **kwargs):
      if request.user.is_staff == False:
        return redirect('homepage')
      return view_function(request, *args,**kwargs)
    return wrapped_view
  
  
  