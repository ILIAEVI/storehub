from django.contrib.auth.decorators import login_required



@login_required()
def make_order(request):
    pass


@login_required()
def order_list(request):
    pass